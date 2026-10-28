# dispatchDigitizerTouchEvent

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Dispatches a digitizer touch event to the system.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t dispatchDigitizerTouchEvent(uint64_t timeStamp, IOHIDDigitizerTouchData *touchData, uint32_t touchDataCount);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

The default implementation of this method does nothing. Subclasses must override it to dispatch touch events.

## Parameters

- `timeStamp`: The timestamp of the event. Use the timestamp of the report element that is the source of the event.
- `touchData`: An array of structures containing the data for the individual touches. For more information, see [`IOHIDDigitizerTouchData`](../iohiddigitizertouchdata.md).
- `touchDataCount`: The number of structures in the `touchData` parameter.

## See Also

### Dispatching Events
- [dispatchKeyboardEvent](./dispatchkeyboardevent.md)
  Dispatches a keyboard-related event to the system.
- [dispatchRelativePointerEvent](./dispatchrelativepointerevent.md)
  Dispatches a relative pointer event to the system.
- [dispatchAbsolutePointerEvent](./dispatchabsolutepointerevent.md)
  Dispatches an absolute pointer event to the system.
- [dispatchDigitizerStylusEvent](./dispatchdigitizerstylusevent.md)
  Dispatches a digitizer stylus event to the system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohideventservice/dispatchdigitizertouchevent)*