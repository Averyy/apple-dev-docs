# SCSIType05OutVersion

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: enum

Constants that represent versions of the type 05 outbound interface.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
typedef enum SCSIType05OutVersion : unsigned int { ... } SCSIType05OutVersion;
```

## Topics

### Versions
- [kScsiType05OutCurrentVersion1](scsitype05outversion/kscsitype05outcurrentversion1.md)
  Version 1 of the type 05 outbound interface.

## See Also

- [UserSendCDB](iouserscsiperipheraldevicetype05/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType05OutParameters](scsitype05outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType05InParameters](scsitype05inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType05InVersion](scsitype05inversion.md)
  Constants that represent versions of the type 05 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsitype05outversion)*