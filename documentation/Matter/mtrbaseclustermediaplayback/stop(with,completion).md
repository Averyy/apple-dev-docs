# stop(with:completion:)

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
func stop(with params: MTRMediaPlaybackClusterStopParams?, completion: @escaping @Sendable (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)
```

```swift
func stop(with params: MTRMediaPlaybackClusterStopParams?) async throws -> MTRMediaPlaybackClusterPlaybackResponseParams
```

```objc
- (void) stopWithParams:(MTRMediaPlaybackClusterStopParams *) params completion:(void (^)(MTRMediaPlaybackClusterPlaybackResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermediaplayback/stop(with:completion:))*