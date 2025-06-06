# IOHIDScrollEventOptions

**Framework**: HIDDriverKit  
**Kind**: enum

Options that you use to dispatch scrolling-related events.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
typedef enum { ... } IOHIDScrollEventOptions;
```

#### Overview

Pass these options to the [`dispatchRelativeScrollWheelEvent`](iohideventservice/dispatchrelativescrollwheelevent.md) method of [`IOHIDEventService`](iohideventservice.md).

## Topics

### Getting the Scroll Event Option
- [kIOHIDScrollEventOptionsNoAcceleration](iohidscrolleventoptions/kiohidscrolleventoptionsnoacceleration.md)
  An option for not applying the default acceleration algorithm to this event.

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
- [dispatchRelativeScrollWheelEvent](iohideventservice/dispatchrelativescrollwheelevent.md)
  Dispatches a relative scroll wheel event to the system.
- [dispatchEvent](iohideventservice/dispatchevent.md)
  Dispatches a HID event to the system.
- [IOHIDKeyboardEventOptions](iohidkeyboardeventoptions.md)
  Options that you use to dispatch keyboard events.
- [IOHIDPointerEventOptions](iohidpointereventoptions.md)
  Options that you use to dispatch pointer-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidscrolleventoptions)*