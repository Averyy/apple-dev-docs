# init(heartbeatSeries:dataHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates a new heartbeat series query.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(heartbeatSeries: HKHeartbeatSeriesSample, dataHandler: @escaping (HKHeartbeatSeriesQuery, TimeInterval, Bool, Bool, (any Error)?) -> Void)
```

#### Discussion

The system calls the `dataHandler` once for each heartbeat until either the `done` parameter is [`true`](https://developer.apple.com/documentation/foundation/nsexpression/1411874-true), or you call [`stop(_:)`](hkhealthstore/stop(_:).md).

## Parameters

- `heartbeatSeries`: The series sample containing the heartbeat data.
- `dataHandler`: The handler called by the query. The handler takes the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesquery/init(heartbeatseries:datahandler:))*