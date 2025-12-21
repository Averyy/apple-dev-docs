# subscript(_:)

**Framework**: Metal  
**Kind**: subscript

Returns the render pipeline state for the specified color attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
subscript(attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor! { get set }
```

#### Return Value

An [`MTLRenderPipelineColorAttachmentDescriptor`](mtlrenderpipelinecolorattachmentdescriptor.md) instance that describes the render pipeline information for a color attachment.

## Parameters

- `attachmentIndex`: An index in the color attachment array.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray/subscript(_:))*