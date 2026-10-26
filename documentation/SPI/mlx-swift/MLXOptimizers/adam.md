---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adam"
framework: "mlx-swift/MLXOptimizers"
---

# Adam

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

The Adam optimizer [1].

## Declaration

```swift
class Adam
```

#### Overview

By default our Adam implementation omits bias correction in the first and second moment estimates. Set `biasCorrection` to `true` to apply it. In detail,

[1]: Kingma, D.P. and Ba, J., 2015. Adam: A method for stochastic optimization. ICLR 2015.

##### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Initializers
- [init(learningRate: Float, betas: (Float, Float), eps: Float, biasCorrection: Bool)](./adam/init%28learningrate,betas,eps,biascorrection%29.md)
  Initialize the optimizer.
### Instance Properties
- [var betas: (Float, Float)](./adam/betas.md)
  The coefficients used for computing running averages of the gradient and its square
- [var biasCorrection: Bool](./adam/biascorrection.md)
  If `true`, apply bias correction to the first and second moments
- [var eps: Float](./adam/eps.md)
  The epsilon added to the denominator to improve numerical stability
- [var learningRate: Float](./adam/learningrate.md)
  The learning rate
### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: AdamState) -> (MLXArray, AdamState)](./adam/applysingle%28gradient,parameter,state%29.md)
- [func newState(parameter: MLXArray) -> AdamState](./adam/newstate%28parameter%29.md)
  Subclasses must implement this to create a new `State` when needed.  This is called for each parameter in the model.

## Relationships

### Inherits From
- [OptimizerBase](./optimizerbase.md)
### Inherited By
- [AdamW](./adamw.md)
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
- [class Adamax](./adamax.md)
  The Adamax optimizer, a variant of Adam based on the infinity norm [1].
- [class Lion](./lion.md)
  The Lion optimizer [1].
- [class RMSprop](./rmsprop.md)
  The RMSprop optimizer [1].
- [class SGD](./sgd.md)
  Stochastic gradient descent optimizer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adam)*