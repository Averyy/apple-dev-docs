# dispatchKeyboardEvent

**Framework**: HIDDriverKit  
**Kind**: method

Dispatches a keyboard-related event to the system.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t dispatchKeyboardEvent(uint64_t timeStamp, uint32_t usagePage, uint32_t usage, uint32_t value, IOOptionBits options, bool repeat);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Call this method from your event service to dispatch a keyboard event to the system. Typically, you call this method when handling a report from the device, after you determine that the report contains a keyboard-related event.

## Parameters

- `timeStamp`: The timestamp of the event. Use the timestamp of the report element that is the source of the event.
- `usagePage`: The HID usage page to associate with the event. For a list of possible values, see  .
- `usage`: The HID usage code indicating the specific type of the event. For a list of possible usage values, see  .
- `value`: The value associated with the event.
- `options`: Additional options for keyboard events. Specify   for no options. For a list of other values, see  .
- `repeat`: The autorepeat behavior to apply when the user holds down a key. Specify   to apply the default behavior, which repeats the key event after a user-configurable amount of time elapses. Specify   to prevent the delivery of repeat events.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohideventservice/dispatchkeyboardevent)*