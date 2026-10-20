# init(learningRate:gradientRescale:appliesGradientClipping:gradientClippingType:gradientClipMax:gradientClipMin:maximumClippingNorm:customGlobalNorm:regularizationType:regularizationScale:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a descriptor with the learning rate, gradient rescale, clipping option and values, and regularization type and scale that you specify.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(learningRate: Float, gradientRescale: Float, appliesGradientClipping: Bool, gradientClippingType: MLCGradientClippingType, gradientClipMax: Float, gradientClipMin: Float, maximumClippingNorm: Float, customGlobalNorm: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)
```

```objc
+ (instancetype) descriptorWithLearningRate:(float) learningRate gradientRescale:(float) gradientRescale appliesGradientClipping:(BOOL) appliesGradientClipping gradientClippingType:(MLCGradientClippingType) gradientClippingType gradientClipMax:(float) gradientClipMax gradientClipMin:(float) gradientClipMin maximumClippingNorm:(float) maximumClippingNorm customGlobalNorm:(float) customGlobalNorm regularizationType:(MLCRegularizationType) regularizationType regularizationScale:(float) regularizationScale;
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

### Creating an Optimizer Descriptor
- [convenience init(learningRate: Float, gradientRescale: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](./init%28learningrate,gradientrescale,regularizationtype,regularizationscale%29.md)
  Creates an optimizer descriptor with the learning rate, gradient rescale, regularization type, and regulation scale that you specify.
- [convenience init(learningRate: Float, gradientRescale: Float, appliesGradientClipping: Bool, gradientClipMax: Float, gradientClipMin: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](./init%28learningrate,gradientrescale,appliesgradientclipping,gradientclipmax,gradientclipmin,regularizationtype,regularizationscale%29.md)
  Creates a descriptor with the learning rate, gradient rescale, clipping option and values, and regularization type and scale that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizerdescriptor/init(learningrate:gradientrescale:appliesgradientclipping:gradientclippingtype:gradientclipmax:gradientclipmin:maximumclippingnorm:customglobalnorm:regularizationtype:regularizationscale:))*