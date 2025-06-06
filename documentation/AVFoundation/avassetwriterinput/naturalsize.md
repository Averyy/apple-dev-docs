# naturalSize

**Framework**: AVFoundation  
**Kind**: property

The natural display dimensions of the output’s visual media.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var naturalSize: CGSize { get set }
```

#### Discussion

The default value is [`CGSizeZero`](https://developer.apple.com/documentation/CoreGraphics/CGSizeZero), which indicates the system sets the natural size according to the dimensions of the output track’s format descriptions.

You can’t set this value after writing starts.

## See Also

- [var transform: CGAffineTransform](avassetwriterinput/transform.md)
  The transform to use for display of the output’s visual media.
- [var preferredVolume: Float](avassetwriterinput/preferredvolume.md)
  The volume to prefer for playback of the output’s audio data.
- [var mediaTimeScale: CMTimeScale](avassetwriterinput/mediatimescale.md)
  The time scale of the track in the output file.
- [var marksOutputTrackAsEnabled: Bool](avassetwriterinput/marksoutputtrackasenabled.md)
  A Boolean value that indicates whether to enable a track in the output for playback and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/naturalsize)*