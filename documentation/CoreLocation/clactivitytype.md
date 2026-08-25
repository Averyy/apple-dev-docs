# CLActivityType

**Framework**: Core Location  
**Kind**: enum

Constants that indicate the type of activity associated with location updates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CLActivityType
```

## Topics

### Activity types
- [CLActivityType.airborne](clactivitytype/airborne.md)
  The value that indicates activities in the air.
- [CLActivityType.automotiveNavigation](clactivitytype/automotivenavigation.md)
  The value that indicates positioning in an automobile following a road network.
- [CLActivityType.fitness](clactivitytype/fitness.md)
  The value that indicates positioning during dedicated fitness sessions, such as walking workouts, running workouts, cycling workouts, and so on.
- [CLActivityType.maritime](clactivitytype/maritime.md)
  The value that indicates positioning for activities in vessels on water, including while anchored.
- [CLActivityType.other](clactivitytype/other.md)
  The value that indicates the app is using location manager for an unspecified activity.
- [CLActivityType.otherNavigation](clactivitytype/othernavigation.md)
  The value that indicates positioning for activities that don’t or may not adhere to roads such as cycling, scooters, trains, boats and off-road vehicles.
### Creating an activity type instance
- [init?(rawValue: Int)](clactivitytype/init(rawvalue:).md)
  Creates an activity type instance with the provided value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func startUpdatingLocation()](cllocationmanager/startupdatinglocation.md)
  Starts the generation of updates that report the user’s current location.
- [func stopUpdatingLocation()](cllocationmanager/stopupdatinglocation.md)
  Stops the generation of location updates.
- [func requestLocation()](cllocationmanager/requestlocation.md)
  Requests the one-time delivery of the user’s current location.
- [var pausesLocationUpdatesAutomatically: Bool](cllocationmanager/pauseslocationupdatesautomatically.md)
  A Boolean value that indicates whether the location-manager object may pause location updates.
- [var allowsBackgroundLocationUpdates: Bool](cllocationmanager/allowsbackgroundlocationupdates.md)
  A Boolean value that indicates whether the app receives location updates when running in the background.
- [var showsBackgroundLocationIndicator: Bool](cllocationmanager/showsbackgroundlocationindicator.md)
  A Boolean value that indicates whether the status bar changes its appearance when an app uses location services in the background.
- [var activityType: CLActivityType](cllocationmanager/activitytype.md)
  The type of activity the app expects the user to typically perform while in the app’s location session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clactivitytype)*