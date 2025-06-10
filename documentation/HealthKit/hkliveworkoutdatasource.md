# HKLiveWorkoutDataSource

**Framework**: HealthKit  
**Kind**: class

A data source that automatically provides live data from an active workout session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS ?+
- watchOS 5.0+

## Declaration

```swift
class HKLiveWorkoutDataSource
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

## Topics

### Creating a live data source
- [init(healthStore: HKHealthStore, workoutConfiguration: HKWorkoutConfiguration?)](hkliveworkoutdatasource/init(healthstore:workoutconfiguration:).md)
  Creates a new data source based on the provided workout configuration.
- [var typesToCollect: Set<HKQuantityType>](hkliveworkoutdatasource/typestocollect.md)
  The quantity type samples that the data source automatically sends to the workout builder.
### Calculating statistics
- [func enableCollection(for: HKQuantityType, predicate: NSPredicate?)](hkliveworkoutdatasource/enablecollection(for:predicate:).md)
  Begins automatically calculating statistics for samples that match the quantity type and predicate.
- [func disableCollection(for: HKQuantityType)](hkliveworkoutdatasource/disablecollection(for:).md)
  Stops automatically calculating statistics for the quantity type.
### Instance Properties
- [var collectsGeneratedTypes: Bool](hkliveworkoutdatasource/collectsgeneratedtypes.md)
- [var currentCollectedTypes: Set<HKQuantityType>](hkliveworkoutdatasource/currentcollectedtypes.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
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
  A session that tracks the user’s workout on Apple Watch.
- [class HKWorkoutConfiguration](hkworkoutconfiguration.md)
  An object that contains configuration information about a workout session.
- [enum HKWorkoutSessionState](hkworkoutsessionstate.md)
  A workout session’s state.
- [class HKLiveWorkoutBuilder](hkliveworkoutbuilder.md)
  A builder object that constructs a workout incrementally based on live data from an active workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource)*