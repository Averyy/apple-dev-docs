# DoAsyncEjectMedia

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method  
**Role**: Instance Method

Ejects the media.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t DoAsyncEjectMedia(uint32_t requestID);
```

#### Return Value

A value that indicates the eject result. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

#### Discussion

When the eject operation completes, the dext calls your [`Complete`](./complete.md) method with the results of the operation.

## Parameters

- `requestID`: An opaque identifier. After the dext completes the request, it calls [`Complete`](./complete.md) and sends this value as a parameter.

## See Also

### Accessing the Device
- [DoAsyncUnmap](./doasyncunmap.md)
  Sends an asynchronous request to the dext to reclaim storage by unmapping.
- [BlockRange](../blockrange.md)
  A structure that represents a range of blocks.
- [DoAsyncSynchronize](./doasyncsynchronize.md)
  Forces the hardware buffer to flush data blocks to the media.
- [Complete](./complete.md)
  Indicates that the dext completed an asynchronous call.
- [DoAsyncReadWrite](./doasyncreadwrite.md)
  Starts an asynchronous read or write operation.
- [IOUserStorageOptions](../iouserstorageoptions.md)
  Options that affect the performance of read-write operations.
- [CompleteIO](./completeio.md)
  Indicates that the dext completed an asynchronous read-write call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/doasyncejectmedia)*