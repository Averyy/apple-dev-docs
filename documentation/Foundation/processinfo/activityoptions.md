# ProcessInfo.ActivityOptions

**Framework**: Foundation  
**Kind**: struct

Option flags used with [`beginActivity(options:reason:)`](processinfo/beginactivity(options:reason:).md) and [`performActivity(options:reason:using:)`](processinfo/performactivity(options:reason:using:).md).

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
struct ActivityOptions
```

#### Overview

To include one of these individual flags in one of the sets, use bitwise `OR`; for example, during a presentation you might use:

```objc
NSActivityUserInitiated | NSActivityIdleDisplaySleepDisabled
```

To exclude from one of the sets, use bitwise `AND` with `NOT`; for example, during a user initiated action that may be safely terminated with no application interaction in case of logout you might use:

```objc
NSActivityUserInitiated & ~NSActivitySuddenTerminationDisabled
```

## Topics

### Constants
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
- [static var trackingEnabled: ProcessInfo.ActivityOptions](processinfo/activityoptions/trackingenabled.md)
  A flag to track the activity with a signpost interval.
### Initializers
- [init(rawValue: UInt64)](processinfo/activityoptions/init(rawvalue:).md)
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
- [static var trackingEnabled: ProcessInfo.ActivityOptions](processinfo/activityoptions/trackingenabled.md)
  A flag to track the activity with a signpost interval.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct OperatingSystemVersion](operatingsystemversion.md)
  A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.
- [ProcessInfo.ThermalState](processinfo/thermalstate-swift.enum.md)
  Values used to indicate the system’s thermal state.
- [Anonymous](1552984-anonymous.md)
  The following constants are provided by the `NSProcessInfo` class as return values for [`operatingSystem()`](processinfo/operatingsystem().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/activityoptions)*