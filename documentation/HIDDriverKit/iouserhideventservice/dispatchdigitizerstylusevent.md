# dispatchDigitizerStylusEvent

**Framework**: HIDDriverKit  
**Kind**: method

Dispatches a digitizer stylus event to the system.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t dispatchDigitizerStylusEvent(uint64_t timeStamp, IOHIDDigitizerStylusData * stylusData);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Call this method from your event service to dispatch a stylus event to the system. Typically, you call this method when handling a report from the device, after you determine that the event originated from a stylus.

## Parameters

- `timeStamp`: The timestamp of the event. Use the timestamp of the report element that is the source of the event.
- `stylusData`: A structure containing the stylus data. For more information, see  .

## See Also

- [dispatchDigitizerTouchEvent](iouserhideventservice/dispatchdigitizertouchevent.md)
  Dispatches a digitizer touch event to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/dispatchdigitizerstylusevent)*