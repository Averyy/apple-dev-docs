# MTLCommandBufferDescriptor

**Framework**: Metal  
**Kind**: class

A configuration that customizes the behavior for a new command buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLCommandBufferDescriptor
```

#### Overview

Create a command buffer with a custom configuration by creating an [`MTLCommandBufferDescriptor`](mtlcommandbufferdescriptor.md) instance and passing it to an [`MTLCommandQueue`](mtlcommandqueue.md) instance’s [`makeCommandBuffer(descriptor:)`](mtlcommandqueue/makecommandbuffer(descriptor:).md) method. You can configure whether the command buffer retains references to resources that its commands refer to with the [`retainedReferences`](mtlcommandbufferdescriptor/retainedreferences.md) property. The command buffer can save extra error information, which is useful during development, by setting its [`errorOptions`](mtlcommandbufferdescriptor/erroroptions.md) property to [`encoderExecutionStatus`](mtlcommandbuffererroroption/encoderexecutionstatus.md).

## Topics

### Configuring the command buffer
- [var logState: (any MTLLogState)?](mtlcommandbufferdescriptor/logstate.md)
  The shader logging configuration that the command buffer uses.
- [var retainedReferences: Bool](mtlcommandbufferdescriptor/retainedreferences.md)
  A Boolean value that indicates whether the command buffer the descriptor creates maintains strong references to the resources it uses.
- [var errorOptions: MTLCommandBufferErrorOption](mtlcommandbufferdescriptor/erroroptions.md)
  The reporting configuration that indicates which information the GPU driver stores in a command buffer’s error property.
- [struct MTLCommandBufferErrorOption](mtlcommandbuffererroroption.md)
  Options for reporting errors from a command buffer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Setting up a command structure](setting-up-a-command-structure.md)
  Discover how Metal executes commands on a GPU.
- [protocol MTLCommandQueue](mtlcommandqueue.md)
  An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.
- [class MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md)
  A configuration that customizes the behavior for a new command queue.
- [protocol MTLCommandBuffer](mtlcommandbuffer.md)
  A container that stores a sequence of GPU commands that you encode into it.
- [struct MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [protocol MTLCommandEncoder](mtlcommandencoder.md)
  An encoder that writes GPU commands into a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferdescriptor)*