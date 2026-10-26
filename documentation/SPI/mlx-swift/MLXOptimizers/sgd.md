---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/sgd"
framework: "mlx-swift/MLXOptimizers"
---

# SGD

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

Stochastic gradient descent optimizer.

## Declaration

```swift
class SGD
```

##### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Initializers
- [init(learningRate: Float, momentum: Float, weightDecay: Float, dampening: Float, nesterov: Bool)](./sgd/init%28learningrate,momentum,weightdecay,dampening,nesterov%29.md)
  Initialize the SGD optimizer.
### Instance Properties
- [var dampening: Float](./sgd/dampening.md)
  Dampening for momentum
- [var learningRate: Float](./sgd/learningrate.md)
  The learning rate
- [var momentum: Float](./sgd/momentum.md)
  Momentum strength
- [var nesterov: Bool](./sgd/nesterov.md)
  Enables Nesterov momentum
- [var weightDecay: Float](./sgd/weightdecay.md)
  Weight decay (L2 penalty)
### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: MLXArray) -> (MLXArray, MLXArray)](./sgd/applysingle%28gradient,parameter,state%29.md)
- [func newState(parameter: MLXArray) -> MLXArray](./sgd/newstate%28parameter%29.md)
  Subclasses must implement this to create a new `State` when needed.  This is called for each parameter in the model.

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
- [class RMSprop](./rmsprop.md)
  The RMSprop optimizer [1].


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/sgd)*