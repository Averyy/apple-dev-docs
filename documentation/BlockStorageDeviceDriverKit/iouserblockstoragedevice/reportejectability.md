# ReportEjectability

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method

Returns a Boolean value that indicates whether the media is ejectable, in response to a call from the framework.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t ReportEjectability(bool * isEjectable);
```

#### Return Value

A value that indicates the report-ejectability result. Return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) to inidicate success. To indicate a failure, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants) for error definitions.

## Parameters

- `isEjectable`: An in/out Boolean parameter. On output, set this to   if the hardware supports ejecting the media.

## See Also

- [ReportRemovability](iouserblockstoragedevice/reportremovability.md)
  Returns a Boolean value that indicates whether the media is removable, in response to a call from the framework.
- [ReportWriteProtection](iouserblockstoragedevice/reportwriteprotection.md)
  Returns a Boolean value that indicates whether the media is write protected, in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/reportejectability)*