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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/alphablendoperation)*