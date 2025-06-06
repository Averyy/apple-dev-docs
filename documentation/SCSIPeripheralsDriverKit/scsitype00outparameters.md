# SCSIType00OutParameters

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: struct

Parameters for commands to send to the external SCSI device.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
struct SCSIType00OutParameters;
```

#### Discussion

This type contains all the fields from [`SCSIDeviceOutParameters`](scsideviceoutparameters.md), typed for use only with [`IOUserSCSIPeripheralDeviceType00`](iouserscsiperipheraldevicetype00.md) devices.

## Relationships

### Inherits From
- [SCSIDeviceOutParameters](scsideviceoutparameters.md)

## See Also

- [UserSendCDB](iouserscsiperipheraldevicetype00/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType00OutVersion](scsitype00outversion.md)
  Constants that represent versions of the type 00 outbound interface.
- [SCSIType00InParameters](scsitype00inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType00InVersion](scsitype00inversion.md)
  Constants that represent versions of the type 00 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsitype00outparameters)*