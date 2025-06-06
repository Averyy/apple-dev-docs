# ReportRemovability

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method

Returns a Boolean value that indicates whether the media is removable, in response to a call from the framework.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t ReportRemovability(bool * isRemovable);
```

#### Return Value

A value that indicates the report-removability result. Return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) to inidicate success. To indicate a failure, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants) for error definitions.

## Parameters

- `isRemovable`: An in/out Boolean parameter. On output, set this to   if the hardware supports removable media.

## See Also

- [ReportEjectability](iouserblockstoragedevice/reportejectability.md)
  Returns a Boolean value that indicates whether the media is ejectable, in response to a call from the framework.
- [ReportWriteProtection](iouserblockstoragedevice/reportwriteprotection.md)
  Returns a Boolean value that indicates whether the media is write protected, in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/reportremovability)*