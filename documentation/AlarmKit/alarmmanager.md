# AlarmManager

**Framework**: AlarmKit  
**Kind**: class

An object that exposes functions to work with alarms: scheduling, snoozing, cancelling.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
class AlarmManager
```

#### Overview

Schedule your alarm alert using `AlarmManager`. The following example calls the `AlarmManager` schedule function by passing in the id and configuration.

```swift
Task {
let _ = try? await AlarmManager.shared.schedule(id: id, configuration: configuration)
}
```

## Topics

### Creating a shared instance
- [static let shared: AlarmManager](alarmmanager/shared.md)
  The singleton instance for interacting with the alarm system.
### Updating an alarm
- [AlarmManager.AlarmUpdates](alarmmanager/alarmupdates-swift.struct.md)
  An async sequence that publishes whenever an alarm changes.
- [var alarmUpdates: some AsyncSequence<Array<Alarm>, Never>](alarmmanager/alarmupdates-swift.property.md)
  An asynchronous sequence that emits events when the set of alarms changes.
- [var alarms: [Alarm]](alarmmanager/alarms.md)
  Fetches all alarms from the daemon that belong to the current client.
### Scheduling an alarm
- [func schedule<Metadata>(id: Alarm.ID, configuration: AlarmManager.AlarmConfiguration<Metadata>) async throws -> Alarm](alarmmanager/schedule(id:configuration:).md)
  Schedules a new alarm.
- [AlarmManager.AlarmConfiguration](alarmmanager/alarmconfiguration.md)
  An object that contains all the properties necessary to schedule an alarm.
### Requesting authorization
- [func requestAuthorization() async throws -> AlarmManager.AuthorizationState](alarmmanager/requestauthorization.md)
  Requests permission to use the alarm system if it hasn’t been requested before.
### Checking authorization status
- [AlarmManager.AlarmAuthorizationStateUpdates](alarmmanager/alarmauthorizationstateupdates.md)
  An asynchronous sequence that publishes a new value when authorization for the alarms and timers system changes.
- [var authorizationUpdates: some AsyncSequence<AlarmManager.AuthorizationState, Never>](alarmmanager/authorizationupdates.md)
  An asynchronous sequence that emits events when authorization to use alarms changes.
- [AlarmManager.AuthorizationState](alarmmanager/authorizationstate-swift.enum.md)
  An enumeration describing all authorization states for the client process.
- [var authorizationState: AlarmManager.AuthorizationState](alarmmanager/authorizationstate-swift.property.md)
  Returns the current authorization state for this client.
### Changing an alarm state
- [func cancel(id: Alarm.ID) throws](alarmmanager/cancel(id:).md)
  Cancels the alarm with the specified ID.
- [func countdown(id: Alarm.ID) throws](alarmmanager/countdown(id:).md)
  Performs a countdown for the alarm with the specified ID if it’s currently alerting.
- [func pause(id: Alarm.ID) throws](alarmmanager/pause(id:).md)
  Pauses the alarm with the specified ID if it’s in the countdown state.
- [func resume(id: Alarm.ID) throws](alarmmanager/resume(id:).md)
  Resumes the alarm with the specified ID if it’s in the paused state.
- [func stop(id: Alarm.ID) throws](alarmmanager/stop(id:).md)
  Stops the alarm with the specified ID.
### Throwing an error
- [AlarmManager.AlarmError](alarmmanager/alarmerror.md)
  An error that occurs when trying to schedule a timer.

## See Also

- [Scheduling an alarm with AlarmKit](scheduling-an-alarm-with-alarmkit.md)
  Create prominent alerts at specified dates for your iOS app.
- [struct Alarm](alarm.md)
  An object that describes an alarm that can alert once or on a repeating schedule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager)*