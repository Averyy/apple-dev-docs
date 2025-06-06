# IOUserSCSIPeripheralDeviceType05

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: class

A DriverKit provider object that works with type 05 devices, those that use SCSI Multimedia Commands (SMC).

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
class IOUserSCSIPeripheralDeviceType05;
```

#### Overview

Subclass this class to create a driver for multimedia devices, such as CD-ROM and DVD-ROM peripherals. In your subclass, override all pure virtual methods.

Use the functions in [`SCSI commands`](scsi-commands.md) to populate Command Descriptor Blocks (CDBs) that you send to the device with [`UserSendCDB`](iouserscsiperipheraldevicetype05/usersendcdb.md).

## Topics

### Managing the device
- [UserInitializeDeviceSupport](iouserscsiperipheraldevicetype05/userinitializedevicesupport.md)
  Performs enumeration-time initializations in response to a call from the framework.
- [UserResetDevice](iouserscsiperipheraldevicetype05/userresetdevice.md)
  Performs a bus reset of the external drive.
### Sending commands to the device
- [UserSendCDB](iouserscsiperipheraldevicetype05/usersendcdb.md)
  Sends a vendor-specific Command Descriptor Block (CDB) to the device.
- [SCSIType05OutParameters](scsitype05outparameters.md)
  Parameters for commands to send to the external SCSI device.
- [SCSIType05OutVersion](scsitype05outversion.md)
  Constants that represent versions of the type 05 outbound interface.
- [SCSIType05InParameters](scsitype05inparameters.md)
  Parameters for responses from the external SCSI device.
- [SCSIType05InVersion](scsitype05inversion.md)
  Constants that represent versions of the type 05 inbound interface.
### Suspending and resuming services
- [UserSuspendServices](iouserscsiperipheraldevicetype05/usersuspendservices.md)
  Suspends services and allows the dext to communicate with the external drive.
- [UserResumeServices](iouserscsiperipheraldevicetype05/userresumeservices.md)
  Resumes normal services after a suspension.
### Providing device metadata
- [UserReportMediumBlockSize](iouserscsiperipheraldevicetype05/userreportmediumblocksize.md)
  Provides a report on the external device’s block size.

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)

## See Also

- [IOUserSCSIPeripheralDeviceType00](iouserscsiperipheraldevicetype00.md)
  A DriverKit provider object that works with type 00 devices, those that use SCSI Block Commands (SBC).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05)*