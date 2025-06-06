# videoComposition

**Framework**: AVFoundation  
**Kind**: property

The video composition settings to be applied during playback.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var videoComposition: AVVideoComposition? { get set }
```

#### Discussion

A video composition can only be used with file-based media and is not supported for use with media served using HTTP Live Streaming.

## See Also

- [var customVideoCompositor: (any AVVideoCompositing)?](avplayeritem/customvideocompositor.md)
  The custom video compositor.
- [var seekingWaitsForVideoCompositionRendering: Bool](avplayeritem/seekingwaitsforvideocompositionrendering.md)
  A Boolean value that indicates whether the item’s timing follows the displayed video frame when seeking with a video composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/videocomposition)*