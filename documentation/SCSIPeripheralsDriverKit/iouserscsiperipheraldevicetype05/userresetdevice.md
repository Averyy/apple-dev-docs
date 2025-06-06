# UserResetDevice

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method

Performs a bus reset of the external drive.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
kern_return_t UserResetDevice(SCSIServiceResponse * response);
```

#### Return Value

A value that indicates the result of the bus reset. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

## Parameters

- `response`: A pointer to a   instance. On return, the framework populates this reference with the response from the protocol driver.

## See Also

- [UserInitializeDeviceSupport](iouserscsiperipheraldevicetype05/userinitializedevicesupport.md)
  Performs enumeration-time initializations in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05/userresetdevice)*