# MTLCommandEncoder

**Framework**: Metal  
**Kind**: protocol

An encoder that writes GPU commands into a command buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLCommandEncoder : NSObjectProtocol
```

## Mentions

- [Setting up a command structure](setting-up-a-command-structure.md)
- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Overview

Don’t implement this protocol yourself; instead you call methods on an [`MTLCommandBuffer`](mtlcommandbuffer.md) instance to create command encoders. Command encoder instances are lightweight instances that you re-create every time you need to send commands to the GPU.

There are many different kinds of command encoders, each providing a different set of commands that can be encoded into the buffer. A command encoder implements the [`MTLCommandEncoder`](mtlcommandencoder.md) protocol and an additional protocol specific to the kind of encoder being created.

| Protocol | Task |
| --- | --- |
| [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) | Graphics rendering |
| [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) | Computation |
| [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) | Memory management |
| [`MTLParallelRenderCommandEncoder`](mtlparallelrendercommandencoder.md) | Multiple graphics rendering tasks encoded in parallel. |

While a command encoder is active, it has the exclusive right to append commands to its command buffer. Once you finish encoding commands, call the [`endEncoding()`](mtlcommandencoder/endencoding().md) method to finish encoding the commands. To write further commands into the same command buffer, create a new command encoder.

You can call the [`insertDebugSignpost(_:)`](mtlcommandencoder/insertdebugsignpost(_:).md), [`pushDebugGroup(_:)`](mtlcommandencoder/pushdebuggroup(_:).md), and [`popDebugGroup()`](mtlcommandencoder/popdebuggroup().md) methods to put debug strings into the command buffer and to push or pop string labels used to identify groups of encoded commands. These methods don’t change the rendering or compute behavior of your app; the Xcode debugger uses them to organize your app’s rendering commands in a format that may provide insight into how your app works.

## Topics

### Ending command encoding
- [func endEncoding()](mtlcommandencoder/endencoding.md)
  Declares that all command generation from the encoder is completed.
### Annotating the command buffer with debug information
- [func insertDebugSignpost(String)](mtlcommandencoder/insertdebugsignpost(_:).md)
  Inserts a debug string into the captured frame data.
- [func pushDebugGroup(String)](mtlcommandencoder/pushdebuggroup(_:).md)
  Pushes a specific string onto a stack of debug group strings for the command encoder.
- [func popDebugGroup()](mtlcommandencoder/popdebuggroup.md)
  Pops the latest string off of a stack of debug group strings for the command encoder.
### Identifying the command encoder
- [var device: any MTLDevice](mtlcommandencoder/device.md)
  The Metal device from which the command encoder was created.
- [var label: String?](mtlcommandencoder/label.md)
  A string that labels the command encoder.
### Instance Methods
- [func barrier(afterQueueStages: MTLStages, beforeStages: MTLStages)](mtlcommandencoder/barrier(afterqueuestages:beforestages:).md)
  Encodes a consumer barrier on work you commit to the same command queue.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md)
- [MTLBlitCommandEncoder](mtlblitcommandencoder.md)
- [MTLComputeCommandEncoder](mtlcomputecommandencoder.md)
- [MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md)
- [MTLRenderCommandEncoder](mtlrendercommandencoder.md)
- [MTLResourceStateCommandEncoder](mtlresourcestatecommandencoder.md)

## See Also

- [Setting up a command structure](setting-up-a-command-structure.md)
  Discover how Metal executes commands on a GPU.
- [protocol MTLCommandQueue](mtlcommandqueue.md)
  An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.
- [class MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md)
  A configuration that customizes the behavior for a new command queue.
- [protocol MTLCommandBuffer](mtlcommandbuffer.md)
  A container that stores a sequence of GPU commands that you encode into it.
- [class MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md)
  A configuration that customizes the behavior for a new command buffer.
- [struct MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencoder)*