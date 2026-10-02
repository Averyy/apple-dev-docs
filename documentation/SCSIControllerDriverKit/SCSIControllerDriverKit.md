# SCSIControllerDriverKit

**Framework**: SCSIControllerDriverKit  
**Kind**: module

Develop drivers for SCSI protocol-based devices.

**Availability**:
- DriverKit 20.4+

#### Overview

The SCSIControllerDriverKit framework supports the development of DriverKit extension (dext) drivers for devices that communicate using SCSI protocols.

Develop your driver by subclassing [`IOUserSCSIParallelInterfaceController`](iouserscsiparallelinterfacecontroller.md), overriding all methods the framework declares as pure virtual. Then package your driver in an app that uses the [`System Extensions`](https://developer.apple.com/documentation/systemextensions) framework to install and upgrade the driver on a Mac.

##### Creating a Driver

When you subclass [`IOUserSCSIParallelInterfaceController`](iouserscsiparallelinterfacecontroller.md), update the [`IOKitPersonalities`](https://developer.apple.com/documentation/bundleresources/information-property-list/iokitpersonalities) key of your driver extension’s information property list file with information to match your driver to appropriate hardware. For this class, always include the keys and values in the following table:

| Key | Value |
| --- | --- |
| `CFBundleIDentifier` | The bundle ID of your driver |
| `CFBundleIdentifierKernel` | `com.apple.iokit.IOSCSIParallelFamily` |
| `IOClass` | `IOUserSCSIParallelInterfaceController`, the framework class that contains the base behavior |
| `IOUserClass` | The name of your custom dext class, a subclass of `IOUserSCSIParallelInterfaceController` |
| `IOUserServerName` | The bundle identifier of your driver, such as `com.example.dextname` |
| `IOProviderClass` | `IOPCIDevice` |

In addition to these required keys, you can include key-value pairs as needed.

The following example shows a minimal entry for the `IOKitPersonalities` key in the information property list:

```xml
<key>IOKitPersonalities</key>
    <dict>
        <key>ExampleDext</key>
        </dict>
            <key>CFBundleIdentifierKernel</key>
            <string>com.apple.iokit.IOSCSIParallelFamily</string>
            <key>CFBundleIdentifier</key>
            <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
            <key>IOClass</key>
            <string>IOUserSCSIParallelInterfaceController</string>
            <key>IOProviderClass</key>
            <string>IOPCIDevice</string>
            <key>IOUserClass</key>
            <string>YourDextClassName</string>
            <key>IOUserServerName</key>
            <string>com.example.dextname</string>
        </dict>
    </dict>
</key>
```

> **Note**:  SCSIControllerDriverKit is available on macOS.

## Topics

### Entitlements
- [com.apple.developer.driverkit](../bundleresources/entitlements/com.apple.developer.driverkit.md)
  A Boolean value that indicates whether your extension has permission to run as a user-space driver.
- [com.apple.developer.driverkit.family.scsicontroller](../bundleresources/entitlements/com.apple.developer.driverkit.family.scsicontroller.md)
  A Boolean value that indicates whether to match the driver against devices with SCSI controllers.
### Samples
- [DriverKit sample code](../driverkit/driverkit-sample-code.md)
  Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.
### Driver interfaces
- [IOUserSCSIParallelInterfaceController](iouserscsiparallelinterfacecontroller.md)
  A DriverKit provider object that manages communications with SCSI-based devices.
### Macros
- [Macros](scsicontrollerdriverkit-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/SCSIControllerDriverKit)*