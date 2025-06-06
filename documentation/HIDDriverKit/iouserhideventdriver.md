# IOUserHIDEventDriver

**Framework**: HIDDriverKit  
**Kind**: class

A complete driver object that dispatches keyboard, digitizer, scrolling, and pointer events originating from a HID device.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
class IOUserHIDEventDriver;
```

#### Overview

An `IOUserHIDEventDriver` object is a fully functional driver that handles many common types of HID events. This driver parses incoming reports and uses the information to dispatch many types of events to the system. Apple provides this driver object as a default implementation for devices that conform to the HID specifications and don’t include any custom information that requires a special driver.

You can subclass `IOUserHIDEventDriver` and add support for other types of events. Alternatively, you can subclass [`IOUserHIDEventService`](iouserhideventservice.md) and customize how your event service processes the report data.

##### Specify the Drivers Personality Information

When you subclass [`IOUserHIDEventDriver`](iouserhideventdriver.md), update the `IOKitPersonalities` key of your driver extension’s `Info.plist` file with information to match your driver to appropriate hardware. For this class, always include the keys and values in the following table.

| Key | Discussion |
| --- | --- |
| `IOClass` | The value `AppleUserHIDEventService`. |
| `IOProviderClass` | The provider class information. For HID interfaces, specify [`IOHIDInterface`](iohidinterface.md). |
| `IOUserClass` | The name of your custom subclass. |
| [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier) | The bundle identifier of your driver. |

You may add other keys to assist with the matching process. For example, you might include the `VendorID`, `ProductID`, `PrimaryUsagePage`, and `PrimaryUsage` keys to match against specific USB devices and HID usage types. The USB specification defines which keys to include when matching your driver to a USB device. For information about the specific key combinations, see  at [`https://www.usb.org`](https://developer.apple.comhttps://www.usb.org).

## Topics

### Running the Driver
- [init](iouserhideventdriver/init.md)
  Handles the basic initialization of the event service.
- [Start](iouserhideventdriver/start.md)
  Starts the current event driver and associates it with the specified provider object.
- [free](iouserhideventdriver/free.md)
  Performs any final cleanup for the service.
### Parsing the Element Hierarchy
- [parseElements](iouserhideventdriver/parseelements.md)
  Parses the specified array of elements.
- [parsePointerElement](iouserhideventdriver/parsepointerelement.md)
  Parses an element to see if it supports pointer usages.
- [parseDigitizerElement](iouserhideventdriver/parsedigitizerelement.md)
  Parses an element to see if it supports digitizer usages.
- [parseKeyboardElement](iouserhideventdriver/parsekeyboardelement.md)
  Parses an element to see if it contains keyboard-related information.
- [parseScrollElement](iouserhideventdriver/parsescrollelement.md)
  Parses an element to see if it supports scroll usages.
- [parseLEDElement](iouserhideventdriver/parseledelement.md)
  Parses an element to see if it supports LED usages.
### Handling New Data Reports
- [handleReport](iouserhideventdriver/handlereport.md)
  Processes the information in a new device report and dispatches any relevant events in response.
- [handleKeyboardReport](iouserhideventdriver/handlekeyboardreport.md)
  Iterates through keyboard elements and dispatches them if the element value has been updated.
- [handleRelativePointerReport](iouserhideventdriver/handlerelativepointerreport.md)
  Iterates through relative pointer elements and dispatches them if the element value has been updated.
- [handleAbsolutePointerReport](iouserhideventdriver/handleabsolutepointerreport.md)
  Iterates through absolute pointer elements and dispatches them if the element value has been updated.
- [handleScrollReport](iouserhideventdriver/handlescrollreport.md)
  Iterates through scroll elements and dispatches them if the element value has been updated.
- [handleDigitizerReport](iouserhideventdriver/handledigitizerreport.md)
  Processes the digitizer elements and dispatches events for any updated values.
- [createEventForDigitizerCollection](iouserhideventdriver/createeventfordigitizercollection.md)
  Creates a HID event object that represents a digitizer collection.
### Configuring LED Lights
- [SetLED](iouserhideventdriver/setled.md)
  Sets the state of an LED on the device.
### Configuring Private Properties
- [setAccelerationProperties](iouserhideventdriver/setaccelerationproperties.md)
- [setSurfaceDimensions](iouserhideventdriver/setsurfacedimensions.md)
- [setTipThreshold](iouserhideventdriver/settipthreshold.md)
### Instance Methods
- [SetProperties](iouserhideventdriver/setproperties.md)
- [calibrateCenteredPreferredStateElement](iouserhideventdriver/calibratecenteredpreferredstateelement.md)
- [calibrateJustifiedPreferredStateElement](iouserhideventdriver/calibratejustifiedpreferredstateelement.md)
- [checkGameControllerElement](iouserhideventdriver/checkgamecontrollerelement.md)
- [copyKeyboardEvent](iouserhideventdriver/copykeyboardevent.md)
- [getButtonStateFromElements](iouserhideventdriver/getbuttonstatefromelements.md)
- [handleCopyMatchingEvent](iouserhideventdriver/handlecopymatchingevent.md)
- [handleGameControllerReport](iouserhideventdriver/handlegamecontrollerreport.md)
- [handleProximityReport](iouserhideventdriver/handleproximityreport.md)
- [parseElement](iouserhideventdriver/parseelement.md)
- [parseGameControllerElement](iouserhideventdriver/parsegamecontrollerelement.md)
- [parseProximityElement](iouserhideventdriver/parseproximityelement.md)
- [parseRemainingElement](iouserhideventdriver/parseremainingelement.md)
- [parseRemainingElements](iouserhideventdriver/parseremainingelements.md)
- [postProcessElements](iouserhideventdriver/postprocesselements.md)
- [postProcessElements_internal](iouserhideventdriver/postprocesselements_internal.md)
- [processDigitizerElements](iouserhideventdriver/processdigitizerelements.md)
- [processGameControllerElements](iouserhideventdriver/processgamecontrollerelements.md)
- [setDigitizerProperties](iouserhideventdriver/setdigitizerproperties.md)
- [setGameControllerProperties](iouserhideventdriver/setgamecontrollerproperties.md)
- [setKeyboardProperties](iouserhideventdriver/setkeyboardproperties.md)
- [setLEDProperties](iouserhideventdriver/setledproperties.md)
- [setRelativeProperties](iouserhideventdriver/setrelativeproperties.md)
- [setScrollProperties](iouserhideventdriver/setscrollproperties.md)

## Relationships

### Inherits From
- [IOUserHIDEventService](iouserhideventservice.md)

## See Also

- [com.apple.developer.driverkit.family.hid.eventservice](../BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.eventservice.md)
  A Boolean value that indicates whether the driver provides a HID-related event service to the system.
- [IOUserHIDEventService](iouserhideventservice.md)
  A service that parses HID report data into elements that you can use to dispatch events.
- [IOHIDEventService](iohideventservice.md)
  The base class for implementing a device or operating system service that dispatches events to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver)*