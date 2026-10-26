---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/optimizer"
framework: "mlx-swift/MLXOptimizers"
---

# Optimizer

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: protocol  
**Role**: Protocol

Public interface for all Optimizer types.

## Declaration

```swift
protocol Optimizer : Evaluatable, Updatable
```

##### See Also

- [MLXOptimizers](./MLXOptimizers.md)
- [`OptimizerBase`](./optimizerbase.md)

## Topics

### Instance Methods
- [func update(model: Module, gradients: ModuleParameters)](./optimizer/update%28model,gradients%29.md)
  Apply the gradients to the parameters of the model and update the model with the new parameters.

## Relationships

### Inherits From
- MLX.Evaluatable
- MLX.Updatable
### Conforming Types
- [AdaDelta](./adadelta.md)
- [AdaGrad](./adagrad.md)
- [Adafactor](./adafactor.md)
- [Adam](./adam.md)
- [AdamW](./adamw.md)
- [Adamax](./adamax.md)
- [Lion](./lion.md)
- [MultiOptimizer](./multioptimizer.md)
- [Muon](./muon.md)
- [OptimizerBase](./optimizerbase.md)
- [OptimizerBaseArrayState](./optimizerbasearraystate.md)
- [RMSprop](./rmsprop.md)
- [SGD](./sgd.md)

## See Also

### Base Classes and Protocols
- [class OptimizerBase](./optimizerbase.md)
  The base class for all optimizers. It allows us to implement an optimizer on a per-parameter basis and apply it to a parameter tree.
- [class OptimizerBaseArrayState](./optimizerbasearraystate.md)
  Convenience subclass of OptimizerBase that provides `MLXArray` State.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/optimizer)*