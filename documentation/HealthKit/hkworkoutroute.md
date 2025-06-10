# HKWorkoutRoute

**Framework**: HealthKit  
**Kind**: class

A sample that contains a workout’s route data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HKWorkoutRoute
```

## Mentions

- [Creating a workout route](creating-a-workout-route.md)
- [Reading route data](reading-route-data.md)

#### Overview

When creating a workout route, you do not instantiate the [`HKWorkoutRoute`](hkworkoutroute.md) objects directly. Instead, create a [`HKWorkoutRouteBuilder`](hkworkoutroutebuilder.md) object, and provide it with location data throughout the workout. After the workout ends, call the route builder’s  [`finishRoute(with:metadata:completion:)`](hkworkoutroutebuilder/finishroute(with:metadata:completion:).md) method to create the route. For detailed instructions, see [`Creating a workout route`](creating-a-workout-route.md).

The route’s location data is stored as an array of doc://com.apple.documentation/documentation/corelocation/cllocation objects. Because the route may contain a large number of location objects, use a [`HKWorkoutRouteQuery`](hkworkoutroutequery.md) object to asynchronously read the location data from the HealthKit store in batches. For more information, see [`Reading route data`](reading-route-data.md).

##### Using Workout Routes

Like many HealthKit classes, the [`HKWorkoutRoute`](hkworkoutroute.md) class should not be subclassed. You can extend [`HKWorkoutRoute`](hkworkoutroute.md) objects by adding custom metadata keys and values to the metadata dictionary when the object is created.

## Relationships

### Inherits From
- [HKSeriesSample](hkseriessample.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating a workout route](creating-a-workout-route.md)
  Record the user’s route during a workout.
- [Reading route data](reading-route-data.md)
  Access the user’s route for a workout.
- [class HKWorkoutRouteBuilder](hkworkoutroutebuilder.md)
  A builder object that incrementally constructs a workout route.
- [struct HKWorkoutRouteQueryDescriptor](hkworkoutroutequerydescriptor.md)
  A query interface that reads the location data stored in a workout route using Swift concurrency.
- [class HKWorkoutRouteQuery](hkworkoutroutequery.md)
  A query to access the location data stored in a workout route.
- [let HKWorkoutRouteTypeIdentifier: String](hkworkoutroutetypeidentifier.md)
  A series sample containing location data that defines the route the user took during a workout.
- [class HKSeriesBuilder](hkseriesbuilder.md)
  An abstract base class for building series samples.
- [class HKSeriesSample](hkseriessample.md)
  An abstract base class that defines samples that contain a series of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroute)*