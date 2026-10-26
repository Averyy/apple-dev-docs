---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers"
framework: "mlx-swift/MLXOptimizers"
---

# MLXOptimizers

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: module  
**Role**: Framework

Built-in optimizers.

#### Overview

MLX has a number of built in optimizers that are useful for training models.  Here is a simple training loop:

```
func loss(model: Model, x: MLXArray, y: MLXArray) -> MLXArray {
    // choose the loss function
    mseLoss(predictions: model(x), targets: y, reduction: .mean)
}

// function to compute the value (loss) and gradient
let lg = valueAndGrad(model: model, loss)

let optimizer = SGD(learningRate: 1e-1)

for _ in 0 ..< epochs {
    let (x, y) = ...

    // evaluate the training data
    let (loss, grads) = lg(model, x, y)

    // use the optimizer to update the model parameters
    optimizer.update(model: model, gradients: grads)

    eval(model, optimizer)
}
```

#### Other MLX Packages

- [MLX](../MLX/MLX.md)
- [MLXNN](../MLXNN/MLXNN.md)
- [Python mlx](https://ml-explore.github.io/mlx/build/html/index.html)

## Topics

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
- [class SGD](./sgd.md)
  Stochastic gradient descent optimizer.
### Base Classes and Protocols
- [protocol Optimizer](./optimizer.md)
  Public interface for all Optimizer types.
- [class OptimizerBase](./optimizerbase.md)
  The base class for all optimizers. It allows us to implement an optimizer on a per-parameter basis and apply it to a parameter tree.
- [class OptimizerBaseArrayState](./optimizerbasearraystate.md)
  Convenience subclass of OptimizerBase that provides `MLXArray` State.
### Classes
- [class MultiOptimizer](./multioptimizer.md)
  An optimizer that delegates to several sub-optimizers, routing each parameter to the first optimizer whose filter matches.
- [class Muon](./muon.md)
  The Muon (MomentUm Orthogonalized by Newton-schulz) optimizer.
### Structures
- [struct AdamState](./adamstate.md)
  State container for Adam-style optimizers that need first and second moments plus an update step for optional bias correction.
- [struct TupleState](./tuplestate.md)
  State container for [`OptimizerBase`](./optimizerbase.md) holding a tuple of `MLXArray`.
### Functions
- [func clipGradNorm(gradients: some Collection<MLXArray>, maxNorm: Float) -> ([MLXArray], MLXArray)](./clipgradnorm%28gradients,maxnorm%29-878zr.md)
  Clips the global norm of the gradients.
- [func clipGradNorm(gradients: ModuleParameters, maxNorm: Float) -> (ModuleParameters, MLXArray)](./clipgradnorm%28gradients,maxnorm%29-94rdm.md)
  Clips the global norm of the gradients.
- [func cosineDecay(Float, decaySteps: Int, end: Float) -> (Int) -> Float](./cosinedecay%28_,decaysteps,end%29.md)
  Make a cosine-decay schedule. The value is constant (`end`) for steps beyond `decaySteps`.
- [func exponentialDecay(Float, decayRate: Float) -> (Int) -> Float](./exponentialdecay%28_,decayrate%29.md)
  Make an exponential-decay schedule: `initial * decayRate ** step`.
- [func joinSchedules([(Int) -> Float], boundaries: [Int]) -> (Int) -> Float](./joinschedules%28_,boundaries%29.md)
  Join multiple schedules into one. Schedule `i + 1` receives a step count indicating the number of steps since the `i`-th boundary.
- [func linearSchedule(Float, end: Float, steps: Int) -> (Int) -> Float](./linearschedule%28_,end,steps%29.md)
  Make a linear schedule from `initial` to `end` over `steps`. The value is `end` for any steps beyond `steps`.
- [func stepDecay(Float, decayRate: Float, stepSize: Int) -> (Int) -> Float](./stepdecay%28_,decayrate,stepsize%29.md)
  Make a step-decay schedule: `initial * decayRate ** (step / stepSize)`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers)*