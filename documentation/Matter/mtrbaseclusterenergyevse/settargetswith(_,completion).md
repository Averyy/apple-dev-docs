# setTargetsWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetTargets

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
func setTargetsWith(_ params: MTREnergyEVSEClusterSetTargetsParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setTargetsWith(_ params: MTREnergyEVSEClusterSetTargetsParams) async throws
```

```objc
- (void) setTargetsWithParams:(MTREnergyEVSEClusterSetTargetsParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

Allows a client to set the user specified charging targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterenergyevse/settargetswith(_:completion:))*