# MTLCommandBufferError.Code

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

Error codes that indicate why a GPU is unable to finish running a command buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum MTLCommandBufferError : NSUInteger;
```

## Topics

### Error codes
- [MTLCommandBufferError.Code.none](./code/none.md)
  An error code that represents the absence of any problems.
- [MTLCommandBufferError.Code.timeout](./code/timeout.md)
  An error code that indicates the system interrupted and terminated the command buffer before it finished running.
- [MTLCommandBufferError.Code.pageFault](./code/pagefault.md)
  An error code that indicates the command buffer generated a page fault the GPU can’t service.
- [MTLCommandBufferError.Code.notPermitted](./code/notpermitted.md)
  An error code that indicates a process doesn’t have access to a GPU device.
- [MTLCommandBufferError.Code.outOfMemory](./code/outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to execute a command buffer.
- [MTLCommandBufferError.Code.invalidResource](./code/invalidresource.md)
  An error code that indicates the command buffer has an invalid reference to resource.
- [MTLCommandBufferError.Code.memoryless](./code/memoryless.md)
  An error code that indicates the GPU ran out of one or more of its internal resources that support memoryless render pass attachments.
- [MTLCommandBufferError.Code.deviceRemoved](./code/deviceremoved.md)
  An error code that indicates a person physically removed the GPU device before the command buffer finished running.
- [MTLCommandBufferError.Code.stackOverflow](./code/stackoverflow.md)
  An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.
- [static var accessRevoked: MTLCommandBufferError.Code](./code/accessrevoked.md)
  An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
- [MTLCommandBufferError.Code.internal](./code/internal.md)
  An error code that indicates the Metal framework has an internal problem.
### Deprecated
- [MTLCommandBufferError.Code.blacklisted](./code/blacklisted.md)
  A former error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
### Initializers
- [init?(rawValue: UInt)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/code)*