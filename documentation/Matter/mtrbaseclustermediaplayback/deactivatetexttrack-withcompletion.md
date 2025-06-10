# deactivateTextTrack(with:completion:)

**Framework**: Matter  
**Kind**: method

Command DeactivateTextTrack

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
func deactivateTextTrack(with params: MTRMediaPlaybackClusterDeactivateTextTrackParams?) async throws
```

#### Discussion

If a Text Track is active (i.e. being displayed), upon receipt of this command, the server SHALL stop displaying it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermediaplayback/deactivatetexttrack(with:completion:))*