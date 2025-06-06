# IOHIDEventService

**Framework**: HIDDriverKit  
**Kind**: class

The base class for implementing a device or operating system service that dispatches events to the system.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
class IOHIDEventService;
```

#### Overview

An `IOHIDEventService` object receives data from a device and generates events for the operating system to handle. Typically, you implement an event service by subclassing [`IOUserHIDEventService`](iouserhideventservice.md), but you may also subclass `IOHIDEventService` directly if you want to parse input reports yourself. In both cases, use the methods of this class to send events to the operating system, which dispatches those events to relevant apps.

## Topics

### Dispatching Events
- [dispatchKeyboardEvent](iohideventservice/dispatchkeyboardevent.md)
  Dispatches a keyboard-related event to the system.
- [dispatchRelativePointerEvent](iohideventservice/dispatchrelativepointerevent.md)
  Dispatches a relative pointer event to the system.
- [dispatchAbsolutePointerEvent](iohideventservice/dispatchabsolutepointerevent.md)
  Dispatches an absolute pointer event to the system.
- [dispatchDigitizerStylusEvent](iohideventservice/dispatchdigitizerstylusevent.md)
  Dispatches a digitizer stylus event to the system.
- [dispatchDigitizerTouchEvent](iohideventservice/dispatchdigitizertouchevent.md)
  Dispatches a digitizer touch event to the system.
- [dispatchRelativeScrollWheelEvent](iohideventservice/dispatchrelativescrollwheelevent.md)
  Dispatches a relative scroll wheel event to the system.
- [dispatchEvent](iohideventservice/dispatchevent.md)
  Dispatches a HID event to the system.
- [IOHIDKeyboardEventOptions](iohidkeyboardeventoptions.md)
  Options that you use to dispatch keyboard events.
- [IOHIDPointerEventOptions](iohidpointereventoptions.md)
  Options that you use to dispatch pointer-related events.
- [IOHIDScrollEventOptions](iohidscrolleventoptions.md)
  Options that you use to dispatch scrolling-related events.
### Configuring the LED Lights
- [SetLED](iohideventservice/setled.md)
  Configures the on/off state for an LED on the device.
### Instance Methods
- [SetLEDState](iohideventservice/setledstate.md)
- [SetProperties](iohideventservice/setproperties.md)
- [Start](iohideventservice/start.md)
- [Stop](iohideventservice/stop.md)
- [free](iohideventservice/free.md)
- [handleCopyMatchingEvent](iohideventservice/handlecopymatchingevent.md)
- [init](iohideventservice/init.md)

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)
### Inherited By
- [IOUserHIDEventService](iouserhideventservice.md)

## See Also

- [com.apple.developer.driverkit.family.hid.eventservice](../BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.eventservice.md)
  A Boolean value that indicates whether the driver provides a HID-related event service to the system.
- [IOUserHIDEventDriver](iouserhideventdriver.md)
  A complete driver object that dispatches keyboard, digitizer, scrolling, and pointer events originating from a HID device.
- [IOUserHIDEventService](iouserhideventservice.md)
  A service that parses HID report data into elements that you can use to dispatch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohideventservice)*