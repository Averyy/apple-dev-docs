---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/moduleinfo"
framework: "mlx-swift/MLXNN"
---

# ModuleInfo

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

ModuleInfo can provde information about child modules and act as an update point for [`update(modules:verify:path:modulePath:)`](./module/update%28modules,verify,path,modulepath%29.md).

## Declaration

```swift
@propertyWrapper
class ModuleInfo<T>
```

## Mentions

- [Creating Modules](./custom-layers.md)

#### Overview

The keys for modules and parameters are usually named after their instance variables, but `feed_forward` would not be a very Swifty variable name:

```python
class TransformerBlock(nn.Module):
    def __init__(self, args: ModelArgs):
        super().__init__()
        ...
        self.feed_forward = FeedForward(args=args)
```

Instead we can use [`ModuleInfo`](./moduleinfo.md) to supply a replacement key that matches the python version:

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

##### See Also

- [Creating Modules](./custom-layers.md)
- [`ParameterInfo`](./parameterinfo.md)

## Topics

### Initializers
- [init(key: String?)](./moduleinfo/init%28key%29.md)
- [init(wrappedValue: T, key: String?)](./moduleinfo/init%28wrappedvalue,key%29.md)
### Instance Properties
- [var wrappedValue: T](./moduleinfo/wrappedvalue.md)

## See Also

### Base Classes and Interfaces
- [class Module](./module.md)
  Base class for building neural networks with MLX.
- [protocol UnaryLayer](./unarylayer.md)
  A `Layer` ([`Module`](./module.md) subclass) that can be evaluated as a *unary function*.
- [protocol Quantizable](./quantizable.md)
  Protocol for layers that can be quantized
- [class ParameterInfo](./parameterinfo.md)
  ParameterInfo allows you to specify alternate keys for parameter propreties.
- [typealias ModuleParameters](./moduleparameters.md)
  `NestedDictionary` structure of `MLXArray`
- [typealias ModuleChildren](./modulechildren.md)
  `NestedDictionary` structure of `Module`
- [typealias ModuleItem](./moduleitem.md)
  Single item from [`items()`](./module/items%28%29.md)
- [typealias ModuleItems](./moduleitems.md)
  `NestedDictionary` structure of `ModuleValue` from [`items()`](./module/items%28%29.md)
- [enum ModuleValue](./modulevalue.md)
  A single value from [`Module`](./module.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/moduleinfo)*