# HKWorkoutSessionState

**Framework**: HealthKit  
**Kind**: enum

A workout session’s state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HKWorkoutSessionState
```

## Topics

### Session states
- [HKWorkoutSessionState.notStarted](hkworkoutsessionstate/notstarted.md)
  The workout session has not started.
- [HKWorkoutSessionState.prepared](hkworkoutsessionstate/prepared.md)
  The session is ready but not yet running.
- [HKWorkoutSessionState.running](hkworkoutsessionstate/running.md)
  The workout session is running.
- [HKWorkoutSessionState.paused](hkworkoutsessionstate/paused.md)
  The workout session has paused.
- [HKWorkoutSessionState.stopped](hkworkoutsessionstate/stopped.md)
  The session has stopped.
- [HKWorkoutSessionState.ended](hkworkoutsessionstate/ended.md)
  The workout session has ended.
### Initializers
- [init?(rawValue: Int)](hkworkoutsessionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Running workout sessions](running-workout-sessions.md)
  Track a workout on Apple Watch.
- [Build a workout app for Apple Watch](build-a-workout-app-for-apple-watch.md)
  Create your own workout app, quickly and easily, with HealthKit and SwiftUI.
- [Building a multidevice workout app](building-a-multidevice-workout-app.md)
  Mirror a workout from a watchOS app to its companion iOS app, and perform bidirectional communication between them.
- [Building a workout app for iPhone and iPad](building-a-workout-app-for-iphone-and-ipad.md)
  Start a workout in iOS, control it from the Lock Screen with App Intents, and present the workout status with Live Activities.
- [class HKWorkoutSession](hkworkoutsession.md)
  A session that tracks a person’s workout.
- [class HKWorkoutConfiguration](hkworkoutconfiguration.md)
  An object that contains configuration information about a workout session.
- [class HKLiveWorkoutBuilder](hkliveworkoutbuilder.md)
  A builder object that constructs a workout incrementally based on live data from an active workout session.
- [class HKLiveWorkoutDataSource](hkliveworkoutdatasource.md)
  A data source that automatically provides live data from an active workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessionstate)*