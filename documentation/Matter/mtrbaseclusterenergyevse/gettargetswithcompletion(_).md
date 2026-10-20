# getTargetsWithCompletion(_:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func getTargetsWithCompletion(_ completion: @escaping @Sendable (MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)
```

```swift
func targets() async throws -> MTREnergyEVSEClusterGetTargetsResponseParams
```

```objc
- (void) getTargetsWithCompletion:(void (^)(MTREnergyEVSEClusterGetTargetsResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterenergyevse/gettargetswithcompletion(_:))*