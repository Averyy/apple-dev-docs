# MTLBlendOperation

**Framework**: Metal  
**Kind**: enum

For every pixel, `MTLBlendOperation` determines how to combine and weight the source fragment values with the destination values. Some blend operations multiply the source values by a source blend factor (SBF), multiply the destination values by a destination blend factor (DBF), and then combine the results using addition or subtraction. Other blend operations use either a minimum or maximum function to determine the result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLBlendOperation
```

## Topics

### Blend operations
- [MTLBlendOperation.add](mtlblendoperation/add.md)
  Add portions of both source and destination pixel values.
- [MTLBlendOperation.subtract](mtlblendoperation/subtract.md)
  Subtract a portion of the destination pixel values from a portion of the source.
- [MTLBlendOperation.reverseSubtract](mtlblendoperation/reversesubtract.md)
  Subtract a portion of the source values from a portion of the destination pixel values.
- [MTLBlendOperation.min](mtlblendoperation/min.md)
  Minimum of the source and destination pixel values.
- [MTLBlendOperation.max](mtlblendoperation/max.md)
  Maximum of the source and destination pixel values.
### Enumeration Cases
- [MTLBlendOperation.unspecialized](mtlblendoperation/unspecialized.md)
  Defers assigning the blend operation.
### Initializers
- [init?(rawValue: UInt)](mtlblendoperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isBlendingEnabled: Bool](mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled.md)
  A Boolean value that determines whether blending is enabled.
- [var alphaBlendOperation: MTLBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/alphablendoperation.md)
  The blend operation assigned for the alpha data.
- [var rgbBlendOperation: MTLBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation.md)
  The blend operation assigned for the RGB data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblendoperation)*