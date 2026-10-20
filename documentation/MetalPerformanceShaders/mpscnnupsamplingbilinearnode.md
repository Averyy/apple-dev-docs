# MPSCNNUpsamplingBilinearNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a bilinear spatial upsampling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNUpsamplingBilinearNode
```

```objc
@interface MPSCNNUpsamplingBilinearNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, integerScaleFactorX: Int, integerScaleFactorY: Int)](./mpscnnupsamplingbilinearnode/init%28source,integerscalefactorx,integerscalefactory%29.md)
- [init(source: MPSNNImageNode, integerScaleFactorX: Int, integerScaleFactorY: Int, alignCorners: Bool)](./mpscnnupsamplingbilinearnode/init%28source,integerscalefactorx,integerscalefactory,aligncorners%29.md)
### Instance Properties
- [var scaleFactorX: Double](./mpscnnupsamplingbilinearnode/scalefactorx.md)
- [var scaleFactorY: Double](./mpscnnupsamplingbilinearnode/scalefactory.md)
- [var alignCorners: Bool](./mpscnnupsamplingbilinearnode/aligncorners.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](./mpsnnfilternode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Upsampling Layer Nodes
- [class MPSCNNUpsamplingNearestNode](./mpscnnupsamplingnearestnode.md)
  A representation of a nearest spatial upsampling filter.
- [class MPSCNNUpsamplingBilinearGradientNode](./mpscnnupsamplingbilineargradientnode.md)
  A representation of a gradient bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearestGradientNode](./mpscnnupsamplingnearestgradientnode.md)
  A representation of a gradient nearest spatial upsampling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsamplingbilinearnode)*