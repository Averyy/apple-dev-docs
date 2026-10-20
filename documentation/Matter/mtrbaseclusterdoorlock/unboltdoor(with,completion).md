# unboltDoor(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command UnboltDoor

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func unboltDoor(with params: MTRDoorLockClusterUnboltDoorParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func unboltDoor(with params: MTRDoorLockClusterUnboltDoorParams?) async throws
```

```objc
- (void) unboltDoorWithParams:(MTRDoorLockClusterUnboltDoorParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command causes the lock device to unlock the door without pulling the latch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdoorlock/unboltdoor(with:completion:))*