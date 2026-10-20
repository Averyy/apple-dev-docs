# cancelBoost(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command CancelBoost

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
func cancelBoost(with params: MTRWaterHeaterManagementClusterCancelBoostParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func cancelBoost(with params: MTRWaterHeaterManagementClusterCancelBoostParams?) async throws
```

```objc
- (void) cancelBoostWithParams:(MTRWaterHeaterManagementClusterCancelBoostParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

Allows a client to cancel an ongoing Boost operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterwaterheatermanagement/cancelboost(with:completion:))*