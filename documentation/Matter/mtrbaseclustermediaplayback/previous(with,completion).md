# previous(with:completion:)

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
func previous(with params: MTRMediaPlaybackClusterPreviousParams?, completion: @escaping @Sendable (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)
```

```swift
func previous(with params: MTRMediaPlaybackClusterPreviousParams?) async throws -> MTRMediaPlaybackClusterPlaybackResponseParams
```

```objc
- (void) previousWithParams:(MTRMediaPlaybackClusterPreviousParams *) params completion:(void (^)(MTRMediaPlaybackClusterPlaybackResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermediaplayback/previous(with:completion:))*