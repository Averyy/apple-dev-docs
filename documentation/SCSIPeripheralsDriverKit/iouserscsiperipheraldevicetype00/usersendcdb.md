# UserSendCDB

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method

Sends a vendor-specific Command Descriptor Block (CDB) to the device.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
virtual kern_return_t UserSendCDB(SCSIType00OutParameters command, SCSIType00InParameters *response);
```

#### Return Value

A value that indicates the result of sending the CDB. [`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) indicates success. [`kIOReturnNotPrivileged`](https://developer.apple.com/documentation/driverkit/kioreturnnotprivileged) means that exclusive access isn’t available. [`kIOReturnBadArgument`](https://developer.apple.com/documentation/driverkit/kioreturnbadargument) indicates that the command provided bad arguments. For all other error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Call this method to deliver vendor-specific 16-byte commands to the external drive that this dext matches.

The dext class can call this method to send a custom 16-byte CDB to the device. You need to obtain exclusive access to send vendor-specific commands, those with an opcode between `0xC0` and `0xFF`. To manage exclusive access, use the `UserSuspendServices` and `UserResumeServices` APIs. If the command fails with a check condition status, these APIs return the sense data, but only if the caller provided a valid sense buffer in [`SCSIType00OutParameters`](scsitype00outparameters.md).

For ATA passthrough commands, the API uses Descriptor format sense data, with an ATA Status Return Descriptor. Have your dext class set the [`fSenseLengthRequested`](scsideviceoutparameters/fsenselengthrequested.md) field in [`SCSIType00OutParameters`](scsitype00outparameters.md) to 22 bytes; this represents 8 bytes for the Descriptor format sense data and 14 bytes for the ATA Status Return Descriptor. For all other commands, the API uses Fixed format sense data. In these cases, have your dext class set [`fSenseLengthRequested`](scsideviceoutparameters/fsenselengthrequested.md) to 18 bytes. These APIs fail if the sense buffer is larger than 22 bytes.

## Parameters

- `command`: A [`SCSIType00OutParameters`](scsitype00outparameters.md) instance that contains the request information.
- `response`: A pointer to a [`SCSIType00InParameters`](scsitype00inparameters.md) instance. On return, the framework fills this object with the response data.

## See Also

- [SCSIType00OutParameters](scsitype00outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType00OutVersion](scsitype00outversion.md)
  Constants that represent versions of the Type00 outbound interface.
- [SCSIType00InParameters](scsitype00inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType00InVersion](scsitype00inversion.md)
  Constants that represent versions of the Type00 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00/usersendcdb)*