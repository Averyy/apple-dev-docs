# com.apple.developer.driverkit.transport.usb

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

An array of dictionaries that identify the USB devices the driver supports.

**Availability**:
- macOS 10.15+

## Details

- **Name**: `com.apple.developer.driverkit.transport.usb` (DriverKit USB Transport)
- **Type**: array of dictionary 

## Discussion

Each element in the array is a dictionary whose keys and values identify a specific type of supported device. The keys in the dictionary correspond to field names of the device descriptor associated with the USB device.

## Topics

### Property List Keys
- [bConfigurationValue](./com.apple.developer.driverkit.transport.usb/bconfigurationvalue.md)
- [bDeviceClass](./com.apple.developer.driverkit.transport.usb/bdeviceclass.md)
- [bDeviceProtocol](./com.apple.developer.driverkit.transport.usb/bdeviceprotocol.md)
- [bDeviceSubClass](./com.apple.developer.driverkit.transport.usb/bdevicesubclass.md)
- [bInterfaceClass](./com.apple.developer.driverkit.transport.usb/binterfaceclass.md)
- [bInterfaceNumber](./com.apple.developer.driverkit.transport.usb/binterfacenumber.md)
- [bInterfaceProtocol](./com.apple.developer.driverkit.transport.usb/binterfaceprotocol.md)
- [bInterfaceSubClass](./com.apple.developer.driverkit.transport.usb/binterfacesubclass.md)
- [bcdDevice](./com.apple.developer.driverkit.transport.usb/bcddevice.md)
- [idProduct](./com.apple.developer.driverkit.transport.usb/idproduct.md)
- [idProductArray](./com.apple.developer.driverkit.transport.usb/idproductarray.md)
- [idProductMask](./com.apple.developer.driverkit.transport.usb/idproductmask.md)
- [idVendor](./com.apple.developer.driverkit.transport.usb/idvendor.md)

## See Also

### DriverKit family entitlements
- [DriverKit Audio Family](./com.apple.developer.driverkit.family.audio.md)
  A Boolean value that indicates whether the device supports audio functionality.
- [com.apple.developer.driverkit.family.block-storage-device](./com.apple.developer.driverkit.family.block-storage-device.md)
  A Boolean value that indicates whether to match the driver against block storage devices that use custom drivers.
- [com.apple.developer.driverkit.family.midi](./com.apple.developer.driverkit.family.midi.md)
  A Boolean value that indicates whether to match the driver against devices that support MIDI.
- [com.apple.developer.driverkit.family.networking](./com.apple.developer.driverkit.family.networking.md)
  A Boolean value that indicates whether to match the driver against devices that communicate using networking protocols.
- [com.apple.developer.driverkit.family.scsicontroller](./com.apple.developer.driverkit.family.scsicontroller.md)
  A Boolean value that indicates whether to match the driver against devices with SCSI controllers.
- [com.apple.developer.driverkit.family.serial](./com.apple.developer.driverkit.family.serial.md)
  A Boolean value that indicates whether to match the driver against devices with serial communication interfaces.
- [com.apple.developer.driverkit.transport.pci](./com.apple.developer.driverkit.transport.pci.md)
  An array of PCI device descriptors that your custom driver supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.transport.usb)*