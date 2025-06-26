# HKElectrocardiogramQuery

**Framework**: HealthKit  
**Kind**: class

A query that returns the underlying voltage measurements for an electrocardiogram sample.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class HKElectrocardiogramQuery
```

#### Overview

Use the [`HKElectrocardiogramQuery`](hkelectrocardiogramquery.md) query to access the individual voltage measurements associated with an [`HKElectrocardiogram`](hkelectrocardiogram.md) sample.

```swift
// Create a query for the voltage measurements
let voltageQuery = HKElectrocardiogramQuery(ecgSample) { (query, result) in
    switch(result) {
    
    case .measurement(let measurement):
        if let voltageQuantity = measurement.quantity(for: .appleWatchSimilarToLeadI) {
            // Do something with the voltage quantity here.

        }
    
    case .done:
        // No more voltages. Finish processing the existing voltages.

    case .error(let error):
        // Handle the error here.

    }
}

// Execute the query.
healthStore.execute(voltageQuery)
```

The query calls the data handler once for each voltage measurement, passing a [`HKElectrocardiogramQuery.Result.measurement(_:)`](hkelectrocardiogramquery/result/measurement(_:).md) instance that contains the voltage data. After it has sent all the voltage measurements, the query calls the data handler one last time, passing [`HKElectrocardiogramQuery.Result.done`](hkelectrocardiogramquery/result/done.md). If an error occurs, it stops collecting voltage data and passes [`HKElectrocardiogramQuery.Result.error(_:)`](hkelectrocardiogramquery/result/error(_:).md) instead.

Electrocardiogram queries are immutable: You set query’s properties when you create it, and they don’t change.

## Topics

### Creating the Query
- [convenience init(HKElectrocardiogram, dataHandler: (HKElectrocardiogramQuery, HKElectrocardiogramQuery.Result) -> Void)](hkelectrocardiogramquery/init(_:datahandler:).md)
  Creates a new electrocardiogram query object.
### Accessing the Results
- [HKElectrocardiogramQuery.Result](hkelectrocardiogramquery/result.md)
  Partial results for an electrocardiogram query.
- [init(electrocardiogram: HKElectrocardiogram, dataHandler: (HKElectrocardiogramQuery, HKElectrocardiogram.VoltageMeasurement?, Bool, (any Error)?) -> Void)](hkelectrocardiogramquery/init(electrocardiogram:datahandler:).md)
  Creates a new electrocardiogram query object.

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
- [class HKHeartbeatSeriesQuery](hkheartbeatseriesquery.md)
  A query that returns the heartbeat data contained in a heartbeat series sample.
- [struct HKElectrocardiogramQueryDescriptor](hkelectrocardiogramquerydescriptor.md)
  A query interface that reads the underlying voltage measurements for an electrocardiogram sample using Swift concurrency.
- [class HKWorkoutEffortRelationship](hkworkouteffortrelationship.md)
- [class HKWorkoutEffortRelationshipQuery](hkworkouteffortrelationshipquery.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogramquery)*