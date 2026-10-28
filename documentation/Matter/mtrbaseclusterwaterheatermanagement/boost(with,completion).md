# boost(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command Boost

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
func boost(with params: MTRWaterHeaterManagementClusterBoostParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func boost(with params: MTRWaterHeaterManagementClusterBoostParams) async throws
```

```objc
- (void) boostWithParams:(MTRWaterHeaterManagementClusterBoostParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

Allows a client to request that the water heater is put into a Boost state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterwaterheatermanagement/boost(with:completion:))*