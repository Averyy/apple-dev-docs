---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/muon"
framework: "mlx-swift/MLXOptimizers"
---

# Muon

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: class  
**Role**: Class

The Muon (MomentUm Orthogonalized by Newton-schulz) optimizer.

## Declaration

```swift
class Muon
```

#### Overview

Follows the original implementation: [Muon: An optimizer for hidden layers in neural networks](https://kellerjordan.github.io/posts/muon/).

> **Note**: Muon may be sub-optimal for the embedding layer, the final fully connected layer, or any 0D/1D parameters; optimize those with a different method (e.g. [`AdamW`](./adamw.md)). For parameters with more than 2 dimensions (e.g. 4D convolution filters) the trailing dimensions are flattened.

##### See Also

- [MLXOptimizers](./MLXOptimizers.md)

## Topics

### Initializers
- [init(learningRate: Float, momentum: Float, weightDecay: Float, nesterov: Bool, nsSteps: Int)](./muon/init%28learningrate,momentum,weightdecay,nesterov,nssteps%29.md)
  Initialize the optimizer.
### Instance Properties
- [var learningRate: Float](./muon/learningrate.md)
  The learning rate
- [var momentum: Float](./muon/momentum.md)
  The momentum strength
- [var nesterov: Bool](./muon/nesterov.md)
  Enables Nesterov momentum (recommended)
- [var nsSteps: Int](./muon/nssteps.md)
  Number of Newton-Schulz iteration steps for orthogonalization
- [var weightDecay: Float](./muon/weightdecay.md)
  The weight decay (L2 penalty)
### Instance Methods
- [func applySingle(gradient: MLXArray, parameter: MLXArray, state: MLXArray) -> (MLXArray, MLXArray)](./muon/applysingle%28gradient,parameter,state%29.md)

## Relationships

### Inherits From
- [OptimizerBaseArrayState](./optimizerbasearraystate.md)
### Conforms To
- MLX.Evaluatable
- MLX.Updatable
- [Optimizer](./optimizer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/muon)*