# HKQuantitySeriesSampleBuilder

**Framework**: HealthKit  
**Kind**: class

A builder object for incrementally building a sample that contains multiple quantities.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class HKQuantitySeriesSampleBuilder
```

## Topics

### Creating a Quantity Series Builder
- [init(healthStore: HKHealthStore, quantityType: HKQuantityType, startDate: Date, device: HKDevice?)](hkquantityseriessamplebuilder/init(healthstore:quantitytype:startdate:device:).md)
  Creates a new quantity series builder.
- [var quantityType: HKQuantityType](hkquantityseriessamplebuilder/quantitytype.md)
  The quantity type for the series.
- [var startDate: Date](hkquantityseriessamplebuilder/startdate.md)
  The starting date and time for the sample.
- [var device: HKDevice?](hkquantityseriessamplebuilder/device.md)
  The device providing the data.
### Adding Values
- [func insert(HKQuantity, at: Date) throws](hkquantityseriessamplebuilder/insert(_:at:).md)
  Adds a new quantity to the series at the provided date and time.
- [func insert(HKQuantity, for: DateInterval) throws](hkquantityseriessamplebuilder/insert(_:for:).md)
  Adds a new quantity to the series with the provided date interval.
### Ending the Collection
- [func discard()](hkquantityseriessamplebuilder/discard.md)
  Discards all previously collected data and invalidates the builder.
- [func finishSeries(metadata: [String : Any]?, completion: ([HKQuantitySample]?, (any Error)?) -> Void)](hkquantityseriessamplebuilder/finishseries(metadata:completion:).md)
  Finalizes the series and returns the resulting quantity samples.
- [func finishSeries(metadata: [String : Any]?, endDate: Date?, completion: ([HKQuantitySample]?, (any Error)?) -> Void)](hkquantityseriessamplebuilder/finishseries(metadata:enddate:completion:).md)
  Finalizes the series with the provided end date, and returns the resulting quantity samples.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [class HKHeartbeatSeriesBuilder](hkheartbeatseriesbuilder.md)
  A builder object for incrementally building a heartbeat series.
- [class HKHeartbeatSeriesSample](hkheartbeatseriessample.md)
  A sample that represents a series of heartbeats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplebuilder)*