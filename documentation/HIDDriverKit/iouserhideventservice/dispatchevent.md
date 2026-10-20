# dispatchEvent

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Dispatches a HID event to the system.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual void dispatchEvent(IOHIDEvent *event);
```

#### Discussion

This method is a funnel point for dispatching events to the system’s registered clients. You can also call it directly to dispatch events for which you create an `IOHIDEvent` object.

## Parameters

- `event`: The event to dispatch.

## See Also

### Performing Private Tasks
- [createReportPool](./createreportpool.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/dispatchevent)*