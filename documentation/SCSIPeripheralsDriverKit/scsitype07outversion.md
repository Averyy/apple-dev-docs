# SCSIType07OutVersion

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: enum

Constants that represent versions of the Type05 outbound interface.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
typedef enum SCSIType07OutVersion : unsigned int { ... } SCSIType07OutVersion;
```

## Topics

### Versions
- [kScsiType07OutCurrentVersion1](scsitype07outversion/kscsitype07outcurrentversion1.md)
  Version 1 of the Type07 outbound interface.

## See Also

- [UserSendCDB](iouserscsiperipheraldevicetype07/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType07OutParameters](scsitype07outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType07InParameters](scsitype07inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType07InVersion](scsitype07inversion.md)
  Constants that represent versions of the Type07 inbound interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsitype07outversion)*