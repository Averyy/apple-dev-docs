---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/lion"
framework: "mlx-swift/MLXOptimizers"
---

# Lion

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

The Lion optimizer [1].

## Declaration

```swift
class Lion
```

## Overview

Since updates are computed through the sign operation, they tend to have larger norm than for other optimizers such as SGD and Adam. We recommend a learning rate that is 3-10x smaller than AdamW and a weight decay 3-10x larger than AdamW to maintain the strength `(lr * wd)`. Our Lion implementation follows the original paper. In detail,

[1]: Chen, X. Symbolic Discovery of Optimization Algorithms. arXiv preprint arXiv:2302.06675.

### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Initializers
- [init(learningRate: Float, betas: (Float, Float), weightDecay: Float)](./lion/init%28learningrate,betas,weightdecay%29.md)
  Initialize the optimizer.
### Instance Properties
- [var betas: (Float, Float)](./lion/betas.md)
  The coefficients used for computing the gradient momentum and update direction
- [var learningRate: Float](./lion/learningrate.md)
  The learning rate
- [var weightDecay: Float](./lion/weightdecay.md)
  The weight decay
### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: MLXArray) -> (MLXArray, MLXArray)](./lion/applysingle%28gradient,parameter,state%29.md)

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
- [class RMSprop](./rmsprop.md)
  The RMSprop optimizer [1].
- [class SGD](./sgd.md)
  Stochastic gradient descent optimizer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/lion)*