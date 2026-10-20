# HKWorkoutConfiguration

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

An object that contains configuration information about a workout session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HKWorkoutConfiguration
```

```objc
@interface HKWorkoutConfiguration : NSObject
```

#### Overview

As with many HealthKit classes, don’t subclass the [`HKWorkoutConfiguration`](./hkworkoutconfiguration.md) class.

## Topics

### Session settings
- [var activityType: HKWorkoutActivityType](./hkworkoutconfiguration/activitytype.md)
  The workout session’s activity type.
- [var locationType: HKWorkoutSessionLocationType](./hkworkoutconfiguration/locationtype.md)
  The workout session’s location.
- [enum HKWorkoutSessionLocationType](./hkworkoutsessionlocationtype.md)
  A constant indicating whether the workout session takes place indoors or outdoors.
- [var swimmingLocationType: HKWorkoutSwimmingLocationType](./hkworkoutconfiguration/swimminglocationtype.md)
  The workout session’s swimming location.
- [enum HKWorkoutSwimmingLocationType](./hkworkoutswimminglocationtype.md)
  The possible locations for swimming.
- [var lapLength: HKQuantity?](./hkworkoutconfiguration/laplength.md)
  The length of the lap for a workout session.
### Initializers
- [init?(coder: NSCoder)](./hkworkoutconfiguration/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Sessions
- [Running workout sessions](./running-workout-sessions.md)
  Track a workout on Apple Watch.
- [Build a workout app for Apple Watch](./build-a-workout-app-for-apple-watch.md)
  Create your own workout app, quickly and easily, with HealthKit and SwiftUI.
- [Building a multidevice workout app](./building-a-multidevice-workout-app.md)
  Mirror a workout from a watchOS app to its companion iOS app, and perform bidirectional communication between them.
- [Building a workout app for iPhone and iPad](./building-a-workout-app-for-iphone-and-ipad.md)
  Start a workout in iOS, control it from the Lock Screen with App Intents, and present the workout status with Live Activities.
- [class HKWorkoutSession](./hkworkoutsession.md)
  A session that tracks a person’s workout.
- [enum HKWorkoutSessionState](./hkworkoutsessionstate.md)
  A workout session’s state.
- [class HKLiveWorkoutBuilder](./hkliveworkoutbuilder.md)
  A builder object that constructs a workout incrementally based on live data from an active workout session.
- [protocol HKLiveWorkoutBuilderDelegate](./hkliveworkoutbuilderdelegate.md)
  A protocol that defines methods for receiving updates from a live workout builder.
- [class HKLiveWorkoutDataSource](./hkliveworkoutdatasource.md)
  A data source that automatically provides live data from an active workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration)*