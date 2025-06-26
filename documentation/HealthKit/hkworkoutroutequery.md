# HKWorkoutRouteQuery

**Framework**: HealthKit  
**Kind**: class

A query to access the location data stored in a workout route.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class HKWorkoutRouteQuery
```

## Mentions

- [Reading route data](reading-route-data.md)

#### Overview

Use a workout route query to access the location data associated with an [`HKWorkoutRoute`](hkworkoutroute.md). Because a route sample can include a large number of [`CLLocation`](https://developer.apple.com/documentation/CoreLocation/CLLocation) objects, the query asynchronously returns the locations in batches. For detailed instructions, see `Reading Route Data`.

## Topics

### Creating route queries
- [init(route: HKWorkoutRoute, dataHandler: (HKWorkoutRouteQuery, [CLLocation]?, Bool, (any Error)?) -> Void)](hkworkoutroutequery/init(route:datahandler:).md)
  Creates a new query to access the location data associated with a workout route.
- [init(route: HKWorkoutRoute, dateInterval: DateInterval, dataHandler: (HKWorkoutRouteQuery, [CLLocation]?, Bool, (any Error)?) -> Void)](hkworkoutroutequery/init(route:dateinterval:datahandler:).md)
  Creates a new query to access the location data associated with a workout route during the specified date interval.

## Relationships

### Inherits From
- [HKQuery](hkquery.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct HKQuantitySeriesSampleQueryDescriptor](hkquantityseriessamplequerydescriptor.md)
  A query interface that reads the series data associated with quantity samples using Swift concurrency.
- [class HKQuantitySeriesSampleQuery](hkquantityseriessamplequery.md)
  A query that accesses the series data associated with a quantity sample.
- [struct HKWorkoutRouteQueryDescriptor](hkworkoutroutequerydescriptor.md)
  A query interface that reads the location data stored in a workout route using Swift concurrency.
- [struct HKHeartbeatSeriesQueryDescriptor](hkheartbeatseriesquerydescriptor.md)
  A query interface that reads the heartbeat series data stored in a heartbeat sample using Swift concurrency.
- [class HKHeartbeatSeriesQuery](hkheartbeatseriesquery.md)
  A query that returns the heartbeat data contained in a heartbeat series sample.
- [struct HKElectrocardiogramQueryDescriptor](hkelectrocardiogramquerydescriptor.md)
  A query interface that reads the underlying voltage measurements for an electrocardiogram sample using Swift concurrency.
- [class HKElectrocardiogramQuery](hkelectrocardiogramquery.md)
  A query that returns the underlying voltage measurements for an electrocardiogram sample.
- [class HKWorkoutEffortRelationship](hkworkouteffortrelationship.md)
- [class HKWorkoutEffortRelationshipQuery](hkworkouteffortrelationshipquery.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutequery)*