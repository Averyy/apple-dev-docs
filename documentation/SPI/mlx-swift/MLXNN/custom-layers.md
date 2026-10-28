---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/custom-layers"
framework: "mlx-swift/MLXNN"
---

# Creating Modules

**Framework**: mlx-swift/MLXNN  
**Role**: Article

Creating custom modules using `MLXNN`.

## Neural Networks

Writing arbitrarily complex neural networks in MLX can be done using only `MLXArray` and `valueAndGrad()`.  However, this requires the user to write again and again the same simple neural network operations as well as handle all the parameter state and initialization manually and explicitly.

The [MLXNN](./MLXNN.md) package solves this problem by providing an intuitive way of composing neural network layers, initializing their parameters, freezing them for finetuning and more.

## The Module Class

The workhorse of any neural network library is the [`Module`](./module.md) class. In MLX the [`Module`](./module.md) class is a container of `MLXArray` or [`Module`](./module.md) instances. Its main function is to provide a way to recursively **access** and **update** its parameters and those of its submodules.

Creating a new [`Module`](./module.md) subclass from scratch looks like this:

```swift
// 1. Declare your class
// 2. Since this class takes a single MLXArray argument we can declare as UnaryLayer
public class FeedForward : Module, UnaryLayer {
    
    // 3. Declare your sub-modules and parameters as needed
    // 4. See section on ModuleInfo/ParameterInfo below
    @ModuleInfo var w1: Linear
    @ModuleInfo var w2: Linear
    @ModuleInfo var w3: Linear
    
    // 5. Initialize your ivars
    public init(dimensions: Int, hiddenDimensions: Int, outputDimensions: Int) {
        self.w1 = Linear(dimensions, hiddenDimensions, bias: false)
        self.w2 = Linear(hiddenDimensions, dimensions, bias: false)
        self.w3 = Linear(dimensions, outputDimensions, bias: false)
    }
    
    // 6. Provide the API to call it
    public func callAsFunction(_ x: MLXArray) -> MLXArray {
        w2(silu(w1(x)) * w3(x))
    }
}
```

This will declare a `FeedForward` layer similar to [the layer in the Mistral Example](https://github.com/ml-explore/mlx-examples/blob/main/llms/mistral/mistral.py).

This layer can be used:

```swift
let layer = FeedForward(dimensions: 20, hiddenDimensions: 64, outputDimensions: 20)

let input: MLXArray

// this calls the `callAsFunction()`
let output = layer(input)
```

See the *Converting From Python* section about other considerations when converting code.

### Parameters

A parameter of a module is any public member of type `MLXArray` (its name should not start with `_`). It can be arbitrarily nested in other [`Module`](./module.md) instances or `[MLXArray]` and `[String:MLXArray]`.

[`parameters()`](./module/parameters%28%29.md) can be used to extract a `NestedDictionary` ([`ModuleParameters`](./moduleparameters.md)) with all the parameters of a module and its submodules.

A [`Module`](./module.md) can also keep track of “frozen” parameters. See the [`freeze(recursive:keys:strict:)`](./module/freeze%28recursive,keys,strict%29.md) method for more details. These parameters will not be considered when computing gradients and updating weights via [`valueAndGrad(model:_:)`](./valueandgrad%28model,_%29-12a2c.md).

See the *ModuleInfo and ParameterInfo* section for more information about using these in swift.

### Updating the Parameters

MLX modules allow accessing and updating individual parameters. However, most times we need to update large subsets of a module’s parameters. This action is performed by [`update(parameters:verify:path:modulePath:)`](./module/update%28parameters,verify,path,modulepath%29.md).

See also [Training a Model](./training.md).

### Inspecting Modules

The simplest way to see the model architecture is to print it. Following along with the above example, you can print the `FeedForward` with:

```swift
print(layer)
```

This will display:

```
FeedForward {
  w1: Linear(inputDimensions=20, outputDimensions=64, bias=false),
  w2: Linear(inputDimensions=64, outputDimensions=20, bias=false),
  w3: Linear(inputDimensions=20, outputDimensions=20, bias=false),
}
```

To get more detailed information on the arrays in a [`Module`](./module.md) you can use [`mapParameters(map:isLeaf:)`](./module/mapparameters%28map,isleaf%29.md).  For example to see the shapes of all the parameters from above:

```swift
print(layer.mapParameters { $0.shape })
```

resulting in:

```
[
  w1: [
    weight: [64, 20]
  ],
  w2: [
    weight: [20, 64]
  ],
  w3: [
    weight: [20, 20]
  ]
]
```

## ModuleInfo and ParameterInfo

The [`ModuleInfo`](./moduleinfo.md) and [`ParameterInfo`](./parameterinfo.md) provide two important features for module instance variables:

- both property wrappers allow replacement keys to be specified
- the [`ModuleInfo`](./moduleinfo.md) allows [`update(modules:verify:path:modulePath:)`](./module/update%28modules,verify,path,modulepath%29.md) to replace the module

Replacement keys are important because many times models and weights are defined in terms of their python implementation.  For example [here is a definition of a module](https://github.com/ml-explore/mlx-examples/blob/main/llms/mistral/mistral.py):

```python
class TransformerBlock(nn.Module):
    def __init__(self, args: ModelArgs):
        super().__init__()
        self.n_heads = args.n_heads
        self.dim = args.dim
        self.attention = Attention(args)
        self.feed_forward = FeedForward(args=args)
        self.attention_norm = RMSNorm(args.dim, eps=args.norm_eps)
        self.ffn_norm = RMSNorm(args.dim, eps=args.norm_eps)
        self.args = args
```

The keys for modules and parameters are usually named after their instance variables, but `feed_forward` would not be a very Swifty variable name.  Instead we can use [`ModuleInfo`](./moduleinfo.md) to supply a replacement key:

```swift
public class TransformerBlock : Module {
    
    let attention: Attention
    
    @ModuleInfo(key: "feed_forward") var feedForward: FeedForward
    @ModuleInfo(key: "attention_norm") var attentionNorm: RMSNorm
    @ModuleInfo(key: "ffn_norm") var ffnNorm: RMSNorm

    public init(_ args: Configuration) {
        self.attention = Attention(args)
        self._feedForward.wrappedValue = FeedForward(args)
        self._attentionNorm.wrappedValue = RMSNorm(args.dimensions, eps: args.normEps)
        self._ffnNorm.wrappedValue = RMSNorm(args.dimensions, eps: args.normEps)
    }
```

All [`Linear`](./linear.md) modules should use a [`ModuleInfo`](./moduleinfo.md) so that [`quantize(model:groupSize:bits:predicate:)`](./quantizedlinear/quantize%28model,groupsize,bits,predicate%29.md) can replace them at runtime:

```swift
public class FeedForward : Module {
    
    @ModuleInfo var w1: Linear
    @ModuleInfo var w2: Linear
    @ModuleInfo var w3: Linear
    
    public init(_ args: Configuration) {
        self.w1 = Linear(args.dimensions, args.hiddenDimensions, bias: false)
        self.w2 = Linear(args.hiddenDimensions, args.dimensions, bias: false)
        self.w3 = Linear(args.dimensions, args.hiddenDimensions, bias: false)
    }
```

The `ModuleInfo` provides a hook for [`QuantizedLinear`](./quantizedlinear.md) and [`update(modules:verify:path:modulePath:)`](./module/update%28modules,verify,path,modulepath%29.md) to replace the contents of `w1`, etc. with a new compatible `Model` after it is created.

Note that `MLXArray` is settable without any [`ParameterInfo`](./parameterinfo.md) – it has an `update()` method.

## Converting From Python

Consider [this example from a Llama model](https://github.com/ml-explore/mlx-examples/blob/main/llms/mlx_lm/models/llama.py):

```python
class RMSNorm(nn.Module):
    def __init__(self, dims: int, eps: float = 1e-5):
        super().__init__()
        self.weight = mx.ones((dims,))
        self.eps = eps

    def _norm(self, x):
        return x * mx.rsqrt(x.square().mean(-1, keepdims=True) + self.eps)

    def __call__(self, x):
        output = self._norm(x.astype(mx.float32)).astype(x.dtype)
        return self.weight * output
```

The straightforward conversion might look like this:

```swift
public class RMSNorm : Module {
    
    // swift uses declared ivars rather than properties dynamically created in init
    let weight: MLXArray
    let eps: Float

    public init(_ dimensions: Int, eps: Float = 1e-5) {
        self.weight = MLXArray.ones([dimensions])
        self.eps = eps
        super.init()
    }

    // we can use `internal` (default) or `private` functions for internal implementation
    func norm(_ x: MLXArray) -> MLXArray {
        x * rsqrt(x.square().mean(axis: -1, keepDims: true) + self.eps)
    }
    
    // this is the equivalent of the `__call__()` method from python and it
    // allows use like:
    //
    // let result = norm(input)
    public func callAsFunction(_ x: MLXArray) -> MLXArray {
        let output = norm(x.asType(.float32)).asType(x.dtype)
        return weight * output
    }
}
```

Here is another example that has parameters (`MLXArray`) from the `mlx.nn` package (both sans documentation):

```python
class Linear(Module):
    def __init__(self, input_dims: int, output_dims: int, bias: bool = True) -> None:
        super().__init__()
        scale = math.sqrt(1.0 / input_dims)
        self.weight = mx.random.uniform(
            low=-scale,
            high=scale,
            shape=(output_dims, input_dims),
        )
        if bias:
            self.bias = mx.random.uniform(
                low=-scale,
                high=scale,
                shape=(output_dims,),
            )

    def _extra_repr(self) -> str:
        return f"input_dims={self.weight.shape[1]}, output_dims={self.weight.shape[0]}, bias={'bias' in self}"

    def __call__(self, x: mx.array) -> mx.array:
        x = x @ self.weight.T
        if "bias" in self:
            x = x + self.bias
        return x
```

and the swift conversion:

```swift
public class Linear: Module, UnaryLayer {

    let weight: MLXArray
    let bias: MLXArray?

    public init(_ inputDimensions: Int, _ outputDimensions: Int, bias: Bool = true) {
        let scale = sqrt(1.0 / Float(inputDimensions))
        self.weight = MLXRandom.uniform(-scale ..< scale, [outputDimensions, inputDimensions])
        if bias {
            self.bias = MLXRandom.uniform(-scale ..< scale, [outputDimensions])
        } else {
            self.bias = nil
        }
        super.init()
    }

    internal init(weight: MLXArray, bias: MLXArray? = nil) {
        self.weight = weight
        self.bias = bias
    }

    public override func describeExtra(_ indent: Int) -> String {
        "(inputDimensions=\(weight.dim(1)), outputDimensions=\(weight.dim(0)), bias=\(bias == nil ? "false" : "true"))"
    }

    public func callAsFunction(_ x: MLXArray) -> MLXArray {
        var result = x.matmul(weight.T)
        if let bias {
            result = result + bias
        }
        return result
    }
}
```

## See Also

### Articles
- [Training a Model](./training.md)
  A model training loop.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/custom-layers)*