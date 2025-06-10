# latencyCritical

**Framework**: Foundation  
**Kind**: property

A flag to indicate the activity requires the highest amount of timer and I/O precision available.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var latencyCritical: ProcessInfo.ActivityOptions { get }
```

#### Discussion

> ❗ **Important**:  Very few applications should need to use this constant.

## See Also

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
- [static var animationTrackingEnabled: ProcessInfo.ActivityOptions](processinfo/activityoptions/animationtrackingenabled.md)
  A flag to track the activity with an animation signpost interval.
- [static var trackingEnabled: ProcessInfo.ActivityOptions](processinfo/activityoptions/trackingenabled.md)
  A flag to track the activity with a signpost interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/activityoptions/latencycritical)*