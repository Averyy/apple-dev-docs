# dispatchDigitizerTouchEvent

**Framework**: HIDDriverKit  
**Kind**: method

Dispatches a digitizer touch event to the system.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t dispatchDigitizerTouchEvent(uint64_t timeStamp, IOHIDDigitizerTouchData * touchData, uint32_t touchDataCount);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Call this method from your event service to dispatch a touch event to the system. Typically, you call this method when handling a report from the device, after you determine that the event originated from a touchscreen or touch pad.

## Parameters

- `timeStamp`: The timestamp of the event. Use the timestamp of the report element that is the source of the event.
- `touchData`: An array of structures containing the data for the individual touches. For more information, see  .
- `touchDataCount`: The number of structures in the   parameter.

## See Also

- [dispatchDigitizerStylusEvent](iouserhideventservice/dispatchdigitizerstylusevent.md)
  Dispatches a digitizer stylus event to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/dispatchdigitizertouchevent)*