# init(learningRate:gradientRescale:regularizationType:regularizationScale:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an optimizer descriptor with the learning rate, gradient rescale, regularization type, and regulation scale that you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(learningRate: Float, gradientRescale: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)
```

```objc
+ (instancetype) descriptorWithLearningRate:(float) learningRate gradientRescale:(float) gradientRescale regularizationType:(MLCRegularizationType) regularizationType regularizationScale:(float) regularizationScale;
```

## Parameters

- `learningRate`: The learning rate.
- `gradientRescale`: The gradient rescale value.
- `regularizationType`: The regularization type.
- `regularizationScale`: The regularization scale.

## See Also

### Creating an Optimizer Descriptor
- [convenience init(learningRate: Float, gradientRescale: Float, appliesGradientClipping: Bool, gradientClipMax: Float, gradientClipMin: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](./init%28learningrate,gradientrescale,appliesgradientclipping,gradientclipmax,gradientclipmin,regularizationtype,regularizationscale%29.md)
  Creates a descriptor with the learning rate, gradient rescale, clipping option and values, and regularization type and scale that you specify.
- [convenience init(learningRate: Float, gradientRescale: Float, appliesGradientClipping: Bool, gradientClippingType: MLCGradientClippingType, gradientClipMax: Float, gradientClipMin: Float, maximumClippingNorm: Float, customGlobalNorm: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](./init%28learningrate,gradientrescale,appliesgradientclipping,gradientclippingtype,gradientclipmax,gradientclipmin,maximumclippingnorm,customglobalnorm,regularizationtype,regularizationscale%29.md)
  Creates a descriptor with the learning rate, gradient rescale, clipping option and values, and regularization type and scale that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizerdescriptor/init(learningrate:gradientrescale:regularizationtype:regularizationscale:))*