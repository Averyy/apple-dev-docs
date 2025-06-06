# DoAsyncUnmap

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method

Sends an asynchronous request to the dext to reclaim storage by unmapping.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t DoAsyncUnmap(uint32_t requestID, IOMemoryDescriptor * buffer, uint32_t numOfRanges);
```

#### Return Value

A value that indicates the unmap result. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

When the unmap operation completes, the dext calls your [`Complete`](iouserblockstoragedevice/complete.md) method with the results of the operation.

## Parameters

- `requestID`: An opaque identifier. After the dext completes the request, it calls   and sends this value as a parameter.
- `buffer`: A memory buffer containing the block ranges to unmap.
- `numOfRanges`: The number of ranges in  .

## See Also

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
- [CompleteIO](iouserblockstoragedevice/completeio.md)
  Indicates that the dext completed an asynchronous read-write call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/doasyncunmap)*