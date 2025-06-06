# init(learningRate:beta1:beta2:timeStep:epsilon:gradientScale:weightDecay:gradientClipping:usesAMSGrad:)

**Framework**: Accelerate  
**Kind**: init

Returns a new AdamW optimizer object with gradient clipped by value or clipped by norm.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
init(learningRate: Float = 0.001, beta1: Float = 0.9, beta2: Float = 0.999, timeStep: Float = 1, epsilon: Float = 1e-8, gradientScale: Float, weightDecay: Float = 1e-2, gradientClipping: BNNS.GradientClipping, usesAMSGrad: Bool = false)
```

## Parameters

- `learningRate`: A value that specifies the learning rate.
- `beta1`: A value that specifies the first-moment constant, in the range   to  .
- `beta2`: A value that specifies the second-moment constant, in the range   to  .
- `timeStep`: A value that’s at least   and represents the optimizer’s current time.
- `epsilon`: The epsilon value you use to improve numerical stability.
- `gradientScale`: A value that specifies the gradient scaling factor.
- `weightDecay`: The weight decay coefficient.
- `gradientClipping`: The gradient clipping function and bounds.
- `usesAMSGrad`: A Boolean value that specifies whether the optimizer should use the AMSGrad variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/adamwoptimizer/init(learningrate:beta1:beta2:timestep:epsilon:gradientscale:weightdecay:gradientclipping:usesamsgrad:))*