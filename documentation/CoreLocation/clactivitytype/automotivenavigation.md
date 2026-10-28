# CLActivityType.automotiveNavigation

**Framework**: Core Location  
**Kind**: case  
**Role**: Case

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

```c
CLActivityTypeAutomotiveNavigation
```

## Mentions

- [Getting the current location of a device](../getting-the-current-location-of-a-device.md)

## Discussion

Use this activity type when your app is using the location manager specifically during a vehicular positioning session to track location changes to the automobile.

This activity might cause the system to pause location updates when the vehicle doesn’t move for an extended period of time.

## See Also

### Activity types
- [CLActivityType.airborne](./airborne.md)
  The value that indicates activities in the air.
- [CLActivityType.fitness](./fitness.md)
  The value that indicates positioning during dedicated fitness sessions, such as walking workouts, running workouts, cycling workouts, and so on.
- [CLActivityType.maritime](./maritime.md)
  The value that indicates positioning for activities in vessels on water, including while anchored.
- [CLActivityType.other](./other.md)
  The value that indicates the app is using location manager for an unspecified activity.
- [CLActivityType.otherNavigation](./othernavigation.md)
  The value that indicates positioning for activities that don’t or may not adhere to roads such as cycling, scooters, trains, boats and off-road vehicles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clactivitytype/automotivenavigation)*