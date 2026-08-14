# HKSeriesSample

**Framework**: HealthKit  
**Kind**: class

An abstract base class that defines samples that contain a series of items.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class HKSeriesSample
```

#### Overview

Never instantiate [`HKSeriesSample`](hkseriessample.md) objects directly. Instead, user one of the concrete subclasses (for example, the [`HKWorkoutRoute`](hkworkoutroute.md) class).

## Topics

### Accessing the series
- [var count: Int](hkseriessample/count.md)
  The number of items in the series.

## Relationships

### Inherits From
- [HKSample](hksample.md)
### Inherited By
- [HKHeartbeatSeriesSample](hkheartbeatseriessample.md)
- [HKWorkoutRoute](hkworkoutroute.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Creating a workout route](creating-a-workout-route.md)
  Record the user’s route during a workout.
- [Reading route data](reading-route-data.md)
  Access the user’s route for a workout.
- [class HKWorkoutRouteBuilder](hkworkoutroutebuilder.md)
  A builder object that incrementally constructs a workout route.
- [class HKWorkoutRoute](hkworkoutroute.md)
  A sample that contains a workout’s route data.
- [struct HKWorkoutRouteQueryDescriptor](hkworkoutroutequerydescriptor.md)
  A query interface that reads the location data stored in a workout route using Swift concurrency.
- [class HKWorkoutRouteQuery](hkworkoutroutequery.md)
  A query to access the location data stored in a workout route.
- [let HKWorkoutRouteTypeIdentifier: String](hkworkoutroutetypeidentifier.md)
  A series sample containing location data that defines the route the user took during a workout.
- [class HKSeriesBuilder](hkseriesbuilder.md)
  An abstract base class for building series samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkseriessample)*