# countdown(id:)

**Framework**: AlarmKit  
**Kind**: method  
**Role**: Instance Method

Performs a countdown for the alarm with the specified ID if it’s currently alerting.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func countdown(id: Alarm.ID) throws
```

## Discussion

The function throws otherwise. This is identical to the repeat function of a timer, or the snooze function of an alarm.

## Parameters

- `id`: The identifier of the alarm to perform a countdown for.

## See Also

### Changing an alarm state
- [func cancel(id: Alarm.ID) throws](./cancel%28id%29.md)
  Cancels the alarm with the specified ID.
- [func pause(id: Alarm.ID) throws](./pause%28id%29.md)
  Pauses the alarm with the specified ID if it’s in the countdown state.
- [func resume(id: Alarm.ID) throws](./resume%28id%29.md)
  Resumes the alarm with the specified ID if it’s in the paused state.
- [func stop(id: Alarm.ID) throws](./stop%28id%29.md)
  Stops the alarm with the specified ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/countdown(id:))*