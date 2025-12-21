# colorAttachmentMappingState

**Framework**: Metal  
**Kind**: property

Configures a logical-to-physical rendering remap state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var colorAttachmentMappingState: MTL4LogicalToPhysicalColorAttachmentMappingState { get set }
```

#### Discussion

Use this property to assign how a [`MTL4RenderCommandEncoder`](mtl4rendercommandencoder.md) instance maps the output of your fragment shader to physical color attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/colorattachmentmappingstate)*