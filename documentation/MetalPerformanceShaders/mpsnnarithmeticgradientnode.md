# MPSNNArithmeticGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: class

A representation of the base class for gradient arithmetic operators.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNArithmeticGradientNode
```

## Topics

### Initializers
- [init(gradientImages: [MPSNNImageNode], forwardFilter: MPSNNFilterNode, isSecondarySourceFilter: Bool)](mpsnnarithmeticgradientnode/init(gradientimages:forwardfilter:issecondarysourcefilter:).md)
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNBinaryGradientStateNode, isSecondarySourceFilter: Bool)](mpsnnarithmeticgradientnode/init(sourcegradient:sourceimage:gradientstate:issecondarysourcefilter:).md)
### Instance Properties
- [var bias: Float](mpsnnarithmeticgradientnode/bias.md)
- [var isSecondarySourceFilter: Bool](mpsnnarithmeticgradientnode/issecondarysourcefilter.md)
- [var maximumValue: Float](mpsnnarithmeticgradientnode/maximumvalue.md)
- [var minimumValue: Float](mpsnnarithmeticgradientnode/minimumvalue.md)
- [var primaryScale: Float](mpsnnarithmeticgradientnode/primaryscale.md)
- [var secondaryScale: Float](mpsnnarithmeticgradientnode/secondaryscale.md)
- [var secondaryStrideInFeatureChannels: Int](mpsnnarithmeticgradientnode/secondarystrideinfeaturechannels.md)
- [var secondaryStrideInPixelsX: Int](mpsnnarithmeticgradientnode/secondarystrideinpixelsx.md)
- [var secondaryStrideInPixelsY: Int](mpsnnarithmeticgradientnode/secondarystrideinpixelsy.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)
### Inherited By
- [MPSNNAdditionGradientNode](mpsnnadditiongradientnode.md)
- [MPSNNMultiplicationGradientNode](mpsnnmultiplicationgradientnode.md)
- [MPSNNSubtractionGradientNode](mpsnnsubtractiongradientnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSNNAdditionNode](mpsnnadditionnode.md)
  A representation of an addition operator.
- [class MPSNNAdditionGradientNode](mpsnnadditiongradientnode.md)
  A representation of a gradient addition operator.
- [class MPSNNSubtractionNode](mpsnnsubtractionnode.md)
  A representation of an subtraction operator.
- [class MPSNNSubtractionGradientNode](mpsnnsubtractiongradientnode.md)
  A representation of a gradient subtraction operator.
- [class MPSNNMultiplicationNode](mpsnnmultiplicationnode.md)
  A representation of a multiplication operator.
- [class MPSNNMultiplicationGradientNode](mpsnnmultiplicationgradientnode.md)
  A representation of a gradient multiplication operator.
- [class MPSNNDivisionNode](mpsnndivisionnode.md)
  A representation of a division operator.
- [class MPSNNBinaryArithmeticNode](mpsnnbinaryarithmeticnode.md)
  Virtual base class for basic arithmetic nodes.
- [class MPSNNArithmeticGradientStateNode](mpsnnarithmeticgradientstatenode.md)
  A representation of the clamp mask used by gradient arithmetic operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnarithmeticgradientnode)*