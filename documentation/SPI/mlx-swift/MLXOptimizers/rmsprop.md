---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/rmsprop"
framework: "mlx-swift/MLXOptimizers"
---

# RMSprop

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

The RMSprop optimizer [1].

## Declaration

```swift
class RMSprop
```

## Overview

[1]: Tieleman, T. and Hinton, G. 2012. Lecture 6.5-rmsprop, coursera: Neural networks for machine learning

### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Initializers
- [init(learningRate: Float, alpha: Float, eps: Float)](./rmsprop/init%28learningrate,alpha,eps%29.md)
  Initialize the optimizer.
### Instance Properties
- [var alpha: Float](./rmsprop/alpha.md)
  The smoothing constant
- [var eps: Float](./rmsprop/eps.md)
  The epsilon added to the denominator to improve numerical stability
- [var learningRate: Float](./rmsprop/learningrate.md)
  The learning rate
### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: MLXArray) -> (MLXArray, MLXArray)](./rmsprop/applysingle%28gradient,parameter,state%29.md)

## Relationships

### Inherits From
- [OptimizerBaseArrayState](./optimizerbasearraystate.md)
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
- [class Adamax](./adamax.md)
  The Adamax optimizer, a variant of Adam based on the infinity norm [1].
- [class Lion](./lion.md)
  The Lion optimizer [1].
- [class SGD](./sgd.md)
  Stochastic gradient descent optimizer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/rmsprop)*