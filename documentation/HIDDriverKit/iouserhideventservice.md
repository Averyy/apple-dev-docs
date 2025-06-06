# IOUserHIDEventService

**Framework**: HIDDriverKit  
**Kind**: class

A service that parses HID report data into elements that you can use to dispatch events.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
class IOUserHIDEventService;
```

#### Overview

Subclass `IOUserHIDEventService` when you want to process incoming data from a HID device before dispatching it to the system. An event service collects the report from a device, parses it into individual data elements, and dispatches events based on the information in those elements. Create a custom event service when you need to synthesize custom event data, or when you need to process the existing data before dispatching the corresponding events.

To implement a custom event service, override the [`handleReport`](iouserhideventservice/handlereport.md) method and use it to iterate over the report contents and dispatch any relevant events. To get the report data, call the [`getElements`](iouserhideventservice/getelements.md) method each time a new report arrives. (Also call that method in your service’s [`Start`](iouserhideventservice/start.md) method to create the elements initially.) The method returns a set of [`IOHIDElement`](iohidelement.md) objects that contain a parsed version of the report data. Each time you call the method, the system updates the elements to incorporate the data from the latest report.

##### Specify the Drivers Personality Information

When you subclass `IOUserHIDEventService`, update the `IOKitPersonalities` key of your driver extension’s `Info.plist` file with information to match your driver to appropriate hardware. For this class, always include the keys and values in the following table.

| Key | Discussion |
| --- | --- |
| `IOClass` | The value `AppleUserHIDEventService`. |
| `IOProviderClass` | The provider class information. For HID interfaces, specify [`IOHIDInterface`](iohidinterface.md). |
| `IOUserClass` | The name of your custom subclass. |
| [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier) | The bundle identifier of your driver. |

You may add other keys to assist with the matching process. For example, you might include the `VendorID`, `ProductID`, `PrimaryUsagePage`, and `PrimaryUsage` keys to match against specific USB devices and HID usage types. The USB specification defines which keys to include when matching your driver to a USB device. For information about the specific key combinations, see  at [`https://www.usb.org`](https://developer.apple.comhttps://www.usb.org).

## Topics

### Running the Service
- [init](iouserhideventservice/init.md)
  Handles the basic initialization of the event service.
- [Start](iouserhideventservice/start.md)
  Starts the current event service and associates it with the specified provider object.
- [handleStart](iouserhideventservice/handlestart.md)
  Performs additional initialization during the startup of the event service.
- [Stop](iouserhideventservice/stop.md)
  Stops the event service associated with the specified provider.
- [free](iouserhideventservice/free.md)
  Performs any final cleanup for the service.
### Responding to Input Reports
- [getElements](iouserhideventservice/getelements.md)
  Returns an array of elements that contain the parsed data from the HID device’s report.
- [handleReport](iouserhideventservice/handlereport.md)
  Converts an incoming device report into dispatchable events.
- [ReportAvailable](iouserhideventservice/reportavailable.md)
  Notifies the event service that an updated report is available from the HID device.
### Dispatching Events to the System
- [dispatchDigitizerStylusEvent](iouserhideventservice/dispatchdigitizerstylusevent.md)
  Dispatches a digitizer stylus event to the system.
- [dispatchDigitizerTouchEvent](iouserhideventservice/dispatchdigitizertouchevent.md)
  Dispatches a digitizer touch event to the system.
### Checking the Supported Usage
- [conformsTo](iouserhideventservice/conformsto.md)
  Returns a Boolean value that indicates whether the service conforms to the specified HID usage and page information.
### Performing Private Tasks
- [createReportPool](iouserhideventservice/createreportpool.md)
- [dispatchEvent](iouserhideventservice/dispatchevent.md)
  Dispatches a HID event to the system.
### Instance Methods
- [SetLEDState](iouserhideventservice/setledstate.md)
- [SetProperties](iouserhideventservice/setproperties.md)
- [dispatchExtendedGameControllerEvent](iouserhideventservice/dispatchextendedgamecontrollerevent.md)
- [dispatchExtendedGameControllerEventWithOptionalButtons](iouserhideventservice/dispatchextendedgamecontrollereventwithoptionalbuttons.md)
- [dispatchStandardGameControllerEvent](iouserhideventservice/dispatchstandardgamecontrollerevent.md)
- [processReport](iouserhideventservice/processreport.md)

## Relationships

### Inherits From
- [IOHIDEventService](iohideventservice.md)
### Inherited By
- [IOUserHIDEventDriver](iouserhideventdriver.md)

## See Also

- [com.apple.developer.driverkit.family.hid.eventservice](../BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.eventservice.md)
  A Boolean value that indicates whether the driver provides a HID-related event service to the system.
- [IOUserHIDEventDriver](iouserhideventdriver.md)
  A complete driver object that dispatches keyboard, digitizer, scrolling, and pointer events originating from a HID device.
- [IOHIDEventService](iohideventservice.md)
  The base class for implementing a device or operating system service that dispatches events to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice)*