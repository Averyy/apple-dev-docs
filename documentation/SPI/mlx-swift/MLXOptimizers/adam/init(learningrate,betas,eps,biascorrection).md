---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adam/init(learningrate:betas:eps:biascorrection:)"
framework: "mlx-swift/MLXOptimizers"
---

# init(learningRate:betas:eps:biasCorrection:)

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: init  
**Role**: Initializer

Initialize the optimizer.

## Declaration

```swift
init(learningRate: Float, betas: (Float, Float) = (0.9, 0.999), eps: Float = 1e-8, biasCorrection: Bool = false)
```

## Parameters

- `learningRate`: The learning rate
- `betas`: Coefficients used for computing running averages of the gradient and its square
- `eps`: The epsilon added to the denominator to improve numerical stability
- `biasCorrection`: If `true`, apply bias correction to the first and second moments


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adam/init(learningrate:betas:eps:biascorrection:))*