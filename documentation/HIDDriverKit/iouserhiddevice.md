# IOUserHIDDevice

**Framework**: Hiddriverkit  
**Kind**: class

A provider object for devices that support interactions with users.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
class IOUserHIDDevice;
```

#### Overview

An `IOUserHIDDevice` represents a low-level interface for managing your HID device’s hardware. Subclass `IOUserHIDDevice` when you need to initialize your hardware or set up its transport layer in a specific way. This class provides only basic information about the device, and you are responsible for managing most interactions.

> **Note**:  Subclass [`IOUserUSBHostHIDDevice`](iouserusbhosthiddevice.md), instead of this class, when you want to customize Apple’s default implementation for USB-based HID devices.

##### Specify the Drivers Personality Information

When you subclass `IOUserHIDDevice`, update the `IOKitPersonalities` key of your driver extension’s `Info.plist` file with information to match your driver to appropriate hardware. For this class, always include the keys and values in the following table.

| Key | Discussion |
| --- | --- |
| `IOClass` | The value `AppleUserHIDDevice`. |
| `IOProviderClass` | The provider class information. For a USB-based HID device, specify [`IOUSBHostInterface`](https://developer.apple.com/documentation/USBDriverKit/IOUSBHostInterface). |
| `IOUserClass` | The name of your custom subclass. |
| [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier) | The bundle identifier of your driver. |

You may add other keys to assist with the matching process. For example, you might include the `VendorID`, `ProductID`, `PrimaryUsagePage`, and `PrimaryUsage` keys to match against specific USB devices and HID usage types. The USB specification defines which keys to include when matching your driver to a USB device. For information about the specific key combinations, see  at [`https://www.usb.org`](https://developer.apple.comhttps://www.usb.org).

## Topics

### Running the Service
- [handleStart](iouserhiddevice/handlestart.md)
  Performs any custom initialization associated with starting the device service.
- [Start](iouserhiddevice/start.md)
  Starts the device service and associates it with the specified provider object.
### Getting the Device Description
- [newDeviceDescription](iouserhiddevice/newdevicedescription.md)
  Creates and returns a new dictionary that describes the HID device.
### Managing Device Reports
- [newReportDescriptor](iouserhiddevice/newreportdescriptor.md)
  Returns the data in the HID device’s report descriptor.

## Relationships

### Inherits From
- [IOHIDDevice](iohiddevice.md)
### Inherited By
- [IOUserUSBHostHIDDevice](iouserusbhosthiddevice.md)

## See Also

- [com.apple.developer.driverkit.family.hid.device](../BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.device.md)
  A Boolean value that indicates whether the driver provides a HID-related service to the system.
- [IOHIDInterface](iohidinterface.md)
  A provider object for a HID device’s interface.
- [IOUserUSBHostHIDDevice](iouserusbhosthiddevice.md)
  A provider object for USB devices that support HID interactions.
- [IOHIDDevice](iohiddevice.md)
  An object containing the low-level behavior for all HID device providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/HIDDriverKit/iouserhiddevice)*