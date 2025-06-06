# SCSIType00OutVersion

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: enum

Constants that represent versions of the type 00 outbound interface.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
typedef enum SCSIType00OutVersion : unsigned int { ... } SCSIType00OutVersion;
```

## Topics

### Versions
- [kScsiType00OutCurrentVersion1](scsitype00outversion/kscsitype00outcurrentversion1.md)
  Version 1 of the type 00 outbound interface.

## See Also

- [UserSendCDB](iouserscsiperipheraldevicetype00/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType00OutParameters](scsitype00outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType00InParameters](scsitype00inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType00InVersion](scsitype00inversion.md)
  Constants that represent versions of the type 00 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsitype00outversion)*