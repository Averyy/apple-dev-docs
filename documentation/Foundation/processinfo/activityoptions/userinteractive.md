# userInteractive

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A flag to indicate the app is responding to user interaction.

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
static var userInteractive: ProcessInfo.ActivityOptions { get }
```

```c
NSActivityUserInteractive
```

#### Discussion

Examples of user-interactive actions include scrolling and interactively dismissing from a navigation controller.

## See Also

### Constants
- [static var idleDisplaySleepDisabled: ProcessInfo.ActivityOptions](./idledisplaysleepdisabled.md)
  A flag to require the screen to stay powered on.
- [static var idleSystemSleepDisabled: ProcessInfo.ActivityOptions](./idlesystemsleepdisabled.md)
  A flag to prevent idle sleep.
- [static var suddenTerminationDisabled: ProcessInfo.ActivityOptions](./suddenterminationdisabled.md)
  A flag to prevent sudden termination.
- [static var automaticTerminationDisabled: ProcessInfo.ActivityOptions](./automaticterminationdisabled.md)
  A flag to prevent automatic termination.
- [static var userInitiated: ProcessInfo.ActivityOptions](./userinitiated.md)
  A flag to indicate the app is performing a user-requested action.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/activityoptions/userinteractive)*