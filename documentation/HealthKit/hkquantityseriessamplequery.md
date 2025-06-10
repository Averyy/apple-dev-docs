# HKQuantitySeriesSampleQuery

**Framework**: HealthKit  
**Kind**: class

A query that accesses the series data associated with a quantity sample.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class HKQuantitySeriesSampleQuery
```

## Mentions

- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)

#### Overview

Use a series query to access the individual [`HKQuantity`](hkquantity.md) objects added to a sample using an [`HKQuantitySeriesSampleBuilder`](hkquantityseriessamplebuilder.md).

> ❗ **Important**:  For many common calculations, consider using a statistical query instead. Statistical queries correctly handle quantity data, whether the samples represent a single quantity or a series.

## Topics

### Creating a Series Query
- [init(quantityType: HKQuantityType, predicate: NSPredicate?, quantityHandler: (HKQuantitySeriesSampleQuery, HKQuantity?, DateInterval?, HKQuantitySample?, Bool, (any Error)?) -> Void)](hkquantityseriessamplequery/init(quantitytype:predicate:quantityhandler:).md)
  Creates a new query for a series of the specified quantity type.
- [var includeSample: Bool](hkquantityseriessamplequery/includesample.md)
  A Boolean value that determines whether the query should return the series sample.
- [var orderByQuantitySampleStartDate: Bool](hkquantityseriessamplequery/orderbyquantitysamplestartdate.md)
  A Boolean value that determines whether the query groups the results based on the quantity sample’s start date.
### Deprecated Mehtods
- [init(sample: HKQuantitySample, quantityHandler: (HKQuantitySeriesSampleQuery, HKQuantity?, Date?, Bool, (any Error)?) -> Void)](hkquantityseriessamplequery/init(sample:quantityhandler:).md)
  Creates a new series query.

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

- [class HKQuantitySeriesSampleBuilder](hkquantityseriessamplebuilder.md)
  A builder object for incrementally building a sample that contains multiple quantities.
- [class HKCumulativeQuantitySample](hkcumulativequantitysample.md)
  A sample that represents a cumulative quantity.
- [class HKDiscreteQuantitySample](hkdiscretequantitysample.md)
  A sample that represents a discrete quantity.
- [struct HKQuantitySeriesSampleQueryDescriptor](hkquantityseriessamplequerydescriptor.md)
  A query interface that reads the series data associated with quantity samples using Swift concurrency.
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
- [class HKElectrocardiogramQuery](hkelectrocardiogramquery.md)
  A query that returns the underlying voltage measurements for an electrocardiogram sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequery)*