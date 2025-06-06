# CLActivityType.fitness

**Framework**: Core Location  
**Kind**: case

The value that indicates positioning during dedicated fitness sessions, such as walking workouts, running workouts, cycling workouts, and so on.

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
case fitness
```

#### Discussion

For other positioning sessions that aren’t workouts, use [`CLActivityType.otherNavigation`](clactivitytype/othernavigation.md) or [`CLActivityType.other`](clactivitytype/other.md). This activity might cause the system to pause location updates when the user doesn’t move a significant distance over a period of time.

When [`activityType`](cllocationmanager/activitytype.md) is [`CLActivityType.fitness`](clactivitytype/fitness.md), the system disables indoor positioning.

## See Also

- [CLActivityType.other](clactivitytype/other.md)
  The value that indicates the app is using location manager for an unspecified activity.
- [CLActivityType.automotiveNavigation](clactivitytype/automotivenavigation.md)
  The value that indicates positioning in an automobile following a road network.
- [CLActivityType.otherNavigation](clactivitytype/othernavigation.md)
  The value that indicates positioning for activities that don’t or may not adhere to roads such as cycling, scooters, trains, boats and off-road vehicles.
- [CLActivityType.airborne](clactivitytype/airborne.md)
  The value that indicates activities in the air.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clactivitytype/fitness)*