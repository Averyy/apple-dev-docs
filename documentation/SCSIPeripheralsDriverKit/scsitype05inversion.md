# SCSIType05InVersion

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: enum

Constants that represent versions of the type 05 inbound interface.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
typedef enum SCSIType05InVersion : unsigned int { ... } SCSIType05InVersion;
```

## Topics

### Versions
- [kScsiType05InCurrentVersion1](scsitype05inversion/kscsitype05incurrentversion1.md)
  Version 1 of the type 05 inbound interface.

## See Also

- [UserSendCDB](iouserscsiperipheraldevicetype05/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType05OutParameters](scsitype05outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType05OutVersion](scsitype05outversion.md)
  Constants that represent versions of the type 05 outbound interface.
- [SCSIType05InParameters](scsitype05inparameters.md)
  Parameters for responses from the external SCSI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsitype05inversion)*