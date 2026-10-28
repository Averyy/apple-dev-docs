# reviewFabricRestrictions(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command ReviewFabricRestrictions

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
func reviewFabricRestrictions(with params: MTRAccessControlClusterReviewFabricRestrictionsParams, completion: @escaping @Sendable (MTRAccessControlClusterReviewFabricRestrictionsResponseParams?, (any Error)?) -> Void)
```

```swift
func reviewFabricRestrictions(with params: MTRAccessControlClusterReviewFabricRestrictionsParams) async throws -> MTRAccessControlClusterReviewFabricRestrictionsResponseParams
```

```objc
- (void) reviewFabricRestrictionsWithParams:(MTRAccessControlClusterReviewFabricRestrictionsParams *) params completion:(void (^)(MTRAccessControlClusterReviewFabricRestrictionsResponseParams *data, NSError *error)) completion;
```

## Discussion

This command signals to the service associated with the device vendor that the fabric administrator would like a review of the current restrictions on the accessing fabric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteraccesscontrol/reviewfabricrestrictions(with:completion:))*