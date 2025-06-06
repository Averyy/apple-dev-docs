# UserSendCDB

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method

Sends a vendor-specific Command Descriptor Block (CDB) to the device.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
kern_return_t UserSendCDB(SCSIType00OutParameters command, SCSIType00InParameters * response);
```

#### Return Value

A value that indicates the result of sending the CDB. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Call this method to deliver vendor-specific 16-byte commands to the external drive that this dext matches.

## Parameters

- `command`: A   instance that contains the request information.
- `response`: A pointer to a   instance. On return, the framework fills this object with the response data.

## See Also

- [SCSIType00OutParameters](scsitype00outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType00OutVersion](scsitype00outversion.md)
  Constants that represent versions of the type 00 outbound interface.
- [SCSIType00InParameters](scsitype00inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType00InVersion](scsitype00inversion.md)
  Constants that represent versions of the type 00 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00/usersendcdb)*