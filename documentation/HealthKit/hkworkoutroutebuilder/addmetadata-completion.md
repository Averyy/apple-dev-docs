# addMetadata(_:completion:)

**Framework**: HealthKit  
**Kind**: method

Adds metadata to the builder.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func addMetadata(_ metadata: [String : Any]) async throws
```

## See Also

- [func finishRoute(with: HKWorkout, metadata: [String : Any]?, completion: (HKWorkoutRoute?, (any Error)?) -> Void)](hkworkoutroutebuilder/finishroute(with:metadata:completion:).md)
  Creates, saves, and associates the route with the provided workout.
- [func insertRouteData([CLLocation], completion: (Bool, (any Error)?) -> Void)](hkworkoutroutebuilder/insertroutedata(_:completion:).md)
  Adds route data to the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutebuilder/addmetadata(_:completion:))*