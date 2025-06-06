# IOHIDInterface

**Framework**: HIDDriverKit  
**Kind**: class

A provider object for a HID device’s interface.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
class IOHIDInterface;
```

#### Overview

An `IOHIDInterface` object represents a specific interface of the HID device. Typically, you don’t create `IOHIDInterface` objects directly. Instead, you specify that your driver relies on an `IOHIDInterface` as its provider, and the system creates the interface object for you during the matching process.

To use a HID interface object directly, call [`Open`](iohidinterface/open.md) to create a new session between the interface and your custom driver. When calling that method, you specify an [`OSAction`](https://developer.apple.com/documentation/DriverKit/OSAction) object to execute each time a new report is ready to process. When a new report arrives, the `IOHIDInterface` object parses the device’s report data, puts the data into a set of [`IOHIDElement`](iohidelement.md) objects, and notifies your action object. Use your action object’s [`ReportAvailable`](iohidinterface/reportavailable.md) method to parse the element objects and dispatch events.

## Topics

### Running the Interface
- [init](iohidinterface/init.md)
  Handles the basic initialization of the interface.
- [free](iohidinterface/free.md)
### Managing the Session
- [Open](iohidinterface/open.md)
  Opens a session to the device and begins the delivery of input reports.
- [Close](iohidinterface/close.md)
  Closes the interface and stops the delivery of input reports.
### Getting and Setting Input Reports
- [ReportAvailable](iohidinterface/reportavailable.md)
  Notifies the interface that an updated report is available from the HID device.
- [AddReportToPool](iohidinterface/addreporttopool.md)
  Adds a memory descriptor to the report pool.
- [processReport](iohidinterface/processreport.md)
  Parses the contents of the specified report and updates the interface’s elements.
- [GetReport](iohidinterface/getreport.md)
  Retrieves a new input report from the HID device.
- [SetReport](iohidinterface/setreport.md)
  Sends a report to the HID device.
### Accessing the Elements of a Report
- [getElements](iohidinterface/getelements.md)
  Returns the array of elements that the interface uses to store  parsed report data.
- [commitElements](iohidinterface/commitelements.md)
  Gets or sets the contents of the interface’s stored elements.

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)

## See Also

- [com.apple.developer.driverkit.family.hid.device](../BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.device.md)
  A Boolean value that indicates whether the driver provides a HID-related service to the system.
- [IOUserUSBHostHIDDevice](iouserusbhosthiddevice.md)
  A provider object for USB devices that support HID interactions.
- [IOUserHIDDevice](iouserhiddevice.md)
  A provider object for devices that support interactions with users.
- [IOHIDDevice](iohiddevice.md)
  An object containing the low-level behavior for all HID device providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidinterface)*