# moveSaturation(with:completion:)

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
func moveSaturation(with params: MTRColorControlClusterMoveSaturationParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func moveSaturation(with params: MTRColorControlClusterMoveSaturationParams) async throws
```

```objc
- (void) moveSaturationWithParams:(MTRColorControlClusterMoveSaturationParams *) params completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustercolorcontrol/movesaturation(with:completion:))*