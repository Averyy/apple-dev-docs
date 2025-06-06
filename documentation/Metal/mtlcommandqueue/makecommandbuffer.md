# makeCommandBuffer()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a command buffer from the command queue that maintains strong references to resources.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeCommandBuffer() -> (any MTLCommandBuffer)?
```

## Mentions

- [Setting Up a Command Structure](setting-up-a-command-structure.md)

#### Discussion

The command buffers you create with this method maintain strong references to the resources you encode into it, including buffers, textures, samplers, and pipeline states. The command buffer releases these references after it finishes running on the GPU.

This method sets the [`retainedReferences`](mtlcommandbuffer/retainedreferences.md) property to [`true`](https://developer.apple.com/documentation/swift/true) for the command buffer it creates.

Each command queue has a fixed number of command buffers for its lifetime (see [`makeCommandQueue(maxCommandBufferCount:)`](mtldevice/makecommandqueue(maxcommandbuffercount:).md)). This method blocks the calling CPU thread when the queue doesn’t have any free command buffers, and returns after the GPU finishes executing one.

## See Also

- [func makeCommandBuffer(descriptor: MTLCommandBufferDescriptor) -> (any MTLCommandBuffer)?](mtlcommandqueue/makecommandbuffer(descriptor:).md)
  Returns a command buffer from the command queue that you configure with a descriptor.
- [func makeCommandBufferWithUnretainedReferences() -> (any MTLCommandBuffer)?](mtlcommandqueue/makecommandbufferwithunretainedreferences.md)
  Returns a command buffer from the command queue that doesn’t maintain strong references to resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/makecommandbuffer())*