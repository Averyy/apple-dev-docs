# Complete

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method

Indicates that the dext completed an asynchronous call.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
void Complete(uint32_t requestID, kern_return_t status);
```

#### Discussion

The dext calls this method to indicate completion of an asynchronous call to methods like [`DoAsyncUnmap`](iouserblockstoragedevice/doasyncunmap.md), [`DoAsyncSynchronize`](iouserblockstoragedevice/doasyncsynchronize.md), or [`DoAsyncEjectMedia`](iouserblockstoragedevice/doasyncejectmedia.md). Use the `requestID` parameter to determine which call resulted in this callback.

## Parameters

- `requestID`: An opaque identifier, originally provided in the corresponding   call.
- `status`: The status of the request.

## See Also

- [DoAsyncUnmap](iouserblockstoragedevice/doasyncunmap.md)
  Sends an asynchronous request to the dext to reclaim storage by unmapping.
- [BlockRange](blockrange.md)
  A structure that represents a range of blocks.
- [DoAsyncSynchronize](iouserblockstoragedevice/doasyncsynchronize.md)
  Forces the hardware buffer to flush data blocks to the media.
- [DoAsyncEjectMedia](iouserblockstoragedevice/doasyncejectmedia.md)
  Ejects the media.
- [DoAsyncReadWrite](iouserblockstoragedevice/doasyncreadwrite.md)
  Starts an asynchronous read or write operation.
- [IOUserStorageOptions](iouserstorageoptions.md)
  Options that affect the performance of read-write operations.
- [CompleteIO](iouserblockstoragedevice/completeio.md)
  Indicates that the dext completed an asynchronous read-write call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/complete)*