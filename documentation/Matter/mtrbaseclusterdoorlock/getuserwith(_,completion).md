# getUserWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func getUserWith(_ params: MTRDoorLockClusterGetUserParams, completion: @escaping @Sendable (MTRDoorLockClusterGetUserResponseParams?, (any Error)?) -> Void)
```

```swift
func user(with params: MTRDoorLockClusterGetUserParams) async throws -> MTRDoorLockClusterGetUserResponseParams
```

```objc
- (void) getUserWithParams:(MTRDoorLockClusterGetUserParams *) params completion:(void (^)(MTRDoorLockClusterGetUserResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdoorlock/getuserwith(_:completion:))*