# CompleteIO

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method  
**Role**: Instance Method

Indicates that the dext completed an asynchronous read-write call.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual void CompleteIO(uint32_t requestID, uint64_t bytesTransferred, kern_return_t IOStatus);
```

#### Discussion

The dext calls this method to indicate completion of an asynchronous read-write call. Use the `requestID` parameter to determine which [`DoAsyncReadWrite`](./doasyncreadwrite.md) call resulted in this callback.

## Parameters

- `requestID`: An opaque identifier, originally provided in the corresponding [`DoAsyncReadWrite`](./doasyncreadwrite.md) call.
- `bytesTransferred`: The number of bytes transferred.
- `IOStatus`: The status of the request.

## See Also

### Accessing the Device
- [DoAsyncUnmap](./doasyncunmap.md)
  Sends an asynchronous request to the dext to reclaim storage by unmapping.
- [BlockRange](../blockrange.md)
  A structure that represents a range of blocks.
- [DoAsyncSynchronize](./doasyncsynchronize.md)
  Forces the hardware buffer to flush data blocks to the media.
- [DoAsyncEjectMedia](./doasyncejectmedia.md)
  Ejects the media.
- [Complete](./complete.md)
  Indicates that the dext completed an asynchronous call.
- [DoAsyncReadWrite](./doasyncreadwrite.md)
  Starts an asynchronous read or write operation.
- [IOUserStorageOptions](../iouserstorageoptions.md)
  Options that affect the performance of read-write operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/completeio)*