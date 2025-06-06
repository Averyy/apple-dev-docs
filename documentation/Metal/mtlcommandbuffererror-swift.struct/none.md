# none

**Framework**: Metal  
**Kind**: property

An error code that represents the absence of any problems.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static var none: MTLCommandBufferError.Code { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/none)*