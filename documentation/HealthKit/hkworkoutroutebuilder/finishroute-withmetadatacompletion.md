# finishRoute(with:metadata:completion:)

**Framework**: Healthkit  
**Kind**: method

Creates, saves, and associates the route with the provided workout.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func finishRoute(with workout: HKWorkout, metadata: [String : Any]?) async throws -> HKWorkoutRoute
```

## Mentions

- [Creating a workout route](creating-a-workout-route.md)

#### Discussion

Call this method after adding all the route data to the builder. The builder creates the route and saves it to the HealthKit store. It also associates the route with the provided workout. You cannot associate the route with another workout.

> **Note**:  You must call [`finishRoute(with:metadata:completion:)`](hkworkoutroutebuilder/finishroute(with:metadata:completion:).md) before the system deallocates the builder. Failure to do so results in a loss of all route data added to the builder.

This method fails if you haven’t added any location data to the builder. The completion handler returns an error and `nil` for the route.

Additionally, this method invalidates the builder. Any further calls to the builder returns an error. To subsequently access the workout route, use a query (for example, an [`HKSampleQuery`](hksamplequery.md) object).

## Parameters

- `workout`: The workout to associate with the route. You must have already saved this workout to the HealthKit store.
- `metadata`: Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own custom keys as needed to extend the HealthKit quantity sample’s capabilities.
- `completion`: A block called after the system has saved the route data. The system passes the block the following parameters:

## See Also

- [func insertRouteData([CLLocation], completion: (Bool, (any Error)?) -> Void)](hkworkoutroutebuilder/insertroutedata(_:completion:).md)
  Adds route data to the builder.
- [func addMetadata([String : Any], completion: (Bool, (any Error)?) -> Void)](hkworkoutroutebuilder/addmetadata(_:completion:).md)
  Adds metadata to the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutebuilder/finishroute(with:metadata:completion:))*