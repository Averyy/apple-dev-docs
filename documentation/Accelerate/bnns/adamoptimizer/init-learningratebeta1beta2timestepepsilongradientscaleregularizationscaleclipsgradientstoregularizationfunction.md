# init(learningRate:beta1:beta2:timeStep:epsilon:gradientScale:regularizationScale:clipsGradientsTo:regularizationFunction:)

**Framework**: Accelerate  
**Kind**: init

Returns a new Adam optimizer object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
init(learningRate: Float, beta1: Float, beta2: Float, timeStep: Float, epsilon: Float, gradientScale: Float, regularizationScale: Float, clipsGradientsTo gradientBounds: ClosedRange<Float>? = nil, regularizationFunction: BNNSOptimizerRegularizationFunction)
```

## Parameters

- `learningRate`: A value that specifies the learning rate.
- `beta1`: A value that specifies the first-moment constant, in the range `0` to `1`.
- `beta2`: A value that specifies the second-moment constant, in the range `0` to `1`.
- `timeStep`: A value that’s at least `1` and represents the optimizer’s current time.
- `epsilon`: The epsilon value you use to improve numerical stability.
- `gradientScale`: A value that specifies the gradient scaling factor.
- `regularizationScale`: A value that specifies the regularization scaling factor.
- `gradientBounds`: The values for the minimum and maximum gradients.
- `regularizationFunction`: The variable that specifies the regularization function.

## See Also

- [init(learningRate: Float, beta1: Float, beta2: Float, timeStep: Float, epsilon: Float, gradientScale: Float, regularizationScale: Float, gradientClipping: BNNS.GradientClipping, regularizationFunction: BNNSOptimizerRegularizationFunction, usesAMSGrad: Bool)](bnns/adamoptimizer/init(learningrate:beta1:beta2:timestep:epsilon:gradientscale:regularizationscale:gradientclipping:regularizationfunction:usesamsgrad:).md)
  Returns a new Adam optimizer object with gradient clipped by value or clipped by norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/adamoptimizer/init(learningrate:beta1:beta2:timestep:epsilon:gradientscale:regularizationscale:clipsgradientsto:regularizationfunction:))*