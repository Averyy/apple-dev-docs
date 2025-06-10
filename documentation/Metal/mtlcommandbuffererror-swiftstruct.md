# MTLCommandBufferError

**Framework**: Metal  
**Kind**: struct

The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct MTLCommandBufferError
```

## Topics

### Errors Codes
- [static var none: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/none.md)
  An error code that represents the absence of any problems.
- [static var timeout: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/timeout.md)
  An error code that indicates the system interrupted and terminated the command buffer because it took more time to execute than the system allows.
- [static var pageFault: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/pagefault.md)
  An error code that indicates the command buffer generated a page fault the GPU can’t service.
- [static var notPermitted: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/notpermitted.md)
  An error code that indicates a process doesn’t have access to a GPU device.
- [static var outOfMemory: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to execute a command buffer.
- [static var invalidResource: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/invalidresource.md)
  An error code that indicates the command buffer has an invalid reference to resource.
- [static var memoryless: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/memoryless.md)
  An error code that indicates the GPU ran out of one or more of its internal resources that support memoryless render pass attachments.
- [static var deviceRemoved: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/deviceremoved.md)
  An error code that indicates a person physically removed the GPU device before the command buffer finished running.
- [static var stackOverflow: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/stackoverflow.md)
  An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.
- [static var accessRevoked: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/accessrevoked.md)
  An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
- [static var `internal`: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/internal.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/code.md)
  Error codes that indicate why a GPU is unable to finish running a command buffer.
### Error Domain
- [static var errorDomain: String](mtlcommandbuffererror-swift.struct/errordomain.md)
  The current command buffer error domain.
- [let MTLCommandBufferErrorDomain: String](mtlcommandbuffererrordomain.md)
  The domain for Metal command buffer errors.
### Deprecated
- [static var blacklisted: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/blacklisted.md)
  A former error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Setting Up a Command Structure](setting-up-a-command-structure.md)
  Discover how Metal executes commands on a GPU.
- [protocol MTLCommandQueue](mtlcommandqueue.md)
  An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.
- [class MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md)
  A configuration that customizes the behavior for a new command queue.
- [protocol MTLCommandBuffer](mtlcommandbuffer.md)
  A container that stores a sequence of GPU commands that you encode into it.
- [class MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md)
  A configuration that customizes the behavior for a new command buffer.
- [protocol MTLCommandEncoder](mtlcommandencoder.md)
  An encoder that writes GPU commands into a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct)*