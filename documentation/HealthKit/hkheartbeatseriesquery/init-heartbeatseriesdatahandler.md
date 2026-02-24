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
init(heartbeatSeries: HKHeartbeatSeriesSample, dataHandler: @escaping @Sendable (HKHeartbeatSeriesQuery, TimeInterval, Bool, Bool, (any Error)?) -> Void)
```

#### Discussion

The system calls the `dataHandler` once for each heartbeat until either the `done` parameter is [`true`](https://developer.apple.com/documentation/Foundation/NSExpression/true), or you call [`stop(_:)`](hkhealthstore/stop(_:).md).

## Parameters

- `heartbeatSeries`: The series sample containing the heartbeat data.
- `dataHandler`: The handler called by the query. The handler takes the following parameters: - **`query`**: The query that returned the heartbeat data.
- **`timeSinceSeriesStart`**: The time of the heartbeat, measured from the series builder’s start date. This must be a positive value.
- **`precededByGap`**: A Boolean value that indicates whether this heartbeat was immediately preceded by a gap in the data, indicating that one or more heartbeats may be missing.
- **`done`**: A Boolean value that indicates whether the query is complete.
- **`error`**: If an error occurred, this contains an object that describes the error; otherwise, `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesquery/init(heartbeatseries:datahandler:))*