# pause(id:)

**Framework**: AlarmKit  
**Kind**: method  
**Role**: Instance Method

Pauses the alarm with the specified ID if it’s in the countdown state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func pause(id: Alarm.ID) throws
```

#### Discussion

The function throws otherwise. Sets the alarm to the [`AlarmPresentationState.Mode.paused(_:)`](../alarmpresentationstate/mode-swift.enum/paused%28_%29.md) state.

## Parameters

- `id`: The identifier of the alarm to pause.

## See Also

### Changing an alarm state
- [func cancel(id: Alarm.ID) throws](./cancel%28id%29.md)
  Cancels the alarm with the specified ID.
- [func countdown(id: Alarm.ID) throws](./countdown%28id%29.md)
  Performs a countdown for the alarm with the specified ID if it’s currently alerting.
- [func resume(id: Alarm.ID) throws](./resume%28id%29.md)
  Resumes the alarm with the specified ID if it’s in the paused state.
- [func stop(id: Alarm.ID) throws](./stop%28id%29.md)
  Stops the alarm with the specified ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/pause(id:))*