# init(route:dataHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates a new query to access the location data associated with a workout route.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(route workoutRoute: HKWorkoutRoute, dataHandler: @escaping @Sendable (HKWorkoutRouteQuery, [CLLocation]?, Bool, (any Error)?) -> Void)
```

#### Return Value

A newly initialized route query.

## Parameters

- `workoutRoute`: The workout route containing the location data.
- `dataHandler`: A block called each time the system returns a batch of location data. This block may be called one or more times. The block is passed the following parameters: - **`query`**: The query that returns the location data.
- **`routeData`**: A batch of location data, or `nil` if an error has occurred.
- **`done`**: A Boolean value that indicates whether the query is complete. It is [`true`](https://developer.apple.com/documentation/swift/true) if all the location data has been returned. If one or more additional batches of data are still pending, it is [`false`](https://developer.apple.com/documentation/swift/false).
- **`error`**: An object that describes the error, if an error has occurred; otherwise, `nil`.

## See Also

- [init(route: HKWorkoutRoute, dateInterval: DateInterval, dataHandler: (HKWorkoutRouteQuery, [CLLocation]?, Bool, (any Error)?) -> Void)](hkworkoutroutequery/init(route:dateinterval:datahandler:).md)
  Creates a new query to access the location data associated with a workout route during the specified date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutequery/init(route:datahandler:))*