# trackingEnabled

**Framework**: Foundation  
**Kind**: property

A flag to track the activity with a signpost interval.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var trackingEnabled: ProcessInfo.ActivityOptions { get }
```

#### Discussion

To help you investigate perfomance issues in your app, use [`trackingEnabled`](processinfo/activityoptions/trackingenabled.md) to track the timing of a user interaction by annotating the beginning and end of an activity using a signpost interval.

Calling [`beginActivity(options:reason:)`](processinfo/beginactivity(options:reason:).md) to begin the activity returns an object token that you retain for the duration of the activity. The logging system produces a distinct message, useful in debugging, if the object token is de-allocated before you call [`endActivity(_:)`](processinfo/endactivity(_:).md).

The flag [`trackingEnabled`](processinfo/activityoptions/trackingenabled.md) differs from [`animationTrackingEnabled`](processinfo/activityoptions/animationtrackingenabled.md) in the type of interval signposts the logging system emits. Use [`animationTrackingEnabled`](processinfo/activityoptions/animationtrackingenabled.md) when the interaction involves an animation.

## See Also

- [Recording Performance Data](../os/recording-performance-data.md)
  Add signposts to record interesting time-based events.
- [static var idleDisplaySleepDisabled: ProcessInfo.ActivityOptions](processinfo/activityoptions/idledisplaysleepdisabled.md)
  A flag to require the screen to stay powered on.
- [static var idleSystemSleepDisabled: ProcessInfo.ActivityOptions](processinfo/activityoptions/idlesystemsleepdisabled.md)
  A flag to prevent idle sleep.
- [static var suddenTerminationDisabled: ProcessInfo.ActivityOptions](processinfo/activityoptions/suddenterminationdisabled.md)
  A flag to prevent sudden termination.
- [static var automaticTerminationDisabled: ProcessInfo.ActivityOptions](processinfo/activityoptions/automaticterminationdisabled.md)
  A flag to prevent automatic termination.
- [static var userInitiated: ProcessInfo.ActivityOptions](processinfo/activityoptions/userinitiated.md)
  A flag to indicate the app is performing a user-requested action.
- [static var userInteractive: ProcessInfo.ActivityOptions](processinfo/activityoptions/userinteractive.md)
  A flag to indicate the app is responding to user interaction.
- [static var userInitiatedAllowingIdleSystemSleep: ProcessInfo.ActivityOptions](processinfo/activityoptions/userinitiatedallowingidlesystemsleep.md)
  A flag to indicate the app is performing a user-requested action, but that the system can sleep on idle.
- [static var background: ProcessInfo.ActivityOptions](processinfo/activityoptions/background.md)
  A flag to indicate the app has initiated some kind of work, but not as the direct result of user request.
- [static var latencyCritical: ProcessInfo.ActivityOptions](processinfo/activityoptions/latencycritical.md)
  A flag to indicate the activity requires the highest amount of timer and I/O precision available.
- [static var animationTrackingEnabled: ProcessInfo.ActivityOptions](processinfo/activityoptions/animationtrackingenabled.md)
  A flag to track the activity with an animation signpost interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/activityoptions/trackingenabled)*