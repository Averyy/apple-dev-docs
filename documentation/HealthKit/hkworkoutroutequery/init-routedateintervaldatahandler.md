# init(route:dateInterval:dataHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates a new query to access the location data associated with a workout route during the specified date interval.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(route workoutRoute: HKWorkoutRoute, dateInterval: DateInterval, dataHandler: @escaping (HKWorkoutRouteQuery, [CLLocation]?, Bool, (any Error)?) -> Void)
```

## Parameters

- `workoutRoute`: The workout route that contains the location data.
- `dateInterval`: If the date interval only partially overlaps the specified workout, the query only returns location data from the overlapping time period.
- `dataHandler`: The system passes this block the following parameters:

## See Also

- [init(route: HKWorkoutRoute, dataHandler: (HKWorkoutRouteQuery, [CLLocation]?, Bool, (any Error)?) -> Void)](hkworkoutroutequery/init(route:datahandler:).md)
  Creates a new query to access the location data associated with a workout route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutequery/init(route:dateinterval:datahandler:))*