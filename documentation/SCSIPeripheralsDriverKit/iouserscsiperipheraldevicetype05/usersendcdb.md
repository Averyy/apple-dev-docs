# UserSendCDB

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method  
**Role**: Instance Method

Sends a vendor-specific Command Descriptor Block (CDB) to the device.

**Availability**:
- DriverKit 22.0+

## Declaration

```cpp
virtual kern_return_t UserSendCDB(SCSIType05OutParameters command, SCSIType05InParameters *response);
```

## Return Value

A value that indicates the result of sending the CDB. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

## Discussion

Call this method to deliver vendor-specific 16-byte commands to the external drive that this dext matches.

## Parameters

- `command`: A [`SCSIType05OutParameters`](../scsitype05outparameters.md) instance that contains the request information.
- `response`: A pointer to a [`SCSIType05InParameters`](../scsitype05inparameters.md) instance. On return, the framework fills this object with the response data.

## See Also

### Sending commands to the device
- [SCSIType05OutParameters](../scsitype05outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType05OutVersion](../scsitype05outversion.md)
  Constants that represent versions of the Type05 outbound interface.
- [SCSIType05InParameters](../scsitype05inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType05InVersion](../scsitype05inversion.md)
  Constants that represent versions of the Type05 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05/usersendcdb)*