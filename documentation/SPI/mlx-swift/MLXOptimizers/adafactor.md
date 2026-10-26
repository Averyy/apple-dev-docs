---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adafactor"
framework: "mlx-swift/MLXOptimizers"
---

# Adafactor

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

The Adafactor optimizer.

## Declaration

```swift
class Adafactor
```

#### Overview

Our Adafactor implementation follows the original paper: `Adafactor: Adaptive Learning Rates with Sublinear Memory Cost [https://arxiv.org/abs/1804.04235](https://arxiv.org/abs/1804.04235)

##### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Structures
- [Adafactor.State](./adafactor/state.md)
### Initializers
- [init(learningRate: Float?, eps: (Float, Float), clipThreshold: Float, decayRate: Float, beta1: Float?, weightDecay: Float, scaleParameter: Bool, relativeStep: Bool, warmupInit: Bool)](./adafactor/init%28learningrate,eps,clipthreshold,decayrate,beta1,weightdecay,scaleparameter,relativestep,warmupinit%29.md)
  Initialize the optimizer.
### Instance Properties
- [var beta1: Float?](./adafactor/beta1.md)
  If set then the first moment will be used
- [var clipThreshold: Float](./adafactor/clipthreshold.md)
  Clips the unscaled update
- [var decayRate: Float](./adafactor/decayrate.md)
  Coefficient for the running average of the squared gradient
- [var eps: (Float, Float)](./adafactor/eps.md)
  The first term is added to the square of the gradients to improve numerical stability
- [var learningRate: Float?](./adafactor/learningrate.md)
  The learning rate
- [var relativeStep: Bool](./adafactor/relativestep.md)
  If `true` the `learningRate` will be ignored and the relative step size will be computed
- [var scaleParameter: Bool](./adafactor/scaleparameter.md)
  If `true` the `learningRate` will be scaled by `max(eps.0, RMS(parameter))`
- [var warmupInit: Bool](./adafactor/warmupinit.md)
  If `true` the relative step size will be calculated by the current step
- [var weightDecay: Float](./adafactor/weightdecay.md)
  The weight decay
### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: Adafactor.State) -> (MLXArray, Adafactor.State)](./adafactor/applysingle%28gradient,parameter,state%29.md)
- [func newState(parameter: MLXArray) -> Adafactor.State](./adafactor/newstate%28parameter%29.md)
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adafactor)*