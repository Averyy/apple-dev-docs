---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/sgd/init(learningrate:momentum:weightdecay:dampening:nesterov:)"
framework: "mlx-swift/MLXOptimizers"
---

# init(learningRate:momentum:weightDecay:dampening:nesterov:)

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: init  
**Role**: Initializer

Initialize the SGD optimizer.

## Declaration

```swift
init(learningRate: Float, momentum: Float = 0, weightDecay: Float = 0, dampening: Float = 0, nesterov: Bool = false)
```

## Discussion

`learningRate` is the only required parameter and `0.1` might be a reasonable number to try.

## Parameters

- `learningRate`: The learning rate
- `momentum`: Momentum strength
- `weightDecay`: Weight decay (L2 penalty)
- `dampening`: Dampening for momentum
- `nesterov`: Enables Nesterov momentum


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/sgd/init(learningrate:momentum:weightdecay:dampening:nesterov:))*