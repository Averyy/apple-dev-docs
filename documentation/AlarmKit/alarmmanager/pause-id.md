# pause(id:)

**Framework**: AlarmKit  
**Kind**: method

Pauses the alarm with the specified ID if it’s in the countdown state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func pause(id: Alarm.ID) throws
```

#### Discussion

The function throws otherwise. Sets the alarm to the [`AlarmPresentationState.Mode.paused(_:)`](alarmpresentationstate/mode-swift.enum/paused(_:).md) state.

## Parameters

- `id`: The identifier of the alarm to pause.

## See Also

- [func cancel(id: Alarm.ID) throws](alarmmanager/cancel(id:).md)
  Cancels the alarm with the specified ID.
- [func countdown(id: Alarm.ID) throws](alarmmanager/countdown(id:).md)
  Performs a countdown for the alarm with the specified ID if it’s currently alerting.
- [func resume(id: Alarm.ID) throws](alarmmanager/resume(id:).md)
  Resumes the alarm with the specified ID if it’s in the paused state.
- [func stop(id: Alarm.ID) throws](alarmmanager/stop(id:).md)
  Stops the alarm with the specified ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/pause(id:))*