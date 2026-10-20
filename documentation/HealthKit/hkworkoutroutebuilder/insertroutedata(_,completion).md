# insertRouteData(_:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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
func insertRouteData(_ routeData: [CLLocation], completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func insertRouteData(_ routeData: [CLLocation]) async throws
```

```objc
- (void) insertRouteData:(NSArray<CLLocation *> *) routeData completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Mentions

- [Creating a workout route](../creating-a-workout-route.md)

#### Discussion

Use this method to asynchronously add one or more [`CLLocation`](../../CoreLocation/cllocation.md) objects to the series. The [`CLLocation`](../../CoreLocation/cllocation.md) objects may be inserted in any order; the builder sorts them by date when finalizing the route.

## Parameters

- `routeData`: An array containing one or more location objects.
- `completion`: A block called after the system adds the collection data to the builder. The system passes the block the following parameters:

  - **`success`**: A Boolean value that indicates whether the  builder successfully received the route data.
  - **`error`**: An object that describes the error, if an error has occurred; otherwise, `nil`.

## See Also

### Building the route
- [func finishRoute(with: HKWorkout, metadata: [String : Any]?, completion: (HKWorkoutRoute?, (any Error)?) -> Void)](./finishroute%28with,metadata,completion%29.md)
  Creates, saves, and associates the route with the provided workout.
- [func addMetadata([String : Any], completion: (Bool, (any Error)?) -> Void)](./addmetadata%28_,completion%29.md)
  Adds metadata to the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutebuilder/insertroutedata(_:completion:))*