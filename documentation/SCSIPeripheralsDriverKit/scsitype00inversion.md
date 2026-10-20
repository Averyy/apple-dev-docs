# SCSIType00InVersion

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent versions of the Type00 inbound interface.

**Availability**:
- DriverKit 22.0+

## Declaration

```c
typedef enum SCSIType00InVersion : unsigned int { ... } SCSIType00InVersion;
```

## Topics

### Versions
- [kScsiType00InCurrentVersion1](./scsitype00inversion/kscsitype00incurrentversion1.md)
  Version 1 of the Type00 inbound interface.

## See Also

### Sending commands to the device
- [UserSendCDB](./iouserscsiperipheraldevicetype00/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType00OutParameters](./scsitype00outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType00OutVersion](./scsitype00outversion.md)
  Constants that represent versions of the Type00 outbound interface.
- [SCSIType00InParameters](./scsitype00inparameters.md)
  Parameters for responses from the external SCSI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsitype00inversion)*