# transform

**Framework**: AVFoundation  
**Kind**: property

The transform to use for display of the output’s visual media.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var transform: CGAffineTransform { get set }
```

#### Discussion

By default, the input uses the [`CGAffineTransformIdentity`](https://developer.apple.com/documentation/CoreGraphics/CGAffineTransformIdentity) transform.

You can’t set this value after writing starts.

## See Also

- [var naturalSize: CGSize](avassetwriterinput/naturalsize.md)
  The natural display dimensions of the output’s visual media.
- [var preferredVolume: Float](avassetwriterinput/preferredvolume.md)
  The volume to prefer for playback of the output’s audio data.
- [var mediaTimeScale: CMTimeScale](avassetwriterinput/mediatimescale.md)
  The time scale of the track in the output file.
- [var marksOutputTrackAsEnabled: Bool](avassetwriterinput/marksoutputtrackasenabled.md)
  A Boolean value that indicates whether to enable a track in the output for playback and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/transform)*