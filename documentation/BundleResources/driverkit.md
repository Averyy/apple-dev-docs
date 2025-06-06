# DriverKit

**Framework**: Bundle Resources

Develop device drivers in macOS and iPadOS.

## Topics

### Essentials
- [com.apple.developer.driverkit](entitlements/com.apple.developer.driverkit.md)
  A Boolean value that indicates whether your extension has permission to run as a user-space driver.
### DriverKit family entitlements
- [DriverKit Audio Family](entitlements/com.apple.developer.driverkit.family.audio.md)
  A Boolean value that indicates whether the device supports audio functionality.
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
### User client entitlements
- [com.apple.developer.driverkit.userclient-access](entitlements/com.apple.developer.driverkit.userclient-access.md)
  An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [com.apple.developer.driverkit.allow-any-userclient-access](entitlements/com.apple.developer.driverkit.allow-any-userclient-access.md)
  A Boolean value that determines whether a macOS driver accepts user client connections from any application.
- [Communicates with Drivers](entitlements/com.apple.developer.driverkit.communicates-with-drivers.md)
  A Boolean value that indicates whether an iPadOS app can communicate with drivers.
- [DriverKit Allow Third Party User Clients](entitlements/com.apple.developer.driverkit.allow-third-party-userclients.md)
  A Boolean value that indicates whether an iPadOS driver accepts calls from third-party user clients.

## See Also

- [System Extensions](system-extensions.md)
  Extend the capabilities of macOS from user space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/driverkit)*