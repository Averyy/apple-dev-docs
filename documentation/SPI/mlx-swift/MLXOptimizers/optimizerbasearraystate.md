---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/optimizerbasearraystate"
framework: "mlx-swift/MLXOptimizers"
---

# OptimizerBaseArrayState

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

Convenience subclass of OptimizerBase that provides `MLXArray` State.

## Declaration

```swift
class OptimizerBaseArrayState
```

##### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Instance Methods
- [func newState(parameter: MLXArray) -> MLXArray](./optimizerbasearraystate/newstate%28parameter%29.md)
  Subclasses must implement this to create a new `State` when needed.  This is called for each parameter in the model.

## Relationships

### Inherits From
- [OptimizerBase](./optimizerbase.md)
### Inherited By
- [AdaGrad](./adagrad.md)
- [Lion](./lion.md)
- [Muon](./muon.md)
- [RMSprop](./rmsprop.md)
- [SGD](./sgd.md)
### Conforms To
- MLX.Evaluatable
- MLX.Updatable
- [Optimizer](./optimizer.md)

## See Also

### Base Classes and Protocols
- [protocol Optimizer](./optimizer.md)
  Public interface for all Optimizer types.
- [class OptimizerBase](./optimizerbase.md)
  The base class for all optimizers. It allows us to implement an optimizer on a per-parameter basis and apply it to a parameter tree.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/optimizerbasearraystate)*