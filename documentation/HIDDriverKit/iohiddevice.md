# IOHIDDevice

**Framework**: HIDDriverKit  
**Kind**: class

An object containing the low-level behavior for all HID device providers.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
class IOHIDDevice;
```

#### Overview

`IOHIDDevice` is the abstract base class for provider objects that represent a human interface device. This class defines the basic interface that subclasses use to manage reports. Don’t create instances of this class directly. Instead, subclass [`IOUserHIDDevice`](iouserhiddevice.md) or [`IOUserUSBHostHIDDevice`](iouserusbhosthiddevice.md) to define the behavior of your custom device provider.

## Topics

### Processing Device Reports
- [handleReport](iohiddevice/handlereport.md)
  Handles an asynchronous report received from the HID device.
- [getReport](iohiddevice/getreport.md)
  Gets a report from the HID device.
- [setReport](iohiddevice/setreport.md)
  Sends a report to the HID device.
- [CompleteReport](iohiddevice/completereport.md)
  Completes all async requests made when getting or setting a report.
- [Report Options](report-options-enum.md)
  The enumerated report options.
### Setting Device Properties
- [setProperty](iohiddevice/setproperty.md)
  Updates the specified property on the corresponding kernel object.

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)
### Inherited By
- [IOUserHIDDevice](iouserhiddevice.md)

## See Also

- [com.apple.developer.driverkit.family.hid.device](../BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.device.md)
  A Boolean value that indicates whether the driver provides a HID-related service to the system.
- [IOHIDInterface](iohidinterface.md)
  A provider object for a HID device’s interface.
- [IOUserUSBHostHIDDevice](iouserusbhosthiddevice.md)
  A provider object for USB devices that support HID interactions.
- [IOUserHIDDevice](iouserhiddevice.md)
  A provider object for devices that support interactions with users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddevice)*