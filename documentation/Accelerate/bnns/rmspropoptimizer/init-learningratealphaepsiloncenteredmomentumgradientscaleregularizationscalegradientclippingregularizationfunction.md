# init(learningRate:alpha:epsilon:centered:momentum:gradientScale:regularizationScale:gradientClipping:regularizationFunction:)

**Framework**: Accelerate  
**Kind**: init

Returns a new RMSProp optimizer object with gradient clipped by value or clipped by norm.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
init(learningRate: Float = 1e-2, alpha: Float = 0.99, epsilon: Float = 1e-8, centered: Bool, momentum: Float = 0, gradientScale: Float, regularizationScale: Float, gradientClipping: BNNS.GradientClipping, regularizationFunction: BNNSOptimizerRegularizationFunction)
```

## Parameters

- `learningRate`: A value that specifies the learning rate.
- `alpha`: A constant that specifies smoothing, in the range   to  .
- `epsilon`: A term that the optimizer adds to the denominator.
- `centered`: A Boolean value that specifies whether to use the centered variant.
- `momentum`: The rate of momentum decay.
- `gradientScale`: A value that specifies the gradient scaling factor.
- `regularizationScale`: A value that specifies the regularization scaling factor.
- `gradientClipping`: The gradient clipping function and bounds.
- `regularizationFunction`: The variable that specifies the regularization function.

## See Also

- [init(learningRate: Float, alpha: Float, epsilon: Float, centered: Bool, momentum: Float, gradientScale: Float, regularizationScale: Float, clipsGradientsTo: ClosedRange<Float>?, regularizationFunction: BNNSOptimizerRegularizationFunction)](bnns/rmspropoptimizer/init(learningrate:alpha:epsilon:centered:momentum:gradientscale:regularizationscale:clipsgradientsto:regularizationfunction:).md)
  Returns a new RMSProp optimizer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/rmspropoptimizer/init(learningrate:alpha:epsilon:centered:momentum:gradientscale:regularizationscale:gradientclipping:regularizationfunction:))*