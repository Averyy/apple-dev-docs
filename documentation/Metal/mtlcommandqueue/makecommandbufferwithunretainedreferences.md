# makeCommandBufferWithUnretainedReferences()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a command buffer from the command queue that doesn’t maintain strong references to resources.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeCommandBufferWithUnretainedReferences() -> (any MTLCommandBuffer)?
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Discussion

Use this method to create a command buffer that doesn’t retain or release any of the resources it needs to run its commands.

Apps typically create command buffers that don’t maintain references to resources for extremely performance-critical situations. Even though the runtime cost for retaining or releasing a single resource is trivial, the aggregate time savings may be worth it.

It’s your app’s responsibility to maintain strong references to all the resources the command buffer uses until it finishes running on the GPU.

> ❗ **Important**:  Releasing a resource before a command buffer’s commands complete may trigger a runtime error or erratic behavior.

This method sets the [`retainedReferences`](mtlcommandbuffer/retainedreferences.md) property to [`false`](https://developer.apple.com/documentation/Swift/false) for the command buffer it creates.

Each command queue has a fixed number of command buffers for its lifetime (see [`makeCommandQueue(maxCommandBufferCount:)`](mtldevice/makecommandqueue(maxcommandbuffercount:).md)). This method blocks the calling CPU thread when the queue doesn’t have any free command buffers, and returns after the GPU finishes executing one.

## See Also

- [func makeCommandBuffer(descriptor: MTLCommandBufferDescriptor) -> (any MTLCommandBuffer)?](mtlcommandqueue/makecommandbuffer(descriptor:).md)
  Returns a command buffer from the command queue that you configure with a descriptor.
- [func makeCommandBuffer() -> (any MTLCommandBuffer)?](mtlcommandqueue/makecommandbuffer.md)
  Returns a command buffer from the command queue that maintains strong references to resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/makecommandbufferwithunretainedreferences())*