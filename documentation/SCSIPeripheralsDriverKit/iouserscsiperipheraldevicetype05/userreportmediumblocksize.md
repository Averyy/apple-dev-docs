# UserReportMediumBlockSize

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method  
**Role**: Instance Method

Provides a report on the external device’s block size.

**Availability**:
- DriverKit 22.0+

## Declaration

```cpp
virtual kern_return_t UserReportMediumBlockSize(UInt64 *blockSize);
```

#### Return Value

A value that indicates the result of the report request. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

#### Discussion

This call populates `blockSize` with the granularity of the block size, such as 512 bytes or 4096 bytes (4 KB).

## Parameters

- `blockSize`: On return, the external device’s block size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05/userreportmediumblocksize)*