# UserSendCDB

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method

Sends a vendor-specific Command Descriptor Block (CDB) to the device.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
virtual kern_return_t UserSendCDB(SCSIType07OutParameters command, SCSIType07InParameters *response);
```

#### Return Value

A value that indicates the result of sending the CDB. [`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Call this method to deliver vendor-specific 16-byte commands to the external drive that this dext matches.

## Parameters

- `command`: A [`SCSIType07OutParameters`](scsitype07outparameters.md) instance that contains the request information.
- `response`: A pointer to a [`SCSIType07InParameters`](scsitype07inparameters.md) instance. On return, the framework fills this object with the response data.

## See Also

- [SCSIType07OutParameters](scsitype07outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType07OutVersion](scsitype07outversion.md)
  Constants that represent versions of the Type05 outbound interface.
- [SCSIType07InParameters](scsitype07inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType07InVersion](scsitype07inversion.md)
  Constants that represent versions of the Type07 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype07/usersendcdb)*