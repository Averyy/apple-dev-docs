# CLActivityType.automotiveNavigation

**Framework**: Core Location  
**Kind**: case

The value that indicates positioning in an automobile following a road network.

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
case automotiveNavigation
```

## Mentions

- [Getting the current location of a device](getting-the-current-location-of-a-device.md)

#### Discussion

Use this activity type when your app is using the location manager specifically during a vehicular positioning session to track location changes to the automobile.

This activity might cause the system to pause location updates when the vehicle doesn’t move for an extended period of time.

## See Also

- [CLActivityType.other](clactivitytype/other.md)
  The value that indicates the app is using location manager for an unspecified activity.
- [CLActivityType.fitness](clactivitytype/fitness.md)
  The value that indicates positioning during dedicated fitness sessions, such as walking workouts, running workouts, cycling workouts, and so on.
- [CLActivityType.otherNavigation](clactivitytype/othernavigation.md)
  The value that indicates positioning for activities that don’t or may not adhere to roads such as cycling, scooters, trains, boats and off-road vehicles.
- [CLActivityType.airborne](clactivitytype/airborne.md)
  The value that indicates activities in the air.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clactivitytype/automotivenavigation)*