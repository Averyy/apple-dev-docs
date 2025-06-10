# insertRouteData(_:completion:)

**Framework**: HealthKit  
**Kind**: method

Adds route data to the builder.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func insertRouteData(_ routeData: [CLLocation]) async throws
```

## Mentions

- [Creating a workout route](creating-a-workout-route.md)

#### Discussion

Use this method to asynchronously add one or more doc://com.apple.documentation/documentation/corelocation/cllocation objects to the series. The doc://com.apple.documentation/documentation/corelocation/cllocation objects may be inserted in any order; the builder sorts them by date when finalizing the route.

## Parameters

- `routeData`: An array containing one or more location objects.
- `completion`: A block called after the system adds the collection data to the builder. The system passes the block the following parameters:

## See Also

- [func finishRoute(with: HKWorkout, metadata: [String : Any]?, completion: (HKWorkoutRoute?, (any Error)?) -> Void)](hkworkoutroutebuilder/finishroute(with:metadata:completion:).md)
  Creates, saves, and associates the route with the provided workout.
- [func addMetadata([String : Any], completion: (Bool, (any Error)?) -> Void)](hkworkoutroutebuilder/addmetadata(_:completion:).md)
  Adds metadata to the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutebuilder/insertroutedata(_:completion:))*