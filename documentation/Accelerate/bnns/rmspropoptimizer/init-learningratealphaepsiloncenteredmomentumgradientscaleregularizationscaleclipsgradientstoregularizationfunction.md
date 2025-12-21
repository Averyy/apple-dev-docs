# init(learningRate:alpha:epsilon:centered:momentum:gradientScale:regularizationScale:clipsGradientsTo:regularizationFunction:)

**Framework**: Accelerate  
**Kind**: init

Returns a new RMSProp optimizer object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
init(learningRate: Float, alpha: Float, epsilon: Float, centered: Bool, momentum: Float, gradientScale: Float, regularizationScale: Float, clipsGradientsTo gradientBounds: ClosedRange<Float>? = nil, regularizationFunction: BNNSOptimizerRegularizationFunction)
```

## Parameters

- `learningRate`: A value that specifies the learning rate.
- `alpha`: A constant that specifies smoothing, in the range   to  .
- `epsilon`: A term that the optimizer adds to the denominator.
- `centered`: A Boolean value that specifies whether to use the centered variant.
- `momentum`: The rate of momentum decay.
- `gradientScale`: A value that specifies the gradient scaling factor.
- `regularizationScale`: A value that specifies the regularization scaling factor.
- `gradientBounds`: The values for the minimum and maximum gradients.
- `regularizationFunction`: The variable that specifies the regularization function.

## See Also

- [init(learningRate: Float, alpha: Float, epsilon: Float, centered: Bool, momentum: Float, gradientScale: Float, regularizationScale: Float, gradientClipping: BNNS.GradientClipping, regularizationFunction: BNNSOptimizerRegularizationFunction)](bnns/rmspropoptimizer/init(learningrate:alpha:epsilon:centered:momentum:gradientscale:regularizationscale:gradientclipping:regularizationfunction:).md)
  Returns a new RMSProp optimizer object with gradient clipped by value or clipped by norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/rmspropoptimizer/init(learningrate:alpha:epsilon:centered:momentum:gradientscale:regularizationscale:clipsgradientsto:regularizationfunction:))*