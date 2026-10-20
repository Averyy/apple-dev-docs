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
func changeToMode(with params: MTRRVCCleanModeClusterChangeToModeParams, completion: @escaping @Sendable (MTRRVCCleanModeClusterChangeToModeResponseParams?, (any Error)?) -> Void)
```

```swift
func changeToMode(with params: MTRRVCCleanModeClusterChangeToModeParams) async throws -> MTRRVCCleanModeClusterChangeToModeResponseParams
```

```objc
- (void) changeToModeWithParams:(MTRRVCCleanModeClusterChangeToModeParams *) params completion:(void (^)(MTRRVCCleanModeClusterChangeToModeResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterrvccleanmode/changetomode(with:completion:))*