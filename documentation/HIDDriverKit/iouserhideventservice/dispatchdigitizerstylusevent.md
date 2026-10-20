# dispatchDigitizerStylusEvent

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Dispatches a digitizer stylus event to the system.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t dispatchDigitizerStylusEvent(uint64_t timeStamp, IOHIDDigitizerStylusData *stylusData);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

Call this method from your event service to dispatch a stylus event to the system. Typically, you call this method when handling a report from the device, after you determine that the event originated from a stylus.

## Parameters

- `timeStamp`: The timestamp of the event. Use the timestamp of the report element that is the source of the event.
- `stylusData`: A structure containing the stylus data. For more information, see [`IOHIDDigitizerStylusData`](../iohiddigitizerstylusdata.md).

## See Also

### Dispatching Events to the System
- [dispatchDigitizerTouchEvent](./dispatchdigitizertouchevent.md)
  Dispatches a digitizer touch event to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/dispatchdigitizerstylusevent)*