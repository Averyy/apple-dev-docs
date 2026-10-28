# ProcessInfo.ActivityOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Option flags used with [`beginActivity(options:reason:)`](./beginactivity%28options,reason%29.md) and [`performActivity(options:reason:using:)`](./performactivity%28options,reason,using%29.md).

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

```c
enum NSActivityOptions : uint64_t;
```

## Overview

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
- [static var idleDisplaySleepDisabled: ProcessInfo.ActivityOptions](./activityoptions/idledisplaysleepdisabled.md)
  A flag to require the screen to stay powered on.
- [static var idleSystemSleepDisabled: ProcessInfo.ActivityOptions](./activityoptions/idlesystemsleepdisabled.md)
  A flag to prevent idle sleep.
- [static var suddenTerminationDisabled: ProcessInfo.ActivityOptions](./activityoptions/suddenterminationdisabled.md)
  A flag to prevent sudden termination.
- [static var automaticTerminationDisabled: ProcessInfo.ActivityOptions](./activityoptions/automaticterminationdisabled.md)
  A flag to prevent automatic termination.
- [static var userInitiated: ProcessInfo.ActivityOptions](./activityoptions/userinitiated.md)
  A flag to indicate the app is performing a user-requested action.
- [static var userInteractive: ProcessInfo.ActivityOptions](./activityoptions/userinteractive.md)
  A flag to indicate the app is responding to user interaction.
- [static var userInitiatedAllowingIdleSystemSleep: ProcessInfo.ActivityOptions](./activityoptions/userinitiatedallowingidlesystemsleep.md)
  A flag to indicate the app is performing a user-requested action, but that the system can sleep on idle.
- [static var background: ProcessInfo.ActivityOptions](./activityoptions/background.md)
  A flag to indicate the app has initiated some kind of work, but not as the direct result of user request.
- [static var latencyCritical: ProcessInfo.ActivityOptions](./activityoptions/latencycritical.md)
  A flag to indicate the activity requires the highest amount of timer and I/O precision available.
- [static var animationTrackingEnabled: ProcessInfo.ActivityOptions](./activityoptions/animationtrackingenabled.md)
  A flag to track the activity with an animation signpost interval.
- [static var trackingEnabled: ProcessInfo.ActivityOptions](./activityoptions/trackingenabled.md)
  A flag to track the activity with a signpost interval.
### Initializers
- [init(rawValue: UInt64)](./activityoptions/init%28rawvalue%29.md)
- [static var idleDisplaySleepDisabled: ProcessInfo.ActivityOptions](./activityoptions/idledisplaysleepdisabled.md)
  A flag to require the screen to stay powered on.
- [static var idleSystemSleepDisabled: ProcessInfo.ActivityOptions](./activityoptions/idlesystemsleepdisabled.md)
  A flag to prevent idle sleep.
- [static var suddenTerminationDisabled: ProcessInfo.ActivityOptions](./activityoptions/suddenterminationdisabled.md)
  A flag to prevent sudden termination.
- [static var automaticTerminationDisabled: ProcessInfo.ActivityOptions](./activityoptions/automaticterminationdisabled.md)
  A flag to prevent automatic termination.
- [static var userInitiated: ProcessInfo.ActivityOptions](./activityoptions/userinitiated.md)
  A flag to indicate the app is performing a user-requested action.
- [static var userInteractive: ProcessInfo.ActivityOptions](./activityoptions/userinteractive.md)
  A flag to indicate the app is responding to user interaction.
- [static var userInitiatedAllowingIdleSystemSleep: ProcessInfo.ActivityOptions](./activityoptions/userinitiatedallowingidlesystemsleep.md)
  A flag to indicate the app is performing a user-requested action, but that the system can sleep on idle.
- [static var background: ProcessInfo.ActivityOptions](./activityoptions/background.md)
  A flag to indicate the app has initiated some kind of work, but not as the direct result of user request.
- [static var latencyCritical: ProcessInfo.ActivityOptions](./activityoptions/latencycritical.md)
  A flag to indicate the activity requires the highest amount of timer and I/O precision available.
- [static var animationTrackingEnabled: ProcessInfo.ActivityOptions](./activityoptions/animationtrackingenabled.md)
  A flag to track the activity with an animation signpost interval.
- [static var trackingEnabled: ProcessInfo.ActivityOptions](./activityoptions/trackingenabled.md)
  A flag to track the activity with a signpost interval.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing activities
- [func beginActivity(options: ProcessInfo.ActivityOptions, reason: String) -> any NSObjectProtocol](./beginactivity%28options,reason%29.md)
  Begin an activity using the given options and reason.
- [func endActivity(any NSObjectProtocol)](./endactivity%28_%29.md)
  Ends the given activity.
- [func performActivity(options: ProcessInfo.ActivityOptions, reason: String, using: () -> Void)](./performactivity%28options,reason,using%29.md)
  Synchronously perform an activity defined by a given block using the given options.
- [func performExpiringActivity(withReason: String, using: (Bool) -> Void)](./performexpiringactivity%28withreason,using%29.md)
  Performs the specified block asynchronously and notifies you if the process is about to be suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/activityoptions)*