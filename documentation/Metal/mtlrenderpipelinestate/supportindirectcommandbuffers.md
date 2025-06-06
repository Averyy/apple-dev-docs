# supportIndirectCommandBuffers

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the render pipeline supports encoding commands into an indirect command buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var supportIndirectCommandBuffers: Bool { get }
```

#### Discussion

This property gets its value by copying from the [`supportIndirectCommandBuffers`](mtlrenderpipelinedescriptor/supportindirectcommandbuffers.md) property of the [`MTLRenderPipelineDescriptor`](mtlrenderpipelinedescriptor.md) instance as the GPU device creates the pipeline state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/supportindirectcommandbuffers)*