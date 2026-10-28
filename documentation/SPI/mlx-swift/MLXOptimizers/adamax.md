---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adamax"
framework: "mlx-swift/MLXOptimizers"
---

# Adamax

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

The Adamax optimizer, a variant of Adam based on the infinity norm [1].

## Declaration

```swift
class Adamax
```

## Overview

Our Adam implementation follows the original paper and omits the bias correction in the first and second moment estimates. In detail,

[1]: Kingma, D.P. and Ba, J., 2015. Adam: A method for stochastic optimization. ICLR 2015.

### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Initializers
- [init(learningRate: Float, betas: (Float, Float), eps: Float)](./adamax/init%28learningrate,betas,eps%29.md)
  Initialize the optimizer.
### Instance Properties
- [var betas: (Float, Float)](./adamax/betas.md)
  The coefficients used for computing running averages of the gradient and its square
- [var eps: Float](./adamax/eps.md)
  The epsilon added to the denominator to improve numerical stability
- [var learningRate: Float](./adamax/learningrate.md)
  The learning rate
### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: TupleState) -> (MLXArray, TupleState)](./adamax/applysingle%28gradient,parameter,state%29.md)
- [func newState(parameter: MLXArray) -> TupleState](./adamax/newstate%28parameter%29.md)
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
- [class AdaDelta](./adadelta.md)
  The AdaDelta optimizer with a learning rate [1].
- [class Adafactor](./adafactor.md)
  The Adafactor optimizer.
- [class AdaGrad](./adagrad.md)
  The Adagrad optimizer [1].
- [class AdamW](./adamw.md)
  The AdamW optimizer [1].
- [class Adam](./adam.md)
  The Adam optimizer [1].
- [class Lion](./lion.md)
  The Lion optimizer [1].
- [class RMSprop](./rmsprop.md)
  The RMSprop optimizer [1].
- [class SGD](./sgd.md)
  Stochastic gradient descent optimizer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adamax)*