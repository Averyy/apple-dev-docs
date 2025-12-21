# commit(_:options:)

**Framework**: Metal  
**Kind**: method

Enqueues an array of command buffer instances for execution with a set of options.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func commit(_ commandBuffers: [any MTL4CommandBuffer], options: MTL4CommitOptions? = nil)
```

#### Discussion

Provide an [`MTL4CommitOptions`](mtl4commitoptions.md) instance to configure the commit operation.

The order in which you sort the command buffers in the array is meaningful, especially when it contains suspending/resuming render passes. A suspending/resuming render pass is a render pass you create by calling [`makeRenderCommandEncoder(descriptor:options:)`](mtl4commandbuffer/makerendercommandencoder(descriptor:options:).md), and provide `MTL4RenderEncoderOptionSuspending` or `MTL4RenderEncoderOptionResuming` for the `options` parameter.

If your command buffers contain suspend/resume render passes, ensure that the first command buffer only suspends, and the last one only resumes. Additionally, make sure that all intermediate command buffers are both suspending and resuming.

When you commit work from multiple threads, modifying and reusing the same options instance, you are responsible for externally synchronizing access to it.

## Parameters

- `commandBuffers`: A Swift array of   to commit.
- `options`: An instance of   that configures the commit operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/commit(_:options:))*