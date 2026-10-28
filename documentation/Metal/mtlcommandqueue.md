# MTLCommandQueue

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
protocol MTLCommandQueue : NSObjectProtocol, Sendable
```

```objc
@protocol MTLCommandQueue <NSObject>
```

## Mentions

- [Understanding the Metal 4 core API](./understanding-the-metal-4-core-api.md)
- [Simplifying GPU resource management with residency sets](./simplifying-gpu-resource-management-with-residency-sets.md)

## Overview

A command queue maintains an ordered list of command buffers. You use a command queue to:

- Create command buffers, which you fill with commands for the GPU device that creates the queue
- Submit command buffers to run on that GPU

Create a command queue from an [`MTLDevice`](./mtldevice.md) instance by calling its [`makeCommandQueue()`](./mtldevice/makecommandqueue%28%29.md) or [`makeCommandQueue(maxCommandBufferCount:)`](./mtldevice/makecommandqueue%28maxcommandbuffercount%29.md) method. Typically, you create one or more command queues when your app launches and then keep them throughout your app’s lifetime.

With each [`MTLCommandQueue`](./mtlcommandqueue.md) instance you create, you can create [`MTLCommandBuffer`](./mtlcommandbuffer.md) instances for that queue by calling its [`makeCommandBuffer()`](./mtlcommandqueue/makecommandbuffer%28%29.md) or [`makeCommandBufferWithUnretainedReferences()`](./mtlcommandqueue/makecommandbufferwithunretainedreferences%28%29.md) method.

> **Note**:  Each command queue is thread-safe and allows you to encode commands in multiple command buffers simultaneously.

For more information about command buffers and encoding GPU commands to them — such as rendering images and computing data in parallel — see [Setting up a command structure](./setting-up-a-command-structure.md).

## Topics

### Creating command buffers
- [func makeCommandBuffer(descriptor: MTLCommandBufferDescriptor) -> (any MTLCommandBuffer)?](./mtlcommandqueue/makecommandbuffer%28descriptor%29.md)
  Returns a command buffer from the command queue that you configure with a descriptor.
- [func makeCommandBuffer() -> (any MTLCommandBuffer)?](./mtlcommandqueue/makecommandbuffer%28%29.md)
  Returns a command buffer from the command queue that maintains strong references to resources.
- [func makeCommandBufferWithUnretainedReferences() -> (any MTLCommandBuffer)?](./mtlcommandqueue/makecommandbufferwithunretainedreferences%28%29.md)
  Returns a command buffer from the command queue that doesn’t maintain strong references to resources.
### Attaching residency sets
- [func addResidencySet(any MTLResidencySet)](./mtlcommandqueue/addresidencyset%28_%29.md)
  Applies a residency set to a queue, which Metal applies to the queue’s command buffers as you commit them.
- [func addResidencySets([any MTLResidencySet])](./mtlcommandqueue/addresidencysets%28_%29.md)
  Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.
- [- addResidencySets:count:](./mtlcommandqueue/addresidencysets_count_.md)
  Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.
### Detaching residency sets
- [func removeResidencySet(any MTLResidencySet)](./mtlcommandqueue/removeresidencyset%28_%29.md)
  Removes a residency set from a command queue’s list, which means Metal doesn’t apply it to the queue’s command buffers as you commit them.
- [func removeResidencySets([any MTLResidencySet])](./mtlcommandqueue/removeresidencysets%28_%29.md)
  Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.
- [- removeResidencySets:count:](./mtlcommandqueue/removeresidencysets_count_.md)
  Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.
### Identifying the command queue
- [var device: any MTLDevice](./mtlcommandqueue/device.md)
  The GPU device that creates the command queue.
- [var label: String?](./mtlcommandqueue/label.md)
  An optional name that can help you identify the command queue.
### Deprecated
- [func insertDebugCaptureBoundary()](./mtlcommandqueue/insertdebugcaptureboundary%28%29.md)
  Informs Xcode about when GPU Frame Capture starts and stops.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Submitting work to a GPU with Metal
- [Setting up a command structure](./setting-up-a-command-structure.md)
  Discover how Metal executes commands on a GPU.
- [class MTLCommandQueueDescriptor](./mtlcommandqueuedescriptor.md)
  A configuration that customizes the behavior for a new command queue.
- [protocol MTLCommandBuffer](./mtlcommandbuffer.md)
  A container that stores a sequence of GPU commands that you encode into it.
- [class MTLCommandBufferDescriptor](./mtlcommandbufferdescriptor.md)
  A configuration that customizes the behavior for a new command buffer.
- [struct MTLCommandBufferError](./mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [protocol MTLCommandEncoder](./mtlcommandencoder.md)
  An encoder that writes GPU commands into a command buffer.
### Submitting work to a GPU
- [MTLCommandBufferErrorDomain](./mtlcommandbuffererrordomain.md)
  The domain for Metal command buffer errors.
- [MTLCommandBufferError](./mtlcommandbuffererror-swift.struct/code.md)
  Error codes that indicate why a GPU is unable to finish running a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue)*