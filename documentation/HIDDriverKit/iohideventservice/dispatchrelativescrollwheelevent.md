# dispatchRelativeScrollWheelEvent

**Framework**: HIDDriverKit  
**Kind**: method

Dispatches a relative scroll wheel event to the system.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t dispatchRelativeScrollWheelEvent(uint64_t timeStamp, IOFixed dx, IOFixed dy, IOFixed dz, IOOptionBits options, bool accelerate);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Call this method from your event service to dispatch a scroll-wheel event to the system. Typically, you call this method when handling a report from the device, after you determine that the report originated from scroll-wheel hardware or otherwise represents a scrolling event.

## Parameters

- `timeStamp`: The timestamp of the event. Use the timestamp of the report element that is the source of the event.
- `dx`: The delta X value.
- `dy`: The delta Y value.
- `dz`: The delta Z value.
- `options`: Additional options for scrolling-related events. Specify   for no options. For a list of other values, see  .
- `accelerate`: Scroll events are subject to an acceleration algorithm. Pass in   if you don’t wish to have acceleration logic applied to the scroll event.

## See Also

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
- [dispatchEvent](iohideventservice/dispatchevent.md)
  Dispatches a HID event to the system.
- [IOHIDKeyboardEventOptions](iohidkeyboardeventoptions.md)
  Options that you use to dispatch keyboard events.
- [IOHIDPointerEventOptions](iohidpointereventoptions.md)
  Options that you use to dispatch pointer-related events.
- [IOHIDScrollEventOptions](iohidscrolleventoptions.md)
  Options that you use to dispatch scrolling-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohideventservice/dispatchrelativescrollwheelevent)*