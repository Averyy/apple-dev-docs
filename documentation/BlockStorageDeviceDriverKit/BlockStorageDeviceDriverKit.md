# BlockStorageDeviceDriverKit

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: module  
**Role**: Framework

Develop drivers for custom storage devices that communicate with the driver using custom protocols.

**Availability**:
- DriverKit 21.0+

## Overview

Use `BlockStorageDeviceDriverKit` in conjunction with frameworks like [PCIDriverKit](../PCIDriverKit/PCIDriverKit.md) to create drivers that can communicate with their hardware using custom storage interconnect protocols.

Develop your driver by subclassing [`IOUserBlockStorageDevice`](./iouserblockstoragedevice.md) and overriding all methods the framework declares as C++ pure virtual. Then package your driver in an app that uses the [System Extensions](../SystemExtensions/SystemExtensions.md) framework to install and upgrade the driver on the user’s Mac.

> **Note**:  BlockStorageDeviceDriverKit is available on macOS.

## Topics

### Essentials
- [com.apple.developer.driverkit.family.block-storage-device](../BundleResources/entitlements/com.apple.developer.driverkit.family.block-storage-device.md)
  A Boolean value that indicates whether to match the driver against block storage devices that use custom drivers.
### Driver Interfaces
- [IOUserBlockStorageDevice](./iouserblockstoragedevice.md)
  A DriverKit provider object that manages communications with a block storage device.
### Macros
- [kMaxDeviceStringLength](./kmaxdevicestringlength.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/BlockStorageDeviceDriverKit)*