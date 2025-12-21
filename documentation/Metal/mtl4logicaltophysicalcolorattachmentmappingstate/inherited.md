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

Use this setting to indicate Metal should inherit the mapping from the `colorAttachmentMap` property of the current [`MTL4RenderCommandEncoder`](mtl4rendercommandencoder.md) or [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) in use at draw time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4logicaltophysicalcolorattachmentmappingstate/inherited)*