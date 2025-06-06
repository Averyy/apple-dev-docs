# init(learningRate:gradientRescale:regularizationType:regularizationScale:)

**Framework**: ML Compute  
**Kind**: init

Creates an optimizer descriptor with the learning rate, gradient rescale, regularization type, and regulation scale that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(learningRate: Float, gradientRescale: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)
```

## Parameters

- `learningRate`: The learning rate.
- `gradientRescale`: The gradient rescale value.
- `regularizationType`: The regularization type.
- `regularizationScale`: The regularization scale.

## See Also

- [convenience init(learningRate: Float, gradientRescale: Float, appliesGradientClipping: Bool, gradientClipMax: Float, gradientClipMin: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](mlcoptimizerdescriptor/init(learningrate:gradientrescale:appliesgradientclipping:gradientclipmax:gradientclipmin:regularizationtype:regularizationscale:).md)
  Creates a descriptor with the learning rate, gradient rescale, clipping option and values, and regularization type and scale that you specify.
- [convenience init(learningRate: Float, gradientRescale: Float, appliesGradientClipping: Bool, gradientClippingType: MLCGradientClippingType, gradientClipMax: Float, gradientClipMin: Float, maximumClippingNorm: Float, customGlobalNorm: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](mlcoptimizerdescriptor/init(learningrate:gradientrescale:appliesgradientclipping:gradientclippingtype:gradientclipmax:gradientclipmin:maximumclippingnorm:customglobalnorm:regularizationtype:regularizationscale:).md)
  Creates a descriptor with the learning rate, gradient rescale, clipping option and values, and regularization type and scale that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizerdescriptor/init(learningrate:gradientrescale:regularizationtype:regularizationscale:))*