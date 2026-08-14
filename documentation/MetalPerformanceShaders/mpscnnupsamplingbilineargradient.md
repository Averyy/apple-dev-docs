# MPSCNNUpsamplingBilinearGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

A gradient bilinear spatial upsampling filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNUpsamplingBilinearGradient
```

## Topics

### Initializers
- [init(device: any MTLDevice, integerScaleFactorX: Int, integerScaleFactorY: Int)](mpscnnupsamplingbilineargradient/init(device:integerscalefactorx:integerscalefactory:).md)

## Relationships

### Inherits From
- [MPSCNNUpsamplingGradient](mpscnnupsamplinggradient.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MPSCNNUpsampling](mpscnnupsampling.md)
  A filter that resamples an existing MPS image.
- [class MPSCNNUpsamplingBilinear](mpscnnupsamplingbilinear.md)
  A bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearest](mpscnnupsamplingnearest.md)
  A nearest spatial upsampling filter.
- [class MPSCNNUpsamplingGradient](mpscnnupsamplinggradient.md)
  A gradient filter that upsamples an existing Metal Performance Shaders image.
- [class MPSCNNUpsamplingNearestGradient](mpscnnupsamplingnearestgradient.md)
  A gradient upsampling filter that samples the pixel nearest to the source when upsampling to the destination pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsamplingbilineargradient)*