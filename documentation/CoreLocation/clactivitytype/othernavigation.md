# CLActivityType.otherNavigation

**Framework**: Core Location  
**Kind**: case  
**Role**: Case

The value that indicates positioning for activities that don’t or may not adhere to roads such as cycling, scooters, trains, boats and off-road vehicles.

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
case otherNavigation
```

```c
CLActivityTypeOtherNavigation
```

#### Discussion

Use this activity type to track a positioning session such as by boat, train, or for pedestrian navigation tracking that’s not tied to a road network, paths, or trails. You can also use it for positioning activities indoors and outdoors, such as walking, that isn’t tied to a dedicated fitness session.

This activity might cause the system to pause location updates when the vehicle doesn’t move a significant distance over a period of time.

## See Also

### Activity types
- [CLActivityType.airborne](./airborne.md)
  The value that indicates activities in the air.
- [CLActivityType.automotiveNavigation](./automotivenavigation.md)
  The value that indicates positioning in an automobile following a road network.
- [CLActivityType.fitness](./fitness.md)
  The value that indicates positioning during dedicated fitness sessions, such as walking workouts, running workouts, cycling workouts, and so on.
- [CLActivityType.maritime](./maritime.md)
  The value that indicates positioning for activities in vessels on water, including while anchored.
- [CLActivityType.other](./other.md)
  The value that indicates the app is using location manager for an unspecified activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clactivitytype/othernavigation)*