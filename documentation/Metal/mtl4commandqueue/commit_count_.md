# commit:count:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Enqueues an array of command buffers for execution.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) commit:(id<MTL4CommandBuffer> const[]) commandBuffers count:(NSUInteger) count;
```

## Mentions

- [Understanding the Metal 4 core API](../understanding-the-metal-4-core-api.md)

## Discussion

The order in which you sort the command buffers in the array is meaningful, especially when it contains suspending/resuming render passes. A suspending/resuming render pass is a render pass you create by calling [`makeRenderCommandEncoder(descriptor:options:)`](../mtl4commandbuffer/makerendercommandencoder%28descriptor,options%29.md), and provide `MTL4RenderEncoderOptionSuspending` or `MTL4RenderEncoderOptionResuming` for the `options` parameter.

If your command buffers contain suspend/resume render passes, ensure that the first command buffer only suspends, and the last one only resumes. Additionally, make sure that all intermediate command buffers are both suspending and resuming.

## Parameters

- `commandBuffers`: An array of [`MTL4CommandBuffer`](../mtl4commandbuffer.md).
- `count`: The number of [`MTL4CommandBuffer`](../mtl4commandbuffer.md) instances in the `commandBuffers` array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/commit:count:)*