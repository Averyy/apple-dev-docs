# dispatchAbsolutePointerEvent

**Framework**: HIDDriverKit  
**Kind**: method

Dispatches an absolute pointer event to the system.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t dispatchAbsolutePointerEvent(uint64_t timeStamp, IOFixed x, IOFixed y, uint32_t buttonState, IOOptionBits options, bool accelerate);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Call this method from your event service to dispatch a keyboard event to the system. Typically, you call this method after determining that a report contains data representing a mouse- or pointer-related event.

## Parameters

- `timeStamp`: The timestamp of the event. Use the timestamp of the report element that is the source of the event.
- `x`: The X value, specified in the range   to  .
- `y`: The Y value, specified in the range   to  .
- `buttonState`: The current button state, if any.
- `options`: Additional options for pointer events. Specify   for no options. For a list of other values, see  .
- `accelerate`: A Boolean value indicating whether to apply the acceleration algorithm to the pointer event. Specify   if you don’t want to apply that logic.

## See Also

- [dispatchKeyboardEvent](iohideventservice/dispatchkeyboardevent.md)
  Dispatches a keyboard-related event to the system.
- [dispatchRelativePointerEvent](iohideventservice/dispatchrelativepointerevent.md)
  Dispatches a relative pointer event to the system.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohideventservice/dispatchabsolutepointerevent)*