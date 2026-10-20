# navigateTarget(with:completion:)

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
func navigateTarget(with params: MTRTargetNavigatorClusterNavigateTargetParams, completion: @escaping @Sendable (MTRTargetNavigatorClusterNavigateTargetResponseParams?, (any Error)?) -> Void)
```

```swift
func navigateTarget(with params: MTRTargetNavigatorClusterNavigateTargetParams) async throws -> MTRTargetNavigatorClusterNavigateTargetResponseParams
```

```objc
- (void) navigateTargetWithParams:(MTRTargetNavigatorClusterNavigateTargetParams *) params completion:(void (^)(MTRTargetNavigatorClusterNavigateTargetResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertargetnavigator/navigatetarget(with:completion:))*