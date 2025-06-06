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
init(route workoutRoute: HKWorkoutRoute, dataHandler: @escaping (HKWorkoutRouteQuery, [CLLocation]?, Bool, (any Error)?) -> Void)
```

#### Return Value

A newly initialized route query.

## Parameters

- `workoutRoute`: The workout route containing the location data.
- `dataHandler`: The block is passed the following parameters:

## See Also

- [init(route: HKWorkoutRoute, dateInterval: DateInterval, dataHandler: (HKWorkoutRouteQuery, [CLLocation]?, Bool, (any Error)?) -> Void)](hkworkoutroutequery/init(route:dateinterval:datahandler:).md)
  Creates a new query to access the location data associated with a workout route during the specified date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutequery/init(route:datahandler:))*