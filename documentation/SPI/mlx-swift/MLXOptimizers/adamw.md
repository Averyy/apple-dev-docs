---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adamw"
framework: "mlx-swift/MLXOptimizers"
---

# AdamW

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

The AdamW optimizer [1].

## Declaration

```swift
class AdamW
```

#### Overview

By default AdamW omits bias correction in the first and second moments, to match the longstanding MLX Swift behavior. Set `biasCorrection` to `true` to apply it. We update the weights with a `weightDecay` lambda value:

[1]: Loshchilov, I. and Hutter, F., 2019. Decoupled weight decay regularization. ICLR 2019.

##### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Initializers
- [init(learningRate: Float, betas: (Float, Float), eps: Float, weightDecay: Float, biasCorrection: Bool)](./adamw/init%28learningrate,betas,eps,weightdecay,biascorrection%29.md)
  Initialize the optimizer.
### Instance Properties
- [var weightDecay: Float](./adamw/weightdecay.md)
  The weight decay
### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: AdamState) -> (MLXArray, AdamState)](./adamw/applysingle%28gradient,parameter,state%29.md)

## Relationships

### Inherits From
- [Adam](./adam.md)
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adamw)*