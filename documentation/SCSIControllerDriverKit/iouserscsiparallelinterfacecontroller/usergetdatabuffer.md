# UserGetDataBuffer

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Gets the data buffer associated with a particular I/O request.

**Availability**:
- DriverKit ?+

## Declaration

```swift
virtual kern_return_t UserGetDataBuffer(SCSIDeviceIdentifier targetID, uint64_t controllerTaskID, IOBufferMemoryDescriptor **buffer);
```

#### Return Value

A value that indicates the result of getting the buffer. [`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Your dext class can call this method inside [`UserProcessParallelTask`](iouserscsiparallelinterfacecontroller/userprocessparalleltask.md) to get the data buffer associated with the I/O request identified by `controllerTaskID`. Calling this method can have a significant impact on performance, so call it only if you require access to the data buffer. The caller needs to prepare new DMA mappings for this buffer and can no longer use the mappings in [`fBufferIOVMAddr`](scsiuserparalleltask/fbufferiovmaddr.md).

The framework releases the buffer when the caller invokes the parallel task completion callback. Don’t retain this buffer after invoking the task completion callback.

## Parameters

- `targetID`: The identifier of the target to check.
- `controllerTaskID`: A task identifiers that uniquely identifies this I/O. This should be the same as [`fControllerTaskIdentifier`](scsiuserparalleltask/fcontrollertaskidentifier.md) in the [`SCSIUserParallelTask`](scsiuserparalleltask.md) structure.
- `buffer`: On return, the retrieved [`IOBufferMemoryDescriptor`](https://developer.apple.com/documentation/driverkit/iobuffermemorydescriptor).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usergetdatabuffer)*