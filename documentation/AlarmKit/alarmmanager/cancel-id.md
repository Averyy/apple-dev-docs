# cancel(id:)

**Framework**: AlarmKit  
**Kind**: method

Cancels the alarm with the specified ID.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func cancel(id: Alarm.ID) throws
```

#### Discussion

Deletes the alarm from the system even if the alarm has a repeating schedule.

## Parameters

- `id`: The identifier of the alarm to cancel.

## See Also

- [func countdown(id: Alarm.ID) throws](alarmmanager/countdown(id:).md)
  Performs a countdown for the alarm with the specified ID if it’s currently alerting.
- [func pause(id: Alarm.ID) throws](alarmmanager/pause(id:).md)
  Pauses the alarm with the specified ID if it’s in the countdown state.
- [func resume(id: Alarm.ID) throws](alarmmanager/resume(id:).md)
  Resumes the alarm with the specified ID if it’s in the paused state.
- [func stop(id: Alarm.ID) throws](alarmmanager/stop(id:).md)
  Stops the alarm with the specified ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/cancel(id:))*