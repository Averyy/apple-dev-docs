# dispatchRelativePointerEvent

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Dispatches a relative pointer event to the system.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t dispatchRelativePointerEvent(uint64_t timeStamp, IOFixed dx, IOFixed dy, uint32_t buttonState, IOOptionBits options, bool accelerate);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

Call this method from your event service to dispatch a keyboard event to the system. Typically, you call this method after determining that a report contains data representing a mouse- or pointer-related event.

## Parameters

- `timeStamp`: The timestamp of the event. Use the timestamp of the report element that is the source of the event.
- `dx`: The distance traveled along the X axis, relative to the pointer’s previous location.
- `dy`: The distance traveled along the Y axis, relative to the pointer’s previous location.
- `buttonState`: The button state, if any.
- `options`: Additional options for pointer events. Specify `0` for no options. For a list of other values, see [`IOHIDPointerEventOptions`](../iohidpointereventoptions.md).
- `accelerate`: A Boolean value indicating whether to apply the acceleration algorithm to the pointer event. Specify `false` if you don’t want to apply that logic.

## See Also

### Dispatching Events
- [dispatchKeyboardEvent](./dispatchkeyboardevent.md)
  Dispatches a keyboard-related event to the system.
- [dispatchAbsolutePointerEvent](./dispatchabsolutepointerevent.md)
  Dispatches an absolute pointer event to the system.
- [dispatchDigitizerStylusEvent](./dispatchdigitizerstylusevent.md)
  Dispatches a digitizer stylus event to the system.
- [dispatchDigitizerTouchEvent](./dispatchdigitizertouchevent.md)
  Dispatches a digitizer touch event to the system.
- [dispatchRelativeScrollWheelEvent](./dispatchrelativescrollwheelevent.md)
  Dispatches a relative scroll wheel event to the system.
- [dispatchEvent](./dispatchevent.md)
  Dispatches a HID event to the system.
- [IOHIDKeyboardEventOptions](../iohidkeyboardeventoptions.md)
  Options that you use to dispatch keyboard events.
- [IOHIDPointerEventOptions](../iohidpointereventoptions.md)
  Options that you use to dispatch pointer-related events.
- [IOHIDScrollEventOptions](../iohidscrolleventoptions.md)
  Options that you use to dispatch scrolling-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohideventservice/dispatchrelativepointerevent)*