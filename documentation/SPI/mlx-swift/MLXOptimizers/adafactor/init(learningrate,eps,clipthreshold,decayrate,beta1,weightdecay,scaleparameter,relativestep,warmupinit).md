---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adafactor/init(learningrate:eps:clipthreshold:decayrate:beta1:weightdecay:scaleparameter:relativestep:warmupinit:)"
framework: "mlx-swift/MLXOptimizers"
---

# init(learningRate:eps:clipThreshold:decayRate:beta1:weightDecay:scaleParameter:relativeStep:warmupInit:)

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: init  
**Role**: Initializer

Initialize the optimizer.

## Declaration

```swift
init(learningRate: Float? = nil, eps: (Float, Float) = (1e-30, 1e-3), clipThreshold: Float = 1, decayRate: Float = -0.8, beta1: Float? = nil, weightDecay: Float = 0, scaleParameter: Bool = true, relativeStep: Bool = true, warmupInit: Bool = false)
```

## Parameters

- `learningRate`: The learning rate
- `eps`: The first term is added to the square of the gradients to improve numerical stability and the second term is used for parameter scaling if `parameterScale` is `true`
- `clipThreshold`: Clips the unscaled update
- `decayRate`: Ceofficient for the running average of the squared gradient
- `beta1`: If set then the first moment will be used
- `weightDecay`: The weight decay
- `scaleParameter`: If `true` the `learningRate` will be scaled by `max(eps.0, RMS(parameter))`
- `relativeStep`: If `true` the `learningRate` will be ignored and the relative step size will be computed
- `warmupInit`: If `true` the relative step size will be calculated by the current step


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/adafactor/init(learningrate:eps:clipthreshold:decayrate:beta1:weightdecay:scaleparameter:relativestep:warmupinit:))*