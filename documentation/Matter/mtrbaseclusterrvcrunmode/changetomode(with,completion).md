# changeToMode(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func changeToMode(with params: MTRRVCRunModeClusterChangeToModeParams, completion: @escaping @Sendable (MTRRVCRunModeClusterChangeToModeResponseParams?, (any Error)?) -> Void)
```

```swift
func changeToMode(with params: MTRRVCRunModeClusterChangeToModeParams) async throws -> MTRRVCRunModeClusterChangeToModeResponseParams
```

```objc
- (void) changeToModeWithParams:(MTRRVCRunModeClusterChangeToModeParams *) params completion:(void (^)(MTRRVCRunModeClusterChangeToModeResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterrvcrunmode/changetomode(with:completion:))*