# activateAudioTrack(with:completion:)

**Framework**: Matter  
**Kind**: method

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
func activateAudioTrack(with params: MTRMediaPlaybackClusterActivateAudioTrackParams) async throws
```

#### Discussion

Upon receipt, the server SHALL set the active Audio Track to the one identified by the TrackID in the Track catalog for the streaming media. If the TrackID does not exist in the Track catalog, OR does not correspond to the streaming media OR no media is being streamed at the time of receipt of this command, the server will return an error status of INVALID_ARGUMENT.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermediaplayback/activateaudiotrack(with:completion:))*