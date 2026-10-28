---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adagrad"
framework: "mlx-swift/MLXOptimizers"
---

# AdaGrad

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

The Adagrad optimizer [1].

## Declaration

```swift
class AdaGrad
```

## Overview

Our Adagrad implementation follows the original paper. In detail,

[1]: Duchi, J., Hazan, E. and Singer, Y., 2011. Adaptive subgradient methods for online learning and stochastic optimization. JMLR 2011.

### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Initializers
- [init(learningRate: Float, eps: Float)](./adagrad/init%28learningrate,eps%29.md)
  Initialize the optimizer.
### Instance Properties
- [var eps: Float](./adagrad/eps.md)
  The epsilon added to the denominator to improve numerical stability
- [var learningRate: Float](./adagrad/learningrate.md)
  The learning rate
### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: MLXArray) -> (MLXArray, MLXArray)](./adagrad/applysingle%28gradient,parameter,state%29.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adagrad)*