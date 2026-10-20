# HKWorkoutRouteBuilder

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A builder object that incrementally constructs a workout route.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HKWorkoutRouteBuilder
```

```objc
@interface HKWorkoutRouteBuilder : HKSeriesBuilder
```

#### Overview

To create a workout route, use [`seriesBuilder(for:)`](./hkworkoutbuilder/seriesbuilder%28for%29.md) to instantiate a [`HKWorkoutRouteBuilder`](./hkworkoutroutebuilder.md), and provide it with location data throughout the workout. After the workout ends, call the builder’s [`finishRoute(with:metadata:completion:)`](./hkworkoutroutebuilder/finishroute%28with,metadata,completion%29.md) method to construct the route. Instantiating a [`HKWorkoutRouteBuilder`](./hkworkoutroutebuilder.md) directly is discouraged. For detailed instructions, see [Creating a workout route](./creating-a-workout-route.md).

## Topics

### Creating the builder
- [func seriesBuilder(for: HKSeriesType) -> HKSeriesBuilder?](./hkworkoutbuilder/seriesbuilder%28for%29.md)
  Returns the series builder for the specified type, creating a new builder, if necessary.
- [init(healthStore: HKHealthStore, device: HKDevice?)](./hkworkoutroutebuilder/init%28healthstore,device%29.md)
  Creates and returns a new workout route builder.
### Building the route
- [func finishRoute(with: HKWorkout, metadata: [String : Any]?, completion: (HKWorkoutRoute?, (any Error)?) -> Void)](./hkworkoutroutebuilder/finishroute%28with,metadata,completion%29.md)
  Creates, saves, and associates the route with the provided workout.
- [func insertRouteData([CLLocation], completion: (Bool, (any Error)?) -> Void)](./hkworkoutroutebuilder/insertroutedata%28_,completion%29.md)
  Adds route data to the builder.
- [func addMetadata([String : Any], completion: (Bool, (any Error)?) -> Void)](./hkworkoutroutebuilder/addmetadata%28_,completion%29.md)
  Adds metadata to the builder.

## Relationships

### Inherits From
- [HKSeriesBuilder](./hkseriesbuilder.md)
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
- [class HKWorkoutRoute](./hkworkoutroute.md)
  A sample that contains a workout’s route data.
- [struct HKWorkoutRouteQueryDescriptor](./hkworkoutroutequerydescriptor.md)
  A query interface that reads the location data stored in a workout route using Swift concurrency.
- [class HKWorkoutRouteQuery](./hkworkoutroutequery.md)
  A query to access the location data stored in a workout route.
- [let HKWorkoutRouteTypeIdentifier: String](./hkworkoutroutetypeidentifier.md)
  A series sample containing location data that defines the route the user took during a workout.
- [class HKSeriesBuilder](./hkseriesbuilder.md)
  An abstract base class for building series samples.
- [class HKSeriesSample](./hkseriessample.md)
  An abstract base class that defines samples that contain a series of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutebuilder)*