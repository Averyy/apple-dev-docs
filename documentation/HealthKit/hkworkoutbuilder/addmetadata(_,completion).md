# addMetadata(_:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Adds metadata to be saved with the workout.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 5.0+

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

### Adding metadata to the workout
- [var metadata: [String : Any]](./metadata.md)
  The metadata the builder saves with the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/addmetadata(_:completion:))*