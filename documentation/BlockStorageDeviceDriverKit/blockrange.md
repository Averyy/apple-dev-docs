# BlockRange

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: struct

A structure that represents a range of blocks.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
struct BlockRange;
```

#### Discussion

The pure virtual function `_DoAsyncUnmap`, which your dext must implement, takes this type as a parameter that indicates the blocks to unmap.

## Topics

### Accessing Block Range Properties
- [startBlock](blockrange/startblock.md)
  The address of the first block in this range.
- [numOfBlocks](blockrange/numofblocks.md)
  The number of blocks in this range.

## See Also

- [DoAsyncUnmap](iouserblockstoragedevice/doasyncunmap.md)
  Sends an asynchronous request to the dext to reclaim storage by unmapping.
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

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/blockrange)*