# MLCOptimizerDescriptor

**Framework**: ML Compute  
**Kind**: class

A configuration object you use to create an optimizer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCOptimizerDescriptor
```

## Topics

### Creating an Optimizer Descriptor
- [convenience init(learningRate: Float, gradientRescale: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](mlcoptimizerdescriptor/init(learningrate:gradientrescale:regularizationtype:regularizationscale:).md)
  Creates an optimizer descriptor with the learning rate, gradient rescale, regularization type, and regulation scale that you specify.
- [convenience init(learningRate: Float, gradientRescale: Float, appliesGradientClipping: Bool, gradientClipMax: Float, gradientClipMin: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](mlcoptimizerdescriptor/init(learningrate:gradientrescale:appliesgradientclipping:gradientclipmax:gradientclipmin:regularizationtype:regularizationscale:).md)
  Creates a descriptor with the learning rate, gradient rescale, clipping option and values, and regularization type and scale that you specify.
- [convenience init(learningRate: Float, gradientRescale: Float, appliesGradientClipping: Bool, gradientClippingType: MLCGradientClippingType, gradientClipMax: Float, gradientClipMin: Float, maximumClippingNorm: Float, customGlobalNorm: Float, regularizationType: MLCRegularizationType, regularizationScale: Float)](mlcoptimizerdescriptor/init(learningrate:gradientrescale:appliesgradientclipping:gradientclippingtype:gradientclipmax:gradientclipmin:maximumclippingnorm:customglobalnorm:regularizationtype:regularizationscale:).md)
  Creates a descriptor with the learning rate, gradient rescale, clipping option and values, and regularization type and scale that you specify.
### Inspecting an Optimizer Descriptor
- [var learningRate: Float](mlcoptimizerdescriptor/learningrate.md)
  The learning rate.
- [var gradientRescale: Float](mlcoptimizerdescriptor/gradientrescale.md)
  The rescale value the optimizer applies to gradients during updates.
- [var appliesGradientClipping: Bool](mlcoptimizerdescriptor/appliesgradientclipping.md)
  A Boolean that indicates whether you apply gradient clipping.
- [var gradientClipMax: Float](mlcoptimizerdescriptor/gradientclipmax.md)
  The maximum gradient value before the optimizer rescales the gradient, if you enabled gradient clipping.
- [var gradientClipMin: Float](mlcoptimizerdescriptor/gradientclipmin.md)
  The minimum gradient value before the optimizer rescales the gradient, if you enabled gradient clipping.
- [var regularizationScale: Float](mlcoptimizerdescriptor/regularizationscale.md)
  The regularization scale.
- [var regularizationType: MLCRegularizationType](mlcoptimizerdescriptor/regularizationtype.md)
  The regularization type.
- [var gradientClippingType: MLCGradientClippingType](mlcoptimizerdescriptor/gradientclippingtype.md)
  The type of clipping the system applies to the gradient.
- [enum MLCGradientClippingType](mlcgradientclippingtype.md)
  A clipping type the system applies to a gradient.
- [var maximumClippingNorm: Float](mlcoptimizerdescriptor/maximumclippingnorm.md)
  The maximum clipping value.
- [var customGlobalNorm: Float](mlcoptimizerdescriptor/customglobalnorm.md)
  A custom norm the system uses in place of the global norm.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [enum MLCRegularizationType](mlcregularizationtype.md)
  A regularization function to use with an optimizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcoptimizerdescriptor)*