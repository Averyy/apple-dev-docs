# SCSIType05InParameters

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: struct

Parameters for responses from the external SCSI device.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
struct SCSIType05InParameters;
```

#### Discussion

This type contains all the fields from [`SCSIDeviceInParameters`](scsideviceinparameters.md), typed for use only with [`IOUserSCSIPeripheralDeviceType05`](iouserscsiperipheraldevicetype05.md) devices.

## Relationships

### Inherits From
- [SCSIDeviceInParameters](scsideviceinparameters.md)

## See Also

- [UserSendCDB](iouserscsiperipheraldevicetype05/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType05OutParameters](scsitype05outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType05OutVersion](scsitype05outversion.md)
  Constants that represent versions of the type 05 outbound interface.
- [SCSIType05InVersion](scsitype05inversion.md)
  Constants that represent versions of the type 05 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsitype05inparameters)*