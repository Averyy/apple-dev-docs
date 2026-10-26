---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/valueandgrad(model:_:)-12a2c"
framework: "mlx-swift/MLXNN"
---

# valueAndGrad(model:_:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Transform the passed function `f(Model, MLXArray, MLXArray)` to a function that computes the gradients of `f` with regard to the model’s trainable parameters and also its value.

## Declaration

```swift
func valueAndGrad<Model>(model: Model, _ f: @escaping (Model, MLXArray, MLXArray) -> MLXArray) -> (Model, MLXArray, MLXArray) -> (MLXArray, ModuleParameters) where Model : Module
```

## Mentions

- [Creating Modules](./custom-layers.md)
- [Training a Model](./training.md)

#### Return Value

Function that returns the value of `f()` and the gradient of the parameters of the model

#### Discussion

For example:

```swift
class M : Module, UnaryLayer { ... }

// create the model and realize the parameters
let m = M()
MLX.eval(m)

// input and targets
let x = MLXArray(0 ..< 5, [1, 5])
let y = MLXArray(0 ..< 5)

func loss(model: M, x: MLXArray, y: MLXArray) -> MLXArray {
    crossEntropy(logits: model(x), targets: y, reduction: .mean)
}

let lg = valueAndGrad(model: m, loss)

// loss is a scalar MLXArray with the loss value and
// grads are something that could be fed to an Optimizer
// to produce an update for the model parameters.
let (loss, grads) = lg(m, x, y)
```

##### Other Arguments

If other arguments to the loss function are needed there are two variants of `valueAndGrad()` that can be used to build these:

- [`valueAndGrad(model:_:)`](./valueandgrad%28model,_%29-548r7.md) – passing only `[MLXArray]` and returning `[MLXArray]`
- [`valueAndGrad(model:_:)`](./valueandgrad%28model,_%29-45dg5.md)– passing any arguments and returning `[MLXArray]`

Prefer the former as it can cache the value of the underlying `valueAndGrad()` call while the latter must rebuild it for each call.

##### See Also

- [Training a Model](./training.md)

## Parameters

- `model`: Model to apply parameters to
- `f`: Function to compute the gradients for

## See Also

### Value and Grad
- [func valueAndGrad<Model>(model: Model, (Model, [MLXArray]) -> [MLXArray]) -> (Model, [MLXArray]) -> ([MLXArray], ModuleParameters)](./valueandgrad%28model,_%29-548r7.md)
  Variant of `valueAndGrad(model:_:)` that can be used to pass an arbitrary number of `MLXArray` to a loss function.
- [func valueAndGrad<Model, Arguments>(model: Model, (Model, Arguments) -> [MLXArray]) -> (Model, Arguments) -> ([MLXArray], ModuleParameters)](./valueandgrad%28model,_%29-45dg5.md)
  Variant of `valueAndGrad(model:_:)` that can be used to pass an arbitrary parameters to a loss function.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/valueandgrad(model:_:)-12a2c)*