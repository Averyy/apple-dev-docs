# UserCopyDataBuffer

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the data buffer associated with a particular I/O request.

**Availability**:
- DriverKit 27.3+ (Beta)

## Declaration

```cpp
virtual kern_return_t UserCopyDataBuffer(SCSIDeviceIdentifier targetID, uint64_t controllerTaskID, IOBufferMemoryDescriptor **buffer);
```

## Return Value

A value that indicates the result of getting the buffer. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

## Discussion

Your dext class can call this method inside [`UserProcessParallelTask`](./userprocessparalleltask.md) to get the data buffer associated with the I/O request identified by `controllerTaskID`. Calling this method can have a significant impact on performance, so call it only if you require access to the data buffer. The caller needs to prepare new DMA mappings for this buffer and can no longer use the mappings in [`fBufferIOVMAddr`](../scsiuserparalleltask/fbufferiovmaddr.md).

Ownership of `buffer` transfers to the caller. Release the buffer when you’re done with it, before you invoke the parallel task completion callback. Failing to release the buffer causes a memory leak.

## Parameters

- `targetID`: The identifier of the target to check.
- `controllerTaskID`: A task identifier that uniquely identifies this I/O. This should be the same as [`fControllerTaskIdentifier`](../scsiuserparalleltask/fcontrollertaskidentifier.md) in the [`SCSIUserParallelTask`](../scsiuserparalleltask.md) structure.
- `buffer`: On return, the retrieved [`IOBufferMemoryDescriptor`](../../DriverKit/iobuffermemorydescriptor.md).

## See Also

### Accessing data buffers
- [UserGetDataBuffer](./usergetdatabuffer.md)
  Gets the data buffer associated with a particular I/O request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usercopydatabuffer)*