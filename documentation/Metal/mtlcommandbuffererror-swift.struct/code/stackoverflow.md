# MTLCommandBufferError.Code.stackOverflow

**Framework**: Metal  
**Kind**: case

An error code that indicates the GPU terminated the command buffer because a kernel function of tile shader used too many stack frames.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case stackOverflow
```

#### Discussion

You can set the largest number of stack frames your pipelines by configuring these properties:

- [`MTLComputePipelineDescriptor`](mtlcomputepipelinedescriptor.md)`.`[`maxCallStackDepth`](mtlcomputepipelinedescriptor/maxcallstackdepth.md) for kernel functions
- [`MTLTileRenderPipelineDescriptor`](mtltilerenderpipelinedescriptor.md)`.`[`maxCallStackDepth`](mtltilerenderpipelinedescriptor/maxcallstackdepth.md) for tile shaders

## See Also

- [MTLCommandBufferError.Code.none](mtlcommandbuffererror-swift.struct/code/none.md)
  An error code that represents the absence of any problems.
- [MTLCommandBufferError.Code.timeout](mtlcommandbuffererror-swift.struct/code/timeout.md)
  An error code that indicates the system interrupted and terminated the command buffer before it finished running.
- [MTLCommandBufferError.Code.pageFault](mtlcommandbuffererror-swift.struct/code/pagefault.md)
  An error code that indicates the command buffer generated a page fault the GPU can’t service.
- [MTLCommandBufferError.Code.notPermitted](mtlcommandbuffererror-swift.struct/code/notpermitted.md)
  An error code that indicates a process doesn’t have access to a GPU device.
- [MTLCommandBufferError.Code.outOfMemory](mtlcommandbuffererror-swift.struct/code/outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to execute a command buffer.
- [MTLCommandBufferError.Code.invalidResource](mtlcommandbuffererror-swift.struct/code/invalidresource.md)
  An error code that indicates the command buffer has an invalid reference to resource.
- [MTLCommandBufferError.Code.memoryless](mtlcommandbuffererror-swift.struct/code/memoryless.md)
  An error code that indicates the GPU ran out of one or more of its internal resources that support memoryless render pass attachments.
- [MTLCommandBufferError.Code.deviceRemoved](mtlcommandbuffererror-swift.struct/code/deviceremoved.md)
  An error code that indicates a person physically removed the GPU device before the command buffer finished running.
- [static var accessRevoked: MTLCommandBufferError.Code](mtlcommandbuffererror-swift.struct/code/accessrevoked.md)
  An error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.
- [MTLCommandBufferError.Code.internal](mtlcommandbuffererror-swift.struct/code/internal.md)
  An error code that indicates the Metal framework has an internal problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/code/stackoverflow)*