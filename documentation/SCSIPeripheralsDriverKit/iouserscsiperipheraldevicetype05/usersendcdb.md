# UserSendCDB

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method

Sends a vendor-specific Command Descriptor Block (CDB) to the device.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
kern_return_t UserSendCDB(SCSIType05OutParameters command, SCSIType05InParameters * response);
```

#### Return Value

A value that indicates the result of sending the CDB. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Call this method to deliver vendor-specific 16-byte commands to the external drive that this dext matches.

## Parameters

- `command`: A   instance that contains the request information.
- `response`: A pointer to a   instance. On return, the framework fills this object with the response data.

## See Also

- [SCSIType05OutParameters](scsitype05outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType05OutVersion](scsitype05outversion.md)
  Constants that represent versions of the type 05 outbound interface.
- [SCSIType05InParameters](scsitype05inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType05InVersion](scsitype05inversion.md)
  Constants that represent versions of the type 05 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05/usersendcdb)*