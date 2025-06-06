# DriverKit Audio Family

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the device supports audio functionality.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 12.0+

#### Discussion

Add this entitlement to the default entitlements file that Xcode creates for your driver project.

## See Also

- [com.apple.developer.driverkit.family.block-storage-device](entitlements/com.apple.developer.driverkit.family.block-storage-device.md)
  A Boolean value that indicates whether to match the driver against block storage devices that use custom drivers.
- [com.apple.developer.driverkit.family.midi](entitlements/com.apple.developer.driverkit.family.midi.md)
  A Boolean value that indicates whether to match the driver against devices that support MIDI.
- [com.apple.developer.driverkit.family.networking](entitlements/com.apple.developer.driverkit.family.networking.md)
  A Boolean value that indicates whether to match the driver against devices that communicate using networking protocols.
- [com.apple.developer.driverkit.family.scsicontroller](entitlements/com.apple.developer.driverkit.family.scsicontroller.md)
  A Boolean value that indicates whether to match the driver against devices with SCSI controllers.
- [com.apple.developer.driverkit.family.serial](entitlements/com.apple.developer.driverkit.family.serial.md)
  A Boolean value that indicates whether to match the driver against devices with serial communication interfaces.
- [com.apple.developer.driverkit.transport.pci](entitlements/com.apple.developer.driverkit.transport.pci.md)
  An array of PCI device descriptors that your custom driver supports.
- [com.apple.developer.driverkit.transport.usb](entitlements/com.apple.developer.driverkit.transport.usb.md)
  An array of dictionaries that identify the USB devices the driver supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.family.audio)*