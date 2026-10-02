# SCSIPeripheralsDriverKit

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: module

Develop drivers for peripherals that use SCSI Block Command and Multimedia Command protocols.

**Availability**:
- DriverKit 22.0+

#### Overview

The SCSIPeripheralsDriverKit framework supports the development of drivers for external devices that communicate using SCSI protocols. This framework operates at the logical unit level. For block-level driver development, use [`BlockStorageDeviceDriverKit`](https://developer.apple.com/documentation/blockstoragedevicedriverkit). For protocol-level driver development, use [`SCSIControllerDriverKit`](https://developer.apple.com/documentation/scsicontrollerdriverkit).

##### Creating a Driver

SCSIPeripheralsDriverKit supports three types of peripherals defined by the SCSI specifications:

- **Type00**: Block storage devices that use SCSI Block Commands (SBC), such as magnetic disks and solid-state drives.
- **Type05**: Multimedia devices that use SCSI Multimedia Commands (SMC), like CD-ROM and DVD-ROM drives.
- **Type07**: Optical memory devices that use an extended version of SBC, such as erasable and rewritable optical disk drives.

Develop your driver by subclassing [`IOUserSCSIPeripheralDeviceType00`](iouserscsiperipheraldevicetype00.md),  [`IOUserSCSIPeripheralDeviceType05`](iouserscsiperipheraldevicetype05.md), or [`IOUserSCSIPeripheralDeviceType07`](iouserscsiperipheraldevicetype07.md), depending on the relevant device type. In your subclass, override all methods the framework declares as pure virtual. Then package your driver in an app that uses the [`System Extensions`](https://developer.apple.com/documentation/systemextensions) framework to install and upgrade the driver on the user’s Mac.

When you subclass [`IOUserSCSIPeripheralDeviceType00`](iouserscsiperipheraldevicetype00.md),  [`IOUserSCSIPeripheralDeviceType05`](iouserscsiperipheraldevicetype05.md), or [`IOUserSCSIPeripheralDeviceType07`](iouserscsiperipheraldevicetype07.md), update the [`IOKitPersonalities`](https://developer.apple.com/documentation/bundleresources/information-property-list/iokitpersonalities) key of your driver extension’s information property list file with information to match your driver to appropriate hardware. For these classes, always include the keys and values in the following table:

| Key | Value |
| --- | --- |
| `CFBundleIDentifier` | The bundle ID of your driver |
| `CFBundleIdentifierKernel` | `com.apple.iokit.IOSCSIBlockCommandsDevice` for Type00 and Type07 or `com.apple.iokit.IOSCSIMultimediaCommandsDevice` for Type05 |
| `IOClass` | `IOUserSCSIPeripheralDeviceType00`, `IOUserSCSIPeripheralDeviceType05`, or `IOUserSCSIPeripheralDeviceType07`, the framework class that containins the base behavior |
| `IOUserClass` | The name of your custom dext class |
| `IOUserServerName` | The bundle identifier of your driver, such as `com.example.dextname` |
| `IOProviderClass` | `IOSCSIPeripheralDeviceNub`, the class that your service requires as its provider object |
| Peripheral device | `0` for Type00,  `5` for Type05, or `7` Type07 |

In addition to these required keys, you can include additional key-value pairs as needed.

The following example shows a minimal entry for the `IOKitPersonalities` key in the information property list for a block device (Type00) driver:

```xml
<key>IOKitPersonalities</key>
 <dict>
     <key>ExampleDext</key>
     </dict>
         <key>CFBundleIdentifierKernel</key>
         <string>com.apple.iokit.IOSCSIBlockCommandsDevice</string>
         <key>CFBundleIdentifier</key>
         <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
         <key>IOClass</key>
         <string>IOUserSCSIPeripheralDeviceType00</string>
         <key>IOProviderClass</key>
         <string>IOSCSIPeripheralDeviceNub</string>
         <key>IOUserClass</key>
         <string>YourDextClassName</string>
         <key>IOUserServerName</key>
         <string>com.example.yourdextname</string>
         <key>Peripheral Device Type</key>
         <integer>0</integer>
     </dict>
 </dict>   
```

> **Note**:  SCSIPeripheralsDriverKit is available on macOS.

## Topics

### Entitlements
- [com.apple.developer.driverkit](../bundleresources/entitlements/com.apple.developer.driverkit.md)
  A Boolean value that indicates whether your extension has permission to run as a user-space driver.
- [com.apple.developer.driverkit.family.scsicontroller](../bundleresources/entitlements/com.apple.developer.driverkit.family.scsicontroller.md)
  A Boolean value that indicates whether to match the driver against devices with SCSI controllers.
### Driver interfaces
- [IOUserSCSIPeripheralDeviceType00](iouserscsiperipheraldevicetype00.md)
  A DriverKit provider object that works with Type00 devices, those that use SCSI Block Commands (SBC).
- [IOUserSCSIPeripheralDeviceType05](iouserscsiperipheraldevicetype05.md)
  A DriverKit provider object that works with Type05 devices, those that use SCSI Multimedia Commands (SMC).
- [IOUserSCSIPeripheralDeviceType07](iouserscsiperipheraldevicetype07.md)
  A DriverKit provider object that works with Type07 devices, those that use extended SCSI Block Commands (SBC) for optical memory devices.
### Device commands
- [SCSI commands](scsi-commands.md)
  Call the framework’s free functions to populate Command Descriptor Blocks (CDBs) to send to your peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SCSIPeripheralsDriverKit)*