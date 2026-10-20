# MPSNNBinaryArithmeticNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

Virtual base class for basic arithmetic nodes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNBinaryArithmeticNode
```

```objc
@interface MPSNNBinaryArithmeticNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(leftSource: MPSNNImageNode, rightSource: MPSNNImageNode)](./mpsnnbinaryarithmeticnode/init%28leftsource,rightsource%29.md)
- [init(sources: [MPSNNImageNode])](./mpsnnbinaryarithmeticnode/init%28sources%29.md)
### Instance Properties
- [var bias: Float](./mpsnnbinaryarithmeticnode/bias.md)
- [var maximumValue: Float](./mpsnnbinaryarithmeticnode/maximumvalue.md)
- [var minimumValue: Float](./mpsnnbinaryarithmeticnode/minimumvalue.md)
- [var primaryScale: Float](./mpsnnbinaryarithmeticnode/primaryscale.md)
- [var primaryStrideInFeatureChannels: Int](./mpsnnbinaryarithmeticnode/primarystrideinfeaturechannels.md)
- [var primaryStrideInPixelsX: Int](./mpsnnbinaryarithmeticnode/primarystrideinpixelsx.md)
- [var primaryStrideInPixelsY: Int](./mpsnnbinaryarithmeticnode/primarystrideinpixelsy.md)
- [var secondaryScale: Float](./mpsnnbinaryarithmeticnode/secondaryscale.md)
- [var secondaryStrideInFeatureChannels: Int](./mpsnnbinaryarithmeticnode/secondarystrideinfeaturechannels.md)
- [var secondaryStrideInPixelsX: Int](./mpsnnbinaryarithmeticnode/secondarystrideinpixelsx.md)
- [var secondaryStrideInPixelsY: Int](./mpsnnbinaryarithmeticnode/secondarystrideinpixelsy.md)
### Instance Methods
- [func gradientClass() -> AnyClass](./mpsnnbinaryarithmeticnode/gradientclass%28%29.md)
- [func gradientFilters(withSources: [MPSNNImageNode]) -> [MPSNNGradientFilterNode]](./mpsnnbinaryarithmeticnode/gradientfilters%28withsources%29.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](./mpsnnfilternode.md)
### Inherited By
- [MPSNNAdditionNode](./mpsnnadditionnode.md)
- [MPSNNComparisonNode](./mpsnncomparisonnode.md)
- [MPSNNDivisionNode](./mpsnndivisionnode.md)
- [MPSNNMultiplicationNode](./mpsnnmultiplicationnode.md)
- [MPSNNSubtractionNode](./mpsnnsubtractionnode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Arithmetic Layer Nodes
- [class MPSNNAdditionNode](./mpsnnadditionnode.md)
  A representation of an addition operator.
- [class MPSNNAdditionGradientNode](./mpsnnadditiongradientnode.md)
  A representation of a gradient addition operator.
- [class MPSNNSubtractionNode](./mpsnnsubtractionnode.md)
  A representation of an subtraction operator.
- [class MPSNNSubtractionGradientNode](./mpsnnsubtractiongradientnode.md)
  A representation of a gradient subtraction operator.
- [class MPSNNMultiplicationNode](./mpsnnmultiplicationnode.md)
  A representation of a multiplication operator.
- [class MPSNNMultiplicationGradientNode](./mpsnnmultiplicationgradientnode.md)
  A representation of a gradient multiplication operator.
- [class MPSNNDivisionNode](./mpsnndivisionnode.md)
  A representation of a division operator.
- [class MPSNNArithmeticGradientNode](./mpsnnarithmeticgradientnode.md)
  A representation of the base class for gradient arithmetic operators.
- [class MPSNNArithmeticGradientStateNode](./mpsnnarithmeticgradientstatenode.md)
  A representation of the clamp mask used by gradient arithmetic operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnbinaryarithmeticnode)*