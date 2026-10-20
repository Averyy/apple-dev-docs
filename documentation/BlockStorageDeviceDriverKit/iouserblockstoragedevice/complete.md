# Complete

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method  
**Role**: Instance Method

Indicates that the dext completed an asynchronous call.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual void Complete(uint32_t requestID, kern_return_t status);
```

#### Discussion

The dext calls this method to indicate completion of an asynchronous call to methods like [`DoAsyncUnmap`](./doasyncunmap.md), [`DoAsyncSynchronize`](./doasyncsynchronize.md), or [`DoAsyncEjectMedia`](./doasyncejectmedia.md). Use the `requestID` parameter to determine which call resulted in this callback.

## Parameters

- `requestID`: An opaque identifier, originally provided in the corresponding `DoAsync…` call.
- `status`: The status of the request.

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
- [DoAsyncReadWrite](./doasyncreadwrite.md)
  Starts an asynchronous read or write operation.
- [IOUserStorageOptions](../iouserstorageoptions.md)
  Options that affect the performance of read-write operations.
- [CompleteIO](./completeio.md)
  Indicates that the dext completed an asynchronous read-write call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/complete)*