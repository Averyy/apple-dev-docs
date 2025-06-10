# MTLCommandQueue

**Framework**: Metal  
**Kind**: protocol

An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLCommandQueue : NSObjectProtocol, Sendable
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)
- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Overview

A command queue maintains an ordered list of command buffers. You use a command queue to:

- Create command buffers, which you fill with commands for the GPU device that creates the queue
- Submit command buffers to run on that GPU

Create a command queue from an [`MTLDevice`](mtldevice.md) instance by calling its [`makeCommandQueue()`](mtldevice/makecommandqueue().md) or [`makeCommandQueue(maxCommandBufferCount:)`](mtldevice/makecommandqueue(maxcommandbuffercount:).md) method. Typically, you create one or more command queues when your app launches and then keep them throughout your app’s lifetime.

With each [`MTLCommandQueue`](mtlcommandqueue.md) instance you create, you can create [`MTLCommandBuffer`](mtlcommandbuffer.md) instances for that queue by calling its [`makeCommandBuffer()`](mtlcommandqueue/makecommandbuffer().md) or [`makeCommandBufferWithUnretainedReferences()`](mtlcommandqueue/makecommandbufferwithunretainedreferences().md) method.

> **Note**:  Each command queue is thread-safe and allows you to encode commands in multiple command buffers simultaneously.

For more information about command buffers and encoding GPU commands to them — such as rendering images and computing data in parallel — see [`Setting Up a Command Structure`](setting-up-a-command-structure.md).

## Topics

### Creating Command Buffers
- [func makeCommandBuffer(descriptor: MTLCommandBufferDescriptor) -> (any MTLCommandBuffer)?](mtlcommandqueue/makecommandbuffer(descriptor:).md)
  Returns a command buffer from the command queue that you configure with a descriptor.
- [func makeCommandBuffer() -> (any MTLCommandBuffer)?](mtlcommandqueue/makecommandbuffer.md)
  Returns a command buffer from the command queue that maintains strong references to resources.
- [func makeCommandBufferWithUnretainedReferences() -> (any MTLCommandBuffer)?](mtlcommandqueue/makecommandbufferwithunretainedreferences.md)
  Returns a command buffer from the command queue that doesn’t maintain strong references to resources.
### Attaching Residency Sets
- [func addResidencySet(any MTLResidencySet)](mtlcommandqueue/addresidencyset(_:).md)
  Attaches a residency set to the queue, which Metal attaches to its command buffers as you commit them.
- [func addResidencySets([any MTLResidencySet])](mtlcommandqueue/addresidencysets(_:).md)
  Attaches multiple residency sets to the queue, which Metal attaches to its command buffers as you commit them.
### Detaching Residency Sets
- [func removeResidencySet(any MTLResidencySet)](mtlcommandqueue/removeresidencyset(_:).md)
  Detaches a residency set from the command queue, which prevents Metal from attaching it to the queue’s command buffers as you commit them.
- [func removeResidencySets([any MTLResidencySet])](mtlcommandqueue/removeresidencysets(_:).md)
  Detaches multiple residency sets from the command queue, which prevents Metal from attaching them to the queue’s command buffers as you commit them.
### Identifying the Command Queue
- [var device: any MTLDevice](mtlcommandqueue/device.md)
  The GPU device that creates the command queue.
- [var label: String?](mtlcommandqueue/label.md)
  An optional name that can help you identify the command queue.
### Deprecated
- [func insertDebugCaptureBoundary()](mtlcommandqueue/insertdebugcaptureboundary.md)
  Informs Xcode about when GPU Frame Capture starts and stops.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Setting Up a Command Structure](setting-up-a-command-structure.md)
  Discover how Metal executes commands on a GPU.
- [class MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md)
  A configuration that customizes the behavior for a new command queue.
- [protocol MTLCommandBuffer](mtlcommandbuffer.md)
  A container that stores a sequence of GPU commands that you encode into it.
- [class MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md)
  A configuration that customizes the behavior for a new command buffer.
- [struct MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [protocol MTLCommandEncoder](mtlcommandencoder.md)
  An encoder that writes GPU commands into a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue)*