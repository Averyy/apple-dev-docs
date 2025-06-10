# countdown(id:)

**Framework**: AlarmKit  
**Kind**: method

Performs a countdown for the alarm with the specified ID if it’s currently alerting.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func countdown(id: Alarm.ID) throws
```

#### Discussion

The function throws otherwise. This is identical to the repeat function of a timer, or the snooze function of an alarm.

## Parameters

- `id`: The identifier of the alarm to perform a countdown for.

## See Also

- [func cancel(id: Alarm.ID) throws](alarmmanager/cancel(id:).md)
  Cancels the alarm with the specified ID.
- [func pause(id: Alarm.ID) throws](alarmmanager/pause(id:).md)
  Pauses the alarm with the specified ID if it’s in the countdown state.
- [func resume(id: Alarm.ID) throws](alarmmanager/resume(id:).md)
  Resumes the alarm with the specified ID if it’s in the paused state.
- [func stop(id: Alarm.ID) throws](alarmmanager/stop(id:).md)
  Stops the alarm with the specified ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/countdown(id:))*