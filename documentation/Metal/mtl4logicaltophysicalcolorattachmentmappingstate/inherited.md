# MTL4LogicalToPhysicalColorAttachmentMappingState.inherited

**Framework**: Metal  
**Kind**: case

Deduces the color attachment mapping by inheriting it from the color attachment map of the current encoder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case inherited
```

#### Discussion

This setting instructs the pipeline state to inherit the color attachment map of the current render encoder:

- For an [`MTL4RenderCommandEncoder`](mtl4rendercommandencoder.md), call its [`setColorAttachmentMap(_:)`](mtl4rendercommandencoder/setcolorattachmentmap(_:).md) method.
- For an [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md), call its [`setColorAttachmentMap(_:)`](mtlrendercommandencoder/setcolorattachmentmap(_:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4logicaltophysicalcolorattachmentmappingstate/inherited)*