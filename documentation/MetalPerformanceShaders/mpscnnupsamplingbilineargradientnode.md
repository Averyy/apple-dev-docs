# MPSCNNUpsamplingBilinearGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a gradient bilinear spatial upsampling filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNUpsamplingBilinearGradientNode
```

```objc
@interface MPSCNNUpsamplingBilinearGradientNode : MPSNNGradientFilterNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, scaleFactorX: Double, scaleFactorY: Double)](./mpscnnupsamplingbilineargradientnode/init%28sourcegradient,sourceimage,gradientstate,scalefactorx,scalefactory%29.md)
### Instance Properties
- [var scaleFactorX: Double](./mpscnnupsamplingbilineargradientnode/scalefactorx.md)
- [var scaleFactorY: Double](./mpscnnupsamplingbilineargradientnode/scalefactory.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](./mpsnngradientfilternode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Upsampling Layer Nodes
- [class MPSCNNUpsamplingBilinearNode](./mpscnnupsamplingbilinearnode.md)
  A representation of a bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearestNode](./mpscnnupsamplingnearestnode.md)
  A representation of a nearest spatial upsampling filter.
- [class MPSCNNUpsamplingNearestGradientNode](./mpscnnupsamplingnearestgradientnode.md)
  A representation of a gradient nearest spatial upsampling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsamplingbilineargradientnode)*