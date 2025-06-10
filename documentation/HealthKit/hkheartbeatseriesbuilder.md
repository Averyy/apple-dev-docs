# HKHeartbeatSeriesBuilder

**Framework**: HealthKit  
**Kind**: class

A builder object for incrementally building a heartbeat series.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class HKHeartbeatSeriesBuilder
```

## Topics

### Creating a Heartbeat Series Builder
- [init(healthStore: HKHealthStore, device: HKDevice?, start: Date)](hkheartbeatseriesbuilder/init(healthstore:device:start:).md)
  Creates a new heartbeat series builder.
- [class var maximumCount: Int](hkheartbeatseriesbuilder/maximumcount.md)
  The maximum number of heartbeats you can add to the sample.
### Adding Data
- [func addHeartbeatWithTimeInterval(sinceSeriesStartDate: TimeInterval, precededByGap: Bool, completion: (Bool, (any Error)?) -> Void)](hkheartbeatseriesbuilder/addheartbeatwithtimeinterval(sinceseriesstartdate:precededbygap:completion:).md)
  Adds a heartbeat to the series.
- [func addMetadata([String : Any], completion: (Bool, (any Error)?) -> Void)](hkheartbeatseriesbuilder/addmetadata(_:completion:).md)
  Adds metadata to the sample.
### Ending the Collection
- [func finishSeries(completion: (HKHeartbeatSeriesSample?, (any Error)?) -> Void)](hkheartbeatseriesbuilder/finishseries(completion:).md)
  Finalizes the series and returns the resulting heartbeat series sample.

## Relationships

### Inherits From
- [HKSeriesBuilder](hkseriesbuilder.md)
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
- [class HKHeartbeatSeriesSample](hkheartbeatseriessample.md)
  A sample that represents a series of heartbeats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesbuilder)*