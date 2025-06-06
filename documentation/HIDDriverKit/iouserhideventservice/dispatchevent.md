# dispatchEvent

**Framework**: HIDDriverKit  
**Kind**: method

Dispatches a HID event to the system.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void dispatchEvent(IOHIDEvent * event);
```

#### Discussion

This method is a funnel point for dispatching events to the system’s registered clients. You can also call it directly to dispatch events for which you create an `IOHIDEvent` object.

## Parameters

- `event`: The event to dispatch.

## See Also

- [createReportPool](iouserhideventservice/createreportpool.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/dispatchevent)*