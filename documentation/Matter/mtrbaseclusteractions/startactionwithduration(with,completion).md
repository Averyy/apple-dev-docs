# startActionWithDuration(with:completion:)

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
func startActionWithDuration(with params: MTRActionsClusterStartActionWithDurationParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func startActionWithDuration(with params: MTRActionsClusterStartActionWithDurationParams) async throws
```

```objc
- (void) startActionWithDurationWithParams:(MTRActionsClusterStartActionWithDurationParams *) params completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteractions/startactionwithduration(with:completion:))*