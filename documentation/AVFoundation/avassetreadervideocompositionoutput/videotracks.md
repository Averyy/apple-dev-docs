# videoTracks

**Framework**: AVFoundation  
**Kind**: property

The tracks from which the output reads the composited video.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var videoTracks: [AVAssetTrack] { get }
```

#### Discussion

The array contains [`AVAssetTrack`](avassettrack.md) objects owned by the target asset reader’s asset.

## See Also

- [var videoSettings: [String : Any]?](avassetreadervideocompositionoutput/videosettings.md)
  The video settings that the output uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/videotracks)*