# makeCommandBuffer(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a command buffer from the command queue that you configure with a descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makeCommandBuffer(descriptor: MTLCommandBufferDescriptor) -> (any MTLCommandBuffer)?
```

#### Discussion

Use this method to create a command buffer that you configure with a descriptor. You can configure whether the command buffer retains references to resources that its commands refer to by setting the `descriptor` parameter’s [`retainedReferences`](mtlcommandbufferdescriptor/retainedreferences.md) property. You can also configure whether the command buffer saves extra error information, which is useful during development, by setting the descriptor’s [`errorOptions`](mtlcommandbufferdescriptor/erroroptions.md) property.

Each command queue has a fixed number of command buffers for its lifetime (see [`makeCommandQueue(maxCommandBufferCount:)`](mtldevice/makecommandqueue(maxcommandbuffercount:).md)). This method blocks the calling CPU thread when the queue doesn’t have any free command buffers, and returns after the GPU finishes executing one.

## Parameters

- `descriptor`: An   instance that configures the   the method returns.

## See Also

- [func makeCommandBuffer() -> (any MTLCommandBuffer)?](mtlcommandqueue/makecommandbuffer.md)
  Returns a command buffer from the command queue that maintains strong references to resources.
- [func makeCommandBufferWithUnretainedReferences() -> (any MTLCommandBuffer)?](mtlcommandqueue/makecommandbufferwithunretainedreferences.md)
  Returns a command buffer from the command queue that doesn’t maintain strong references to resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/makecommandbuffer(descriptor:))*