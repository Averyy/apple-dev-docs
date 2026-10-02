# IOUserSCSIPeripheralDeviceType07

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: class

A DriverKit provider object that works with Type07 devices, those that use extended SCSI Block Commands (SBC) for optical memory devices.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
class IOUserSCSIPeripheralDeviceType07;
```

#### Overview

Subclass this class to create a driver for optical memory devices, such as erasable or rewritable optical disk drives. In your subclass, override all pure virtual methods.

Use the functions in [`SCSI commands`](scsi-commands.md) to populate Command Descriptor Blocks (CDBs) that you send to the device with [`UserSendCDB`](iouserscsiperipheraldevicetype07/usersendcdb.md).

## Topics

### Managing the device
- [UserDetermineDeviceCharacteristics](iouserscsiperipheraldevicetype07/userdeterminedevicecharacteristics.md)
  Performs enumeration-time initializations in response to a call from the framework.
- [UserResetDevice](iouserscsiperipheraldevicetype07/userresetdevice.md)
  Performs a bus reset of the external drive.
### Sending commands to the device
- [UserSendCDB](iouserscsiperipheraldevicetype07/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType07OutParameters](scsitype07outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType07OutVersion](scsitype07outversion.md)
  Constants that represent versions of the Type05 outbound interface.
- [SCSIType07InParameters](scsitype07inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType07InVersion](scsitype07inversion.md)
  Constants that represent versions of the Type07 inbound interface.
### Providing device metadata
- [UserReportMediumBlockSize](iouserscsiperipheraldevicetype07/userreportmediumblocksize.md)
  Provides a report on the external device’s block size.
### Suspending and resuming services
- [UserSuspendServices](iouserscsiperipheraldevicetype07/usersuspendservices.md)
  Suspends services and allows the dext to communicate with the external drive.
- [UserResumeServices](iouserscsiperipheraldevicetype07/userresumeservices.md)
  Resumes normal services after a suspension.

## Relationships

### Inherits From
- [IOService](../driverkit/ioservice.md)

## See Also

- [IOUserSCSIPeripheralDeviceType00](iouserscsiperipheraldevicetype00.md)
  A DriverKit provider object that works with Type00 devices, those that use SCSI Block Commands (SBC).
- [IOUserSCSIPeripheralDeviceType05](iouserscsiperipheraldevicetype05.md)
  A DriverKit provider object that works with Type05 devices, those that use SCSI Multimedia Commands (SMC).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype07)*