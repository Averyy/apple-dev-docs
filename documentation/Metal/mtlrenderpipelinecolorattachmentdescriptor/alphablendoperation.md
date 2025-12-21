# alphaBlendOperation

**Framework**: Metal  
**Kind**: property

The blend operation assigned for the alpha data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var alphaBlendOperation: MTLBlendOperation { get set }
```

#### Discussion

The default value is [`MTLBlendOperation.add`](mtlblendoperation/add.md).

## See Also

- [var isBlendingEnabled: Bool](mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled.md)
  A Boolean value that determines whether blending is enabled.
- [var rgbBlendOperation: MTLBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation.md)
  The blend operation assigned for the RGB data.
- [enum MTLBlendOperation](mtlblendoperation.md)
  For every pixel, `MTLBlendOperation` determines how to combine and weight the source fragment values with the destination values. Some blend operations multiply the source values by a source blend factor (SBF), multiply the destination values by a destination blend factor (DBF), and then combine the results using addition or subtraction. Other blend operations use either a minimum or maximum function to determine the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/alphablendoperation)*