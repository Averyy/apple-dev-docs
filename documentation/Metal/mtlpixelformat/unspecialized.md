# MTLPixelFormat.unspecialized

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Defers assigning the pixel format.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case unspecialized
```

```c
MTLPixelFormatUnspecialized
```

## Mentions

- [Using the Metal 4 compilation API](../using-the-metal-4-compilation-api.md)

## Discussion

Assign this format to a color attachment’s `pixelFormat` in a render pipeline descriptor to build a pipeline state that leaves the attachment’s format unresolved. To finalize the format, pass a descriptor that assigns a concrete format to [`newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:`](../mtl4compiler/newrenderpipelinestatebyspecializationwithdescriptor_pipeline_error_.md), which returns a specialized pipeline state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/unspecialized)*