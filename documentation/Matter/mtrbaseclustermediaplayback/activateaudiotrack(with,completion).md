# activateAudioTrack(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command ActivateAudioTrack

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
func activateAudioTrack(with params: MTRMediaPlaybackClusterActivateAudioTrackParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func activateAudioTrack(with params: MTRMediaPlaybackClusterActivateAudioTrackParams) async throws
```

```objc
- (void) activateAudioTrackWithParams:(MTRMediaPlaybackClusterActivateAudioTrackParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

This command is used to activate a specific Audio Track for the media being played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermediaplayback/activateaudiotrack(with:completion:))*