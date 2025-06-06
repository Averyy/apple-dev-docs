# com.apple.developer.driverkit.family.block-storage-device

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether to match the driver against block storage devices that use custom drivers.

**Availability**:
- macOS 12.0+

#### Discussion

Add this entitlement to every BlockStorageDeviceDriverKit driver you create. You must request this entitlement from Apple. For information about how to request the entitlement, see [`System Extensions and DriverKit`](https://developer.apple.comhttps://developer.apple.com/system-extensions/).

## See Also

- [DriverKit Audio Family](entitlements/com.apple.developer.driverkit.family.audio.md)
  A Boolean value that indicates whether the device supports audio functionality.
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

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.family.block-storage-device)*