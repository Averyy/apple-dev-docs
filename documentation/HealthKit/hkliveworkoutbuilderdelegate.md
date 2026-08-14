# HKLiveWorkoutBuilderDelegate

**Framework**: HealthKit  
**Kind**: protocol

A protocol that defines methods for receiving updates from a live workout builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS ?+
- watchOS 5.0+

## Declaration

```swift
protocol HKLiveWorkoutBuilderDelegate : NSObjectProtocol
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)
- [Accessing workout zone data](accessing-workout-zone-data.md)

#### Overview

Conform to this protocol to receive notifications about workout data collection, events, activities, and zone changes during a live workout session.

## Topics

### Receiving data updates
- [func workoutBuilder(HKLiveWorkoutBuilder, didCollectDataOf: Set<HKSampleType>)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didcollectdataof:).md)
  Tells the delegate that new data has been added to the builder.
- [func workoutBuilderDidCollectEvent(HKLiveWorkoutBuilder)](hkliveworkoutbuilderdelegate/workoutbuilderdidcollectevent(_:).md)
  Tells the delegate that a new event has been added to the builder.
### Receiving activity updates
- [func workoutBuilder(HKLiveWorkoutBuilder, didBegin: HKWorkoutActivity)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didbegin:).md)
  Tells the delegate that a new workout activity has started.
- [func workoutBuilder(HKLiveWorkoutBuilder, didEnd: HKWorkoutActivity)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didend:).md)
  Tells the delegate that the current workout activity has ended.
### Receiving zone updates
- [func workoutBuilder(HKLiveWorkoutBuilder, didUpdateWorkoutZone: HKLiveWorkoutZoneUpdate)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didupdateworkoutzone:).md)
  Tells the delegate that the person changed zones during the workout.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

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
- [enum HKWorkoutSessionState](hkworkoutsessionstate.md)
  A workout session’s state.
- [class HKLiveWorkoutBuilder](hkliveworkoutbuilder.md)
  A builder object that constructs a workout incrementally based on live data from an active workout session.
- [class HKLiveWorkoutDataSource](hkliveworkoutdatasource.md)
  A data source that automatically provides live data from an active workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilderdelegate)*