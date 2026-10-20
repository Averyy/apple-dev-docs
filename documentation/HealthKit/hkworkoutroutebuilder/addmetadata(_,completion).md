# addMetadata(_:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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
func addMetadata(_ metadata: [String : Any], completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func addMetadata(_ metadata: [String : Any]) async throws
```

```objc
- (void) addMetadata:(NSDictionary<NSString *,id> *) metadata completion:(void (^)(BOOL success, NSError *error)) completion;
```

## See Also

### Building the route
- [func finishRoute(with: HKWorkout, metadata: [String : Any]?, completion: (HKWorkoutRoute?, (any Error)?) -> Void)](./finishroute%28with,metadata,completion%29.md)
  Creates, saves, and associates the route with the provided workout.
- [func insertRouteData([CLLocation], completion: (Bool, (any Error)?) -> Void)](./insertroutedata%28_,completion%29.md)
  Adds route data to the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutebuilder/addmetadata(_:completion:))*