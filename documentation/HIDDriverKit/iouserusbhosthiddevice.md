# IOUserUSBHostHIDDevice

**Framework**: HIDDriverKit  
**Kind**: class

A provider object for USB devices that support HID interactions.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
class IOUserUSBHostHIDDevice;
```

#### Overview

An `IOUserUSBHostHIDDevice` object is a fully functional provider object that represents a USB-based HID device. Typically, you don’t create `IOUserUSBHostHIDDevice` objects directly. Instead, you specify that your driver relies on an `IOUserUSBHostHIDDevice` as its provider, and the system creates the interface object for you during the matching process.

When implementing a custom driver, use this provider object to manage the connection to the underlying device. Specifically, use it to get reports from the device and to manage the device’s configuration. For example, use the object to configure the USB device’s idle policy.

Subclass `IOUserUSBHostHIDDevice` only when you want to customize the interactions with the USB device. For example, you might use a custom subclass to initialize the USB device in a particular way or support a custom transport mechanism. You can also use a custom subclass to perform additional processing on the report data.

##### Specify the Drivers Personality Information

When you subclass `IOUserUSBHostHIDDevice`, update the `IOKitPersonalities` key of your driver extension’s `Info.plist` file with information to match your driver to appropriate hardware. For this class, always include the keys and values in the following table.

| Key | Discussion |
| --- | --- |
| `IOClass` | The value `AppleUserHIDDevice`. |
| `IOProviderClass` | The provider class information. For a USB-based HID device, specify [`IOUSBHostInterface`](https://developer.apple.com/documentation/USBDriverKit/IOUSBHostInterface). |
| `IOUserClass` | The name of your custom subclass. |
| [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier) | The bundle identifier of your driver. |

You may add other keys to assist with the matching process. For example, you might include the `VendorID`, `ProductID`, `PrimaryUsagePage`, and `PrimaryUsage` keys to match against specific USB devices and HID usage types. The USB specification defines which keys to include when matching your driver to a USB device. For information about the specific key combinations, see  at [`https://www.usb.org`](https://developer.apple.comhttps://www.usb.org).

## Topics

### Running the Service
- [init](iouserusbhosthiddevice/init.md)
  Handles the basic initialization of the event service.
- [Start](iouserusbhosthiddevice/start.md)
  Starts the current device service and associates it with the specified provider object.
- [handleStart](iouserusbhosthiddevice/handlestart.md)
  Performs any custom initialization associated with starting the device service.
- [Stop](iouserusbhosthiddevice/stop.md)
  Stops the device service associated with the specified provider.
- [free](iouserusbhosthiddevice/free.md)
  Performs any final cleanup for the service.
### Getting the Device Description
- [newDeviceDescription](iouserusbhosthiddevice/newdevicedescription.md)
  Creates and returns a new dictionary that describes the HID device.
### Managing Device Reports
- [newReportDescriptor](iouserusbhosthiddevice/newreportdescriptor.md)
  Returns the data in the HID device’s report descriptor.
- [getReport](iouserusbhosthiddevice/getreport-6stqs.md)
  Gets a report from the HID device.
- [getReport](iouserusbhosthiddevice/getreport-2v8zk.md)
  Gets a report from the HID device.
- [setReport](iouserusbhosthiddevice/setreport.md)
  Sends a report to the HID device.
- [initInputReport](iouserusbhosthiddevice/initinputreport.md)
  Starts reading the input report from the device.
- [CompleteInputReport](iouserusbhosthiddevice/completeinputreport.md)
  Processes the results of an asynchronous request for an input report.
- [scheduleInputReportRetry](iouserusbhosthiddevice/scheduleinputreportretry.md)
  Retries a previous request for an input report.
- [cancelInputReportRetry](iouserusbhosthiddevice/cancelinputreportretry.md)
  Cancels a retry attempt for an input report request.
- [TimerOccurred](iouserusbhosthiddevice/timeroccurred.md)
  Handles timeout-related actions when retrying input report requests.
### Configuring the Device
- [setProtocol](iouserusbhosthiddevice/setprotocol.md)
  Sets the active protocol to use for communicating with the USB device.
- [setIdle](iouserusbhosthiddevice/setidle.md)
  Sets the device’s idle time.
- [setIdlePolicy](iouserusbhosthiddevice/setidlepolicy.md)
  Sets the amount of idle time that must pass before suspending the device.
- [setProperty](iouserusbhosthiddevice/setproperty.md)
  Updates the specified property on the corresponding kernel object.
- [reset](iouserusbhosthiddevice/reset.md)
  Resets the USB device.
- [USBIdlePolicyType](usbidlepolicytype.md)
  Constants that specify whether to apply the idle policy to an interface or pipe.
### Configuring Private Settings
- [initPipes](iouserusbhosthiddevice/initpipes.md)
- [getHIDDescriptorInfo](iouserusbhosthiddevice/gethiddescriptorinfo.md)
- [CompleteZLP](iouserusbhosthiddevice/completezlp.md)
- [copyStringAtIndex](iouserusbhosthiddevice/copystringatindex.md)
### Instance Methods
- [CompleteOutputReport](iouserusbhosthiddevice/completeoutputreport.md)
- [CompleteOutputRequest](iouserusbhosthiddevice/completeoutputrequest.md)
- [getAction](iouserusbhosthiddevice/getaction.md)
- [isBulkPipeSupported](iouserusbhosthiddevice/isbulkpipesupported.md)
- [returnAction](iouserusbhosthiddevice/returnaction.md)

## Relationships

### Inherits From
- [IOUserHIDDevice](iouserhiddevice.md)

## See Also

- [com.apple.developer.driverkit.family.hid.device](../BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.device.md)
  A Boolean value that indicates whether the driver provides a HID-related service to the system.
- [IOHIDInterface](iohidinterface.md)
  A provider object for a HID device’s interface.
- [IOUserHIDDevice](iouserhiddevice.md)
  A provider object for devices that support interactions with users.
- [IOHIDDevice](iohiddevice.md)
  An object containing the low-level behavior for all HID device providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice)*