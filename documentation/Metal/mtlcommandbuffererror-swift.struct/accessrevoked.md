# accessRevoked

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var accessRevoked: MTLCommandBufferError.Code { get }
```

## See Also

### Errors codes
- [static var none: MTLCommandBufferError.Code](./none.md)
  An error code that represents the absence of any problems.
- [static var timeout: MTLCommandBufferError.Code](./timeout.md)
  An error code that indicates the system interrupted and terminated the command buffer before it finished running.
- [static var pageFault: MTLCommandBufferError.Code](./pagefault.md)
  An error code that indicates the command buffer generated a page fault the GPU can’t service.
- [static var notPermitted: MTLCommandBufferError.Code](./notpermitted.md)
  An error code that indicates a process doesn’t have access to a GPU device.
- [static var outOfMemory: MTLCommandBufferError.Code](./outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to execute a command buffer.
- [static var invalidResource: MTLCommandBufferError.Code](./invalidresource.md)
  An error code that indicates the command buffer has an invalid reference to resource.
- [static var memoryless: MTLCommandBufferError.Code](./memoryless.md)
  An error code that indicates the GPU ran out of one or more of its internal resources that support memoryless render pass attachments.
- [static var deviceRemoved: MTLCommandBufferError.Code](./deviceremoved.md)
  An error code that indicates a person physically removed the GPU device before the command buffer finished running.
- [static var stackOverflow: MTLCommandBufferError.Code](./stackoverflow.md)
  An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.
- [static var `internal`: MTLCommandBufferError.Code](./internal.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLCommandBufferError.Code](./code.md)
  Error codes that indicate why a GPU is unable to finish running a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/accessrevoked)*