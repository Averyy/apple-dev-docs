# init(route:dataHandler:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Creates a new query to access the location data associated with a workout route.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
init(route workoutRoute: HKWorkoutRoute, dataHandler: @escaping @Sendable (HKWorkoutRouteQuery, [CLLocation]?, Bool, (any Error)?) -> Void)
```

```objc
- (instancetype) initWithRoute:(HKWorkoutRoute *) workoutRoute dataHandler:(void (^)(HKWorkoutRouteQuery *query, NSArray<CLLocation *> *routeData, BOOL done, NSError *error)) dataHandler;
```

## Return Value

A newly initialized route query.

## Parameters

- `workoutRoute`: The workout route containing the location data.
- `dataHandler`: A block called each time the system returns a batch of location data. This block may be called one or more times.

  The block is passed the following parameters:

  - **`query`**: The query that returns the location data.
  - **`routeData`**: A batch of location data, or `nil` if an error has occurred.
  - **`done`**: A Boolean value that indicates whether the query is complete. It is [`true`](../../Swift/true.md) if all the location data has been returned. If one or more additional batches of data are still pending, it is [`false`](../../Swift/false.md).
  - **`error`**: An object that describes the error, if an error has occurred; otherwise, `nil`.

## See Also

### Creating route queries
- [init(route: HKWorkoutRoute, dateInterval: DateInterval, dataHandler: (HKWorkoutRouteQuery, [CLLocation]?, Bool, (any Error)?) -> Void)](./init%28route,dateinterval,datahandler%29.md)
  Creates a new query to access the location data associated with a workout route during the specified date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutequery/init(route:datahandler:))*