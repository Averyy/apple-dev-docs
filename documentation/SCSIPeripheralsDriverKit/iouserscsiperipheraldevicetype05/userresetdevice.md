# UserResetDevice

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method  
**Role**: Instance Method

Performs a bus reset of the external drive.

**Availability**:
- DriverKit 22.0+

## Declaration

```cpp
virtual kern_return_t UserResetDevice(SCSIServiceResponse *response);
```

#### Return Value

A value that indicates the result of the bus reset. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

## Parameters

- `response`: A pointer to a [`SCSIServiceResponse`](../../iokit/scsiserviceresponse.md) instance. On return, the framework populates this reference with the response from the protocol driver.

## See Also

### Managing the device
- [UserInitializeDeviceSupport](./userinitializedevicesupport.md)
  Performs enumeration-time initializations in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05/userresetdevice)*