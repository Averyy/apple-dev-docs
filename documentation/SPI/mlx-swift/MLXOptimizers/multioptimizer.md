---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/multioptimizer"
framework: "mlx-swift/MLXOptimizers"
---

# MultiOptimizer

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

An optimizer that delegates to several sub-optimizers, routing each parameter to the first optimizer whose filter matches.

## Declaration

```swift
class MultiOptimizer
```

#### Overview

This makes it easy to use different optimizers (or different hyperparameters) for different weights. The `filters` are predicates over a parameter’s flattened key path and its gradient and must be one fewer than `optimizers` – the last optimizer is the fallback and receives every parameter not matched by an earlier filter.

```swift
// Adam for everything except biases, which use SGD.
let optimizer = MultiOptimizer(
    optimizers: [SGD(learningRate: 0.1), Adam(learningRate: 1e-3)],
    filters: [{ key, _ in key.hasSuffix(".bias") }])
```

This is a port of Python `mlx.optimizers.MultiOptimizer`.

##### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Initializers
- [init(optimizers: [any Optimizer], filters: [(String, MLXArray) -> Bool])](./multioptimizer/init%28optimizers,filters%29.md)
### Instance Properties
- [let optimizers: [any Optimizer]](./multioptimizer/optimizers.md)
  The sub-optimizers; the last one is the fallback for unmatched parameters.
### Instance Methods
- [func innerState() -> [MLXArray]](./multioptimizer/innerstate%28%29.md)
- [func update(model: Module, gradients: ModuleParameters)](./multioptimizer/update%28model,gradients%29.md)
  Apply the gradients to the parameters of the model and update the model with the new parameters.

## Relationships

### Conforms To
- MLX.Evaluatable
- MLX.Updatable
- [Optimizer](./optimizer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/multioptimizer)*