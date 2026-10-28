# suddenTerminationDisabled

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A flag to prevent sudden termination.

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
static var suddenTerminationDisabled: ProcessInfo.ActivityOptions { get }
```

```c
NSActivitySuddenTerminationDisabled
```

## Discussion

This is included by [`userInitiatedAllowingIdleSystemSleep`](./userinitiatedallowingidlesystemsleep.md).

## See Also

### Constants
- [static var idleDisplaySleepDisabled: ProcessInfo.ActivityOptions](./idledisplaysleepdisabled.md)
  A flag to require the screen to stay powered on.
- [static var idleSystemSleepDisabled: ProcessInfo.ActivityOptions](./idlesystemsleepdisabled.md)
  A flag to prevent idle sleep.
- [static var automaticTerminationDisabled: ProcessInfo.ActivityOptions](./automaticterminationdisabled.md)
  A flag to prevent automatic termination.
- [static var userInitiated: ProcessInfo.ActivityOptions](./userinitiated.md)
  A flag to indicate the app is performing a user-requested action.
- [static var userInteractive: ProcessInfo.ActivityOptions](./userinteractive.md)
  A flag to indicate the app is responding to user interaction.
- [static var userInitiatedAllowingIdleSystemSleep: ProcessInfo.ActivityOptions](./userinitiatedallowingidlesystemsleep.md)
  A flag to indicate the app is performing a user-requested action, but that the system can sleep on idle.
- [static var background: ProcessInfo.ActivityOptions](./background.md)
  A flag to indicate the app has initiated some kind of work, but not as the direct result of user request.
- [static var latencyCritical: ProcessInfo.ActivityOptions](./latencycritical.md)
  A flag to indicate the activity requires the highest amount of timer and I/O precision available.
- [static var animationTrackingEnabled: ProcessInfo.ActivityOptions](./animationtrackingenabled.md)
  A flag to track the activity with an animation signpost interval.
- [static var trackingEnabled: ProcessInfo.ActivityOptions](./trackingenabled.md)
  A flag to track the activity with a signpost interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/activityoptions/suddenterminationdisabled)*