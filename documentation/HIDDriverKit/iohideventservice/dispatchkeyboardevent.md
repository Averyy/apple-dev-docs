# dispatchKeyboardEvent

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Dispatches a keyboard-related event to the system.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t dispatchKeyboardEvent(uint64_t timeStamp, uint32_t usagePage, uint32_t usage, uint32_t value, IOOptionBits options, bool repeat);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

Call this method from your event service to dispatch a keyboard event to the system. Typically, you call this method when handling a report from the device, after you determine that the report contains a keyboard-related event.

## Parameters

- `timeStamp`: The timestamp of the event. Use the timestamp of the report element that is the source of the event.
- `usagePage`: The HID usage page to associate with the event. For a list of possible values, see [Usage Pages](../usage-pages-enum.md).
- `usage`: The HID usage code indicating the specific type of the event. For a list of possible usage values, see [HID Usage Tables](../hid-usage-tables.md).
- `value`: The value associated with the event.
- `options`: Additional options for keyboard events. Specify `0` for no options. For a list of other values, see [`IOHIDKeyboardEventOptions`](../iohidkeyboardeventoptions.md).
- `repeat`: The autorepeat behavior to apply when the user holds down a key. Specify `true` to apply the default behavior, which repeats the key event after a user-configurable amount of time elapses. Specify `false` to prevent the delivery of repeat events.

## See Also

### Dispatching Events
- [dispatchRelativePointerEvent](./dispatchrelativepointerevent.md)
  Dispatches a relative pointer event to the system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohideventservice/dispatchkeyboardevent)*