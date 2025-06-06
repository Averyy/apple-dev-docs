# CompleteIO

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method

Indicates that the dext completed an asynchronous read-write call.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
void CompleteIO(uint32_t requestID, uint64_t bytesTransferred, kern_return_t IOStatus);
```

#### Discussion

The dext calls this method to indicate completion of an asynchronous read-write call. Use the `requestID` parameter to determine which [`DoAsyncReadWrite`](iouserblockstoragedevice/doasyncreadwrite.md) call resulted in this callback.

## Parameters

- `requestID`: An opaque identifier, originally provided in the corresponding   call.
- `bytesTransferred`: The number of bytes transferred.
- `IOStatus`: The status of the request.

## See Also

- [DoAsyncUnmap](iouserblockstoragedevice/doasyncunmap.md)
  Sends an asynchronous request to the dext to reclaim storage by unmapping.
- [BlockRange](blockrange.md)
  A structure that represents a range of blocks.
- [DoAsyncSynchronize](iouserblockstoragedevice/doasyncsynchronize.md)
  Forces the hardware buffer to flush data blocks to the media.
- [DoAsyncEjectMedia](iouserblockstoragedevice/doasyncejectmedia.md)
  Ejects the media.
- [Complete](iouserblockstoragedevice/complete.md)
  Indicates that the dext completed an asynchronous call.
- [DoAsyncReadWrite](iouserblockstoragedevice/doasyncreadwrite.md)
  Starts an asynchronous read or write operation.
- [IOUserStorageOptions](iouserstorageoptions.md)
  Options that affect the performance of read-write operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/completeio)*