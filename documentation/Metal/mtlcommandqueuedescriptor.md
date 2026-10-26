# MTLCommandQueueDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

A configuration that customizes the behavior for a new command queue.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class MTLCommandQueueDescriptor
```

```objc
@interface MTLCommandQueueDescriptor : NSObject
```

## Topics

### Instance Properties
- [var logState: (any MTLLogState)?](./mtlcommandqueuedescriptor/logstate.md)
  The shader logging configuration that the command queue uses.
- [var maxCommandBufferCount: Int](./mtlcommandqueuedescriptor/maxcommandbuffercount.md)
  An integer that sets the maximum number of uncompleted command buffers the queue can allow.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Submitting work to a GPU with Metal
- [Setting up a command structure](./setting-up-a-command-structure.md)
  Discover how Metal executes commands on a GPU.
- [protocol MTLCommandQueue](./mtlcommandqueue.md)
  An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueuedescriptor)*