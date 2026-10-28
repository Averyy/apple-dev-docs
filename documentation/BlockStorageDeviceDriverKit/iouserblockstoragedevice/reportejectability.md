# ReportEjectability

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the media is ejectable, in response to a call from the framework.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t ReportEjectability(bool *isEjectable);
```

## Return Value

A value that indicates the report-ejectability result. Return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) to inidicate success. To indicate a failure, see [IOKit Constants](../../iokit/iokit_constants.md) for error definitions.

## Parameters

- `isEjectable`: An in/out Boolean parameter. On output, set this to `true` if the hardware supports ejecting the media.

## See Also

### Reporting Device Capabilities
- [ReportRemovability](./reportremovability.md)
  Returns a Boolean value that indicates whether the media is removable, in response to a call from the framework.
- [ReportWriteProtection](./reportwriteprotection.md)
  Returns a Boolean value that indicates whether the media is write protected, in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/reportejectability)*