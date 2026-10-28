# clearTargets(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command ClearTargets

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
func clearTargets(with params: MTREnergyEVSEClusterClearTargetsParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func clearTargets(with params: MTREnergyEVSEClusterClearTargetsParams?) async throws
```

```objc
- (void) clearTargetsWithParams:(MTREnergyEVSEClusterClearTargetsParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

Allows a client to clear all stored charging targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterenergyevse/cleartargets(with:completion:))*