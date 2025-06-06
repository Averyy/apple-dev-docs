# subscript(_:)

**Framework**: Metal  
**Kind**: subscript

Returns the render pipeline state for the specified color attachment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
subscript(attachmentIndex: Int) -> MTLTileRenderPipelineColorAttachmentDescriptor { get set }
```

#### Return Value

A [`MTLTileRenderPipelineColorAttachmentDescriptor`](mtltilerenderpipelinecolorattachmentdescriptor.md) that describes the render pipeline information for a color attachment.

## Parameters

- `attachmentIndex`: An index in the color attachment array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltilerenderpipelinecolorattachmentdescriptorarray/subscript(_:))*