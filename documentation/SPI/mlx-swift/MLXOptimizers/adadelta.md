---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adadelta"
framework: "mlx-swift/MLXOptimizers"
---

# AdaDelta

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

The AdaDelta optimizer with a learning rate [1].

## Declaration

```swift
class AdaDelta
```

## Overview

Our AdaDelta implementation follows the original paper. In detail,

[1]: Zeiler, M.D., 2012. ADADELTA: an adaptive learning rate method. arXiv preprint arXiv:1212.5701.

### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Initializers
- [init(learningRate: Float, rho: Float, eps: Float)](./adadelta/init%28learningrate,rho,eps%29.md)
  Initialize the optimizer.
### Instance Properties
- [var eps: Float](./adadelta/eps.md)
  The epsilon added to the denominator to improve numerical stability
- [var learningRate: Float](./adadelta/learningrate.md)
  The learning rate
- [var rho: Float](./adadelta/rho.md)
  The coefficient used for computing a running average of squared gradients
### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: TupleState) -> (MLXArray, TupleState)](./adadelta/applysingle%28gradient,parameter,state%29.md)
- [func newState(parameter: MLXArray) -> TupleState](./adadelta/newstate%28parameter%29.md)
  Subclasses must implement this to create a new `State` when needed.  This is called for each parameter in the model.

## Relationships

### Inherits From
- [OptimizerBase](./optimizerbase.md)
### Conforms To
- MLX.Evaluatable
- MLX.Updatable
- [Optimizer](./optimizer.md)

## See Also

### Optimizers
- [class Adafactor](./adafactor.md)
  The Adafactor optimizer.
- [class AdaGrad](./adagrad.md)
  The Adagrad optimizer [1].
- [class AdamW](./adamw.md)
  The AdamW optimizer [1].
- [class Adam](./adam.md)
  The Adam optimizer [1].
- [class Adamax](./adamax.md)
  The Adamax optimizer, a variant of Adam based on the infinity norm [1].
- [class Lion](./lion.md)
  The Lion optimizer [1].
- [class RMSprop](./rmsprop.md)
  The RMSprop optimizer [1].
- [class SGD](./sgd.md)
  Stochastic gradient descent optimizer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adadelta)*