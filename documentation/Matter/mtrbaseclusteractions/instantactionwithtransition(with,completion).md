# instantActionWithTransition(with:completion:)

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
func instantActionWithTransition(with params: MTRActionsClusterInstantActionWithTransitionParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func instantActionWithTransition(with params: MTRActionsClusterInstantActionWithTransitionParams) async throws
```

```objc
- (void) instantActionWithTransitionWithParams:(MTRActionsClusterInstantActionWithTransitionParams *) params completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteractions/instantactionwithtransition(with:completion:))*