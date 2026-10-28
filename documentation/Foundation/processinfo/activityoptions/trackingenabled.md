# trackingEnabled

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```c
NSActivityTrackingEnabled
```

## Discussion

To help you investigate perfomance issues in your app, use [`trackingEnabled`](./trackingenabled.md) to track the timing of a user interaction by annotating the beginning and end of an activity using a signpost interval.

Calling [`beginActivity(options:reason:)`](../beginactivity%28options,reason%29.md) to begin the activity returns an object token that you retain for the duration of the activity. The logging system produces a distinct message, useful in debugging, if the object token is de-allocated before you call [`endActivity(_:)`](../endactivity%28_%29.md).

The flag [`trackingEnabled`](./trackingenabled.md) differs from [`animationTrackingEnabled`](./animationtrackingenabled.md) in the type of interval signposts the logging system emits. Use [`animationTrackingEnabled`](./animationtrackingenabled.md) when the interaction involves an animation.

## See Also

### Related Documentation
- [Recording Performance Data](../../../os/recording-performance-data.md)
  Add signposts to record interesting time-based events.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/activityoptions/trackingenabled)*