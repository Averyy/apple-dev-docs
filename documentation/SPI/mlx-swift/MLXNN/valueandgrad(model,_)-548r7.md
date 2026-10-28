---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/valueandgrad(model:_:)-548r7"
framework: "mlx-swift/MLXNN"
---

# valueAndGrad(model:_:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Variant of `valueAndGrad(model:_:)` that can be used to pass an arbitrary number of `MLXArray` to a loss function.

## Declaration

```swift
func valueAndGrad<Model>(model: Model, _ f: @escaping (Model, [MLXArray]) -> [MLXArray]) -> (Model, [MLXArray]) -> ([MLXArray], ModuleParameters) where Model : Module
```

## Discussion

For example, given a loss function:

```swift
func loss(model: Model, a: MLXArray, b: MLXArray, c: MLXArray) -> MLXArray {
    ...
}
```

it can be wrapped as:

```swift
let vg = valueAndGrad(model: m) { model, args in
    // wrap the result in an array
    [loss(model: model, a: args[0], b: args[1], c: args[2])]
}
```

### See Also

- [Training a Model](./training.md)
- [`valueAndGrad(model:_:)`](./valueandgrad%28model,_%29-12a2c.md)

## See Also

### Value and Grad
- [func valueAndGrad<Model>(model: Model, (Model, MLXArray, MLXArray) -> MLXArray) -> (Model, MLXArray, MLXArray) -> (MLXArray, ModuleParameters)](./valueandgrad%28model,_%29-12a2c.md)
  Transform the passed function `f(Model, MLXArray, MLXArray)` to a function that computes the gradients of `f` with regard to the model’s trainable parameters and also its value.
- [func valueAndGrad<Model, Arguments>(model: Model, (Model, Arguments) -> [MLXArray]) -> (Model, Arguments) -> ([MLXArray], ModuleParameters)](./valueandgrad%28model,_%29-45dg5.md)
  Variant of `valueAndGrad(model:_:)` that can be used to pass an arbitrary parameters to a loss function.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/valueandgrad(model:_:)-548r7)*