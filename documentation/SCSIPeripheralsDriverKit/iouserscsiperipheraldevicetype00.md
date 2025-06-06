# IOUserSCSIPeripheralDeviceType00

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: class

A DriverKit provider object that works with type 00 devices, those that use SCSI Block Commands (SBC).

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
class IOUserSCSIPeripheralDeviceType00;
```

#### Overview

Subclass this class to create a driver for direct-access block devices, such as magnetic disks and solid-state drives. In your subclass, override all pure virtual methods.

Use the functions in [`SCSI commands`](scsi-commands.md) to populate Command Descriptor Blocks (CDBs) that you send to the device with [`UserSendCDB`](iouserscsiperipheraldevicetype00/usersendcdb.md).

## Topics

### Managing the device
- [UserDetermineDeviceCharacteristics](iouserscsiperipheraldevicetype00/userdeterminedevicecharacteristics.md)
  Performs enumeration-time initializations in response to a call from the framework.
- [UserResetDevice](iouserscsiperipheraldevicetype00/userresetdevice.md)
  Performs a bus reset of the external drive.
### Sending commands to the device
- [UserSendCDB](iouserscsiperipheraldevicetype00/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType00OutParameters](scsitype00outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType00OutVersion](scsitype00outversion.md)
  Constants that represent versions of the type 00 outbound interface.
- [SCSIType00InParameters](scsitype00inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType00InVersion](scsitype00inversion.md)
  Constants that represent versions of the type 00 inbound interface.
### Suspending and resuming services
- [UserSuspendServices](iouserscsiperipheraldevicetype00/usersuspendservices.md)
  Suspends services and allows the dext to communicate with the external drive.
- [UserResumeServices](iouserscsiperipheraldevicetype00/userresumeservices.md)
  Resumes normal services after a suspension.
### Providing device metadata
- [UserReportMediumBlockSize](iouserscsiperipheraldevicetype00/userreportmediumblocksize.md)
  Provides a report on the external device’s block size.

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)

## See Also

- [IOUserSCSIPeripheralDeviceType05](iouserscsiperipheraldevicetype05.md)
  A DriverKit provider object that works with type 05 devices, those that use SCSI Multimedia Commands (SMC).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00)*