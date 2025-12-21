# isBlendingEnabled

**Framework**: Metal  
**Kind**: property

A Boolean value that determines whether blending is enabled.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var isBlendingEnabled: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false), meaning blending is disabled and pixel values are unaffected by blending. Disabled blending is effectively the same as the `MTLBlendOperationAdd` blend operation with a source blend factor of `1.0` and a destination blend factor of `0.0` for both RGB and alpha.

If the value is [`true`](https://developer.apple.com/documentation/Swift/true), blending is enabled and the blend descriptor property values are used to determine how source and destination color values are combined.

## See Also

- [var alphaBlendOperation: MTLBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/alphablendoperation.md)
  The blend operation assigned for the alpha data.
- [var rgbBlendOperation: MTLBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation.md)
  The blend operation assigned for the RGB data.
- [enum MTLBlendOperation](mtlblendoperation.md)
  For every pixel, `MTLBlendOperation` determines how to combine and weight the source fragment values with the destination values. Some blend operations multiply the source values by a source blend factor (SBF), multiply the destination values by a destination blend factor (DBF), and then combine the results using addition or subtraction. Other blend operations use either a minimum or maximum function to determine the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled)*