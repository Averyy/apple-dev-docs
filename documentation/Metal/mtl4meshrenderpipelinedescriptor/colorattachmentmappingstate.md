# colorAttachmentMappingState

**Framework**: Metal  
**Kind**: property

Sets the logical-to-physical rendering remap state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var colorAttachmentMappingState: MTL4LogicalToPhysicalColorAttachmentMappingState { get set }
```

#### Discussion

Use this property to assign how a [`MTL4RenderCommandEncoder`](mtl4rendercommandencoder.md) instance maps the output of your fragment shader to physical color attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/colorattachmentmappingstate)*