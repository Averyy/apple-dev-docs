# resume(id:)

**Framework**: AlarmKit  
**Kind**: method

Resumes the alarm with the specified ID if it’s in the paused state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func resume(id: Alarm.ID) throws
```

#### Discussion

The function throws otherwise. Sets the alarm to the [`AlarmPresentationState.Mode.Countdown`](alarmpresentationstate/mode-swift.enum/countdown.md) state

## Parameters

- `id`: The identifier of the alarm to resume.

## See Also

- [func cancel(id: Alarm.ID) throws](alarmmanager/cancel(id:).md)
  Cancels the alarm with the specified ID.
- [func countdown(id: Alarm.ID) throws](alarmmanager/countdown(id:).md)
  Performs a countdown for the alarm with the specified ID if it’s currently alerting.
- [func pause(id: Alarm.ID) throws](alarmmanager/pause(id:).md)
  Pauses the alarm with the specified ID if it’s in the countdown state.
- [func stop(id: Alarm.ID) throws](alarmmanager/stop(id:).md)
  Stops the alarm with the specified ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/resume(id:))*