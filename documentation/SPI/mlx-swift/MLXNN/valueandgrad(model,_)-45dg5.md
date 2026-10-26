---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/valueandgrad(model:_:)-45dg5"
framework: "mlx-swift/MLXNN"
---

# valueAndGrad(model:_:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Variant of `valueAndGrad(model:_:)` that can be used to pass an arbitrary parameters to a loss function.

## Declaration

```swift
func valueAndGrad<Model, Arguments>(model: Model, _ f: @escaping (Model, Arguments) -> [MLXArray]) -> (Model, Arguments) -> ([MLXArray], ModuleParameters) where Model : Module
```

#### Discussion

> **Note**: Prefer the other `valueAndGrad(model:_:)` functions if the arguments are all `MLXArray`. This variant requires re-constructing the gradient function per call.

For example, given a loss function:

```swift
func loss(model: Model, a: MLXArray, x: Int) -> MLXArray {
    ...
}
```

it can be wrapped as:

```swift
let vg = valueAndGrad(model: m) { (model: Module, args: (MLXArray, Int)) in
    // wrap the result in an array
    [loss(model: model, a: args.0, x: args.1)]
}
```

##### See Also

- [Training a Model](./training.md)
- [`valueAndGrad(model:_:)`](./valueandgrad%28model,_%29-12a2c.md)

## See Also

### Value and Grad
- [func valueAndGrad<Model>(model: Model, (Model, MLXArray, MLXArray) -> MLXArray) -> (Model, MLXArray, MLXArray) -> (MLXArray, ModuleParameters)](./valueandgrad%28model,_%29-12a2c.md)
  Transform the passed function `f(Model, MLXArray, MLXArray)` to a function that computes the gradients of `f` with regard to the model’s trainable parameters and also its value.
- [func valueAndGrad<Model>(model: Model, (Model, [MLXArray]) -> [MLXArray]) -> (Model, [MLXArray]) -> ([MLXArray], ModuleParameters)](./valueandgrad%28model,_%29-548r7.md)
  Variant of `valueAndGrad(model:_:)` that can be used to pass an arbitrary number of `MLXArray` to a loss function.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/valueandgrad(model:_:)-45dg5)*