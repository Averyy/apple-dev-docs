# HKHeartbeatSeriesQuery

**Framework**: HealthKit  
**Kind**: class

A query that returns the heartbeat data contained in a heartbeat series sample.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class HKHeartbeatSeriesQuery
```

## Topics

### Creating a Heartbeat Series Query
- [init(heartbeatSeries: HKHeartbeatSeriesSample, dataHandler: (HKHeartbeatSeriesQuery, TimeInterval, Bool, Bool, (any Error)?) -> Void)](hkheartbeatseriesquery/init(heartbeatseries:datahandler:).md)
  Creates a new heartbeat series query.

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
- [class HKWorkoutRouteQuery](hkworkoutroutequery.md)
  A query to access the location data stored in a workout route.
- [struct HKHeartbeatSeriesQueryDescriptor](hkheartbeatseriesquerydescriptor.md)
  A query interface that reads the heartbeat series data stored in a heartbeat sample using Swift concurrency.
- [struct HKElectrocardiogramQueryDescriptor](hkelectrocardiogramquerydescriptor.md)
  A query interface that reads the underlying voltage measurements for an electrocardiogram sample using Swift concurrency.
- [class HKElectrocardiogramQuery](hkelectrocardiogramquery.md)
  A query that returns the underlying voltage measurements for an electrocardiogram sample.
- [class HKWorkoutEffortRelationship](hkworkouteffortrelationship.md)
- [class HKWorkoutEffortRelationshipQuery](hkworkouteffortrelationshipquery.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesquery)*