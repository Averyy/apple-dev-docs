# stop(id:)

**Framework**: AlarmKit  
**Kind**: method

Stops the alarm with the specified ID.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func stop(id: Alarm.ID) throws
```

#### Discussion

If the alarm is a one-shot, meaning it doesn’t have a repeating schedule, then the system deletes the alarm. If the alarm repeats then it’s rescheduled to alert or begins counting down at the next scheduled time.

## Parameters

- `id`: The identifier of the alarm to stop.

## See Also

- [func cancel(id: Alarm.ID) throws](alarmmanager/cancel(id:).md)
  Cancels the alarm with the specified ID.
- [func countdown(id: Alarm.ID) throws](alarmmanager/countdown(id:).md)
  Performs a countdown for the alarm with the specified ID if it’s currently alerting.
- [func pause(id: Alarm.ID) throws](alarmmanager/pause(id:).md)
  Pauses the alarm with the specified ID if it’s in the countdown state.
- [func resume(id: Alarm.ID) throws](alarmmanager/resume(id:).md)
  Resumes the alarm with the specified ID if it’s in the paused state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/stop(id:))*