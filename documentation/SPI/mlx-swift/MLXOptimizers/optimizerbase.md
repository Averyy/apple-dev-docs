---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/optimizerbase"
framework: "mlx-swift/MLXOptimizers"
---

# OptimizerBase

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

The base class for all optimizers. It allows us to implement an optimizer on a per-parameter basis and apply it to a parameter tree.

## Declaration

```swift
class OptimizerBase<State> where State : Updatable
```

## Overview

Subclasses need to implement:

- `func newState(parameter: MLXArray) -> State`
- `func applySingle(gradient: MLXArray, parameter: MLXArray, state: State) -> (MLXArray, State)`

### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: State) -> (MLXArray, State)](./optimizerbase/applysingle%28gradient,parameter,state%29.md)
- [func innerState() -> [MLXArray]](./optimizerbase/innerstate%28%29.md)
- [func newState(parameter: MLXArray) -> State](./optimizerbase/newstate%28parameter%29.md)
  Subclasses must implement this to create a new `State` when needed.  This is called for each parameter in the model.
- [func update(model: Module, gradients: ModuleParameters)](./optimizerbase/update%28model,gradients%29.md)
  Apply the gradients to the parameters of the model and update the model with the new parameters.

## Relationships

### Inherited By
- [AdaDelta](./adadelta.md)
- [Adafactor](./adafactor.md)
- [Adam](./adam.md)
- [Adamax](./adamax.md)
- [OptimizerBaseArrayState](./optimizerbasearraystate.md)
### Conforms To
- MLX.Evaluatable
- MLX.Updatable
- [Optimizer](./optimizer.md)

## See Also

### Base Classes and Protocols
- [protocol Optimizer](./optimizer.md)
  Public interface for all Optimizer types.
- [class OptimizerBaseArrayState](./optimizerbasearraystate.md)
  Convenience subclass of OptimizerBase that provides `MLXArray` State.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/optimizerbase)*