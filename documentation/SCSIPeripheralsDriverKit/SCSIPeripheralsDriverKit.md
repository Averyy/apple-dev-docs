# SCSIPeripheralsDriverKit

**Framework**: Scsiperipheralsdriverkit  
**Kind**: module

Develop drivers for peripherals that use SCSI Block Command and Multimedia Command protocols.

**Availability**:
- DriverKit 22.0+

#### Overview

The SCSIPeripheralsDriverKit framework supports the development of drivers for external devices that communicate using SCSI protocols. This framework operates at the logical unit level. For block-level driver development, use [`BlockStorageDeviceDriverKit`](https://developer.apple.com/documentation/BlockStorageDeviceDriverKit). For protocol-level driver development, use [`SCSIControllerDriverKit`](https://developer.apple.com/documentation/SCSIControllerDriverKit).

Develop your driver by subclassing [`IOUserSCSIPeripheralDeviceType00`](iouserscsiperipheraldevicetype00.md) or [`IOUserSCSIPeripheralDeviceType05`](iouserscsiperipheraldevicetype05.md), depending on whether your device works with SCSI Block Commands (SBC) or SCSI Multimedia Commands (SMC), respectively. In your subclass, override all methods the framework declares as pure virtual. Then package your driver in an app that uses the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade the driver on the user’s Mac.

> **Note**:  SCSIPeripheralsDriverKit is available on macOS.

## Topics

### Driver interfaces
- [IOUserSCSIPeripheralDeviceType00](iouserscsiperipheraldevicetype00.md)
  A DriverKit provider object that works with type 00 devices, those that use SCSI Block Commands (SBC).
- [IOUserSCSIPeripheralDeviceType05](iouserscsiperipheraldevicetype05.md)
  A DriverKit provider object that works with type 05 devices, those that use SCSI Multimedia Commands (SMC).
### Device commands
- [SCSI commands](scsi-commands.md)
  Call the framework’s free functions to populate Command Descriptor Blocks (CDBs) to send to your peripheral.
### Classes
- [IOUserSCSIPeripheralDeviceType07](iouserscsiperipheraldevicetype07.md)
### Reference
- [SCSIPeripheralsDriverKit Enumerations](scsiperipheralsdriverkit-enumerations.md)
- [SCSIPeripheralsDriverKit Data Types](scsiperipheralsdriverkit-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/SCSIPeripheralsDriverKit)*