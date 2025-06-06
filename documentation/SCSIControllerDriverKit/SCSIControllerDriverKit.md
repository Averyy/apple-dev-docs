# SCSIControllerDriverKit

**Framework**: Scsicontrollerdriverkit  
**Kind**: module

Develop drivers for SCSI protocol-based devices.

**Availability**:
- DriverKit 20.4+

#### Overview

The SCSIControllerDriverKit framework supports the development of DriverKit extension (dext) drivers for devices that communicate using SCSI protocols.

Develop your driver by subclassing [`IOUserSCSIParallelInterfaceController`](iouserscsiparallelinterfacecontroller.md), overriding all methods the framework declares as pure virtual. Then package your driver in an app that uses the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade the driver on the user’s Mac.

> **Note**:  SCSIControllerDriverKit is available on macOS.

## Topics

### Essentials
- [com.apple.developer.driverkit.family.scsicontroller](../BundleResources/Entitlements/com.apple.developer.driverkit.family.scsicontroller.md)
  A Boolean value that indicates whether to match the driver against devices with SCSI controllers.
### Samples
- [DriverKit sample code](../DriverKit/driverkit-sample-code.md)
  Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.
### Driver Interfaces
- [IOUserSCSIParallelInterfaceController](iouserscsiparallelinterfacecontroller.md)
  A DriverKit provider object that manages communications with SCSI-based devices.
### Macros
- [Macros](scsicontrollerdriverkit-macros.md)
- [kMaxBundledParallelTasks](kmaxbundledparalleltasks.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/SCSIControllerDriverKit)*