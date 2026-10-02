# SCSIType07OutParameters

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: struct

Parameters for commands to send to the external SCSI device.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
struct SCSIType07OutParameters;
```

#### Discussion

This type contains all the fields from [`SCSIDeviceOutParameters`](scsideviceoutparameters.md), typed for use only with [`IOUserSCSIPeripheralDeviceType07`](iouserscsiperipheraldevicetype07.md) devices.

## Relationships

### Inherits From
- [SCSIDeviceOutParameters](scsideviceoutparameters.md)

## See Also

- [UserSendCDB](iouserscsiperipheraldevicetype07/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType07OutVersion](scsitype07outversion.md)
  Constants that represent versions of the Type05 outbound interface.
- [SCSIType07InParameters](scsitype07inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType07InVersion](scsitype07inversion.md)
  Constants that represent versions of the Type07 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsitype07outparameters)*