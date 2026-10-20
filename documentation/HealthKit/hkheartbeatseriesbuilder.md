# HKHeartbeatSeriesBuilder

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKHeartbeatSeriesBuilder : HKSeriesBuilder
```

## Topics

### Creating a Heartbeat Series Builder
- [init(healthStore: HKHealthStore, device: HKDevice?, start: Date)](./hkheartbeatseriesbuilder/init%28healthstore,device,start%29.md)
  Creates a new heartbeat series builder.
- [class var maximumCount: Int](./hkheartbeatseriesbuilder/maximumcount.md)
  The maximum number of heartbeats you can add to the sample.
### Adding Data
- [func addHeartbeatWithTimeInterval(sinceSeriesStartDate: TimeInterval, precededByGap: Bool, completion: (Bool, (any Error)?) -> Void)](./hkheartbeatseriesbuilder/addheartbeatwithtimeinterval%28sinceseriesstartdate,precededbygap,completion%29.md)
  Adds a heartbeat to the series.
- [func addMetadata([String : Any], completion: (Bool, (any Error)?) -> Void)](./hkheartbeatseriesbuilder/addmetadata%28_,completion%29.md)
  Adds metadata to the sample.
### Ending the Collection
- [func finishSeries(completion: (HKHeartbeatSeriesSample?, (any Error)?) -> Void)](./hkheartbeatseriesbuilder/finishseries%28completion%29.md)
  Finalizes the series and returns the resulting heartbeat series sample.
### Initializers
- [init(healthStore: HKHealthStore, device: HKDevice?, startDate: Date)](./hkheartbeatseriesbuilder/init%28healthstore,device,startdate%29.md)

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

### Series data
- [class HKQuantitySeriesSampleBuilder](./hkquantityseriessamplebuilder.md)
  A builder object for incrementally building a sample that contains multiple quantities.
- [class HKHeartbeatSeriesSample](./hkheartbeatseriessample.md)
  A sample that represents a series of heartbeats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesbuilder)*