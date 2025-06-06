# preferredVolume

**Framework**: AVFoundation  
**Kind**: property

The volume to prefer for playback of the output’s audio data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preferredVolume: Float { get set }
```

#### Discussion

The default value for audio data is `1.0`, which indicates typical playback level. Set the value for this property in the range of `0.0` to `1.0`. For nonaudio media, the default value is `0.0`.

You can’t set this value after writing starts.

## See Also

- [var naturalSize: CGSize](avassetwriterinput/naturalsize.md)
  The natural display dimensions of the output’s visual media.
- [var transform: CGAffineTransform](avassetwriterinput/transform.md)
  The transform to use for display of the output’s visual media.
- [var mediaTimeScale: CMTimeScale](avassetwriterinput/mediatimescale.md)
  The time scale of the track in the output file.
- [var marksOutputTrackAsEnabled: Bool](avassetwriterinput/marksoutputtrackasenabled.md)
  A Boolean value that indicates whether to enable a track in the output for playback and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/preferredvolume)*