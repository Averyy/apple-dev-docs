# init(learningRate:gradientRescale:appliesGradientClipping:gradientClippingType:gradientClipMax:gradientClipMin:maximumClippingNorm:customGlobalNorm:regularizationType:regularizationScale:)

**Framework**: ML Compute  
**Kind**: init

Creates a descriptor with the learning rate, gradient rescale, clipping option and values, and regularization type and scale that you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
convenience init(learningRate: Float, gradientRescale: Float, appliesGradientClipping: Bool, gradientClippingType: MLCGradientClippingType, gradientClipMax: Float, gradientClipMin: Float, maximumClippingNorm: Float, customGlobalNorm: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)
```

## Parameters

- `learningRate`: The learning rate.
- `gradientRescale`: The gradient rescale value.
- `appliesGradientClipping`: A Boolean value that indicates whether you apply gradient clipping.
- `gradientClippingType`: The type of clipping the system applies to gradients.
- `gradientClipMax`: The maximum gradient value before the optimizer rescales the gradient, if you enable gradient clipping.
- `gradientClipMin`: The minimum gradient value before the optimizer rescales the gradient, if you enable gradient clipping.
- `maximumClippingNorm`: The maximum norm to use with gradient clipping.
- `customGlobalNorm`: If nonzero, the value the system uses instead of calculating it.
- `regularizationType`: The regularization type.
- `regularizationScale`: The regularization scale.

## See Also

- [convenience init(learningRate: Float, gradientRescale: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](mlcoptimizerdescriptor/init(learningrate:gradientrescale:regularizationtype:regularizationscale:).md)
  Creates an optimizer descriptor with the learning rate, gradient rescale, regularization type, and regulation scale that you specify.
- [convenience init(learningRate: Float, gradientRescale: Float, appliesGradientClipping: Bool, gradientClipMax: Float, gradientClipMin: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](mlcoptimizerdescriptor/init(learningrate:gradientrescale:appliesgradientclipping:gradientclipmax:gradientclipmin:regularizationtype:regularizationscale:).md)
  Creates a descriptor with the learning rate, gradient rescale, clipping option and values, and regularization type and scale that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizerdescriptor/init(learningrate:gradientrescale:appliesgradientclipping:gradientclippingtype:gradientclipmax:gradientclipmin:maximumclippingnorm:customglobalnorm:regularizationtype:regularizationscale:))*