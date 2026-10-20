# getTargetsWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command GetTargets

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
func getTargetsWith(_ params: MTREnergyEVSEClusterGetTargetsParams?, completion: @escaping @Sendable (MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)
```

```swift
func targets(with params: MTREnergyEVSEClusterGetTargetsParams?) async throws -> MTREnergyEVSEClusterGetTargetsResponseParams
```

```objc
- (void) getTargetsWithParams:(MTREnergyEVSEClusterGetTargetsParams *) params completion:(void (^)(MTREnergyEVSEClusterGetTargetsResponseParams *data, NSError *error)) completion;
```

#### Discussion

Allows a client to retrieve the current set of charging targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterenergyevse/gettargetswith(_:completion:))*