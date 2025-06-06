# DoAsyncReadWrite

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method

Starts an asynchronous read or write operation.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t DoAsyncReadWrite(bool isRead, uint32_t requestID, uint64_t dmaAddr, uint64_t size, uint64_t lba, uint64_t numOfBlocks, IOUserStorageOptions options);
```

#### Return Value

A value that indicates the result of the read/write operation. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

When the read or write operation completes, the dext calls your [`CompleteIO`](iouserblockstoragedevice/completeio.md) method with the results of the operation.

## Parameters

- `requestID`: An opaque identifier. After the dext completes the request, it calls   and sends this value as a parameter.
- `dmaAddr`: The DMA address of the data buffer.
- `size`: The size of the data buffer.
- `lba`: The start logical block number.
- `numOfBlocks`: The number of blocks to read or write.
- `options`: Data transfer options. These can be any combination of   values (defined in  ) combined together with the logical   operator.

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
- [IOUserStorageOptions](iouserstorageoptions.md)
  Options that affect the performance of read-write operations.
- [CompleteIO](iouserblockstoragedevice/completeio.md)
  Indicates that the dext completed an asynchronous read-write call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/doasyncreadwrite)*