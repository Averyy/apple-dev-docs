# stop(id:)

**Framework**: AlarmKit  
**Kind**: method  
**Role**: Instance Method

Stops the alarm with the specified ID.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func stop(id: Alarm.ID) throws
```

## Discussion

If the alarm is a one-shot, meaning it doesn’t have a repeating schedule, then the system deletes the alarm. If the alarm repeats then it’s rescheduled to alert or begins counting down at the next scheduled time.

## Parameters

- `id`: The identifier of the alarm to stop.

## See Also

### Changing an alarm state
- [func cancel(id: Alarm.ID) throws](./cancel%28id%29.md)
  Cancels the alarm with the specified ID.
- [func countdown(id: Alarm.ID) throws](./countdown%28id%29.md)
  Performs a countdown for the alarm with the specified ID if it’s currently alerting.
- [func pause(id: Alarm.ID) throws](./pause%28id%29.md)
  Pauses the alarm with the specified ID if it’s in the countdown state.
- [func resume(id: Alarm.ID) throws](./resume%28id%29.md)
  Resumes the alarm with the specified ID if it’s in the paused state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/stop(id:))*