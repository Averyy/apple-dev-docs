# UserReportMediumBlockSize

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method

Provides a report on the external device’s block size.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
kern_return_t UserReportMediumBlockSize(UInt64 * blockSize);
```

#### Return Value

A value that indicates the result of the report request. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

This call populates `blockSize` with the granularity of the block size, such as 512 bytes or 4096 bytes (4 KB).

## Parameters

- `blockSize`: On return, the external device’s block size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05/userreportmediumblocksize)*