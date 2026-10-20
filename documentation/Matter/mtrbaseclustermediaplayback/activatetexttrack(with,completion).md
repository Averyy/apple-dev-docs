# activateTextTrack(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command ActivateTextTrack

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
func activateTextTrack(with params: MTRMediaPlaybackClusterActivateTextTrackParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func activateTextTrack(with params: MTRMediaPlaybackClusterActivateTextTrackParams) async throws
```

```objc
- (void) activateTextTrackWithParams:(MTRMediaPlaybackClusterActivateTextTrackParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command is used to activate a specific Text Track for the media being played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermediaplayback/activatetexttrack(with:completion:))*