# HKSeriesBuilder

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

An abstract base class for building series samples.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class HKSeriesBuilder
```

```objc
@interface HKSeriesBuilder : NSObject
```

## Overview

Never instantiate [`HKSeriesBuilder`](./hkseriesbuilder.md) objects directly. Instead, user one of the concrete subclasses (for example, the [`HKWorkoutRouteBuilder`](./hkworkoutroutebuilder.md) class).

## Topics

### Managing series generation
- [func discard()](./hkseriesbuilder/discard%28%29.md)
  Invalidates the builder and discards the collected data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [HKHeartbeatSeriesBuilder](./hkheartbeatseriesbuilder.md)
- [HKWorkoutRouteBuilder](./hkworkoutroutebuilder.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Route data
- [Creating a workout route](./creating-a-workout-route.md)
  Record the user’s route during a workout.
- [Reading route data](./reading-route-data.md)
  Access the user’s route for a workout.
- [class HKWorkoutRouteBuilder](./hkworkoutroutebuilder.md)
  A builder object that incrementally constructs a workout route.
- [class HKWorkoutRoute](./hkworkoutroute.md)
  A sample that contains a workout’s route data.
- [struct HKWorkoutRouteQueryDescriptor](./hkworkoutroutequerydescriptor.md)
  A query interface that reads the location data stored in a workout route using Swift concurrency.
- [class HKWorkoutRouteQuery](./hkworkoutroutequery.md)
  A query to access the location data stored in a workout route.
- [let HKWorkoutRouteTypeIdentifier: String](./hkworkoutroutetypeidentifier.md)
  A series sample containing location data that defines the route the user took during a workout.
- [class HKSeriesSample](./hkseriessample.md)
  An abstract base class that defines samples that contain a series of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkseriesbuilder)*