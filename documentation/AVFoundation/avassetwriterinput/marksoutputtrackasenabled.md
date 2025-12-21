# marksOutputTrackAsEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether to enable a track in the output for playback and processing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var marksOutputTrackAsEnabled: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). If the format you’re writing supports disabling tracks, you can disable a track by setting this value to [`false`](https://developer.apple.com/documentation/Swift/false).

You can’t set this value after writing starts.

## See Also

- [var naturalSize: CGSize](avassetwriterinput/naturalsize.md)
  The natural display dimensions of the output’s visual media.
- [var transform: CGAffineTransform](avassetwriterinput/transform.md)
  The transform to use for display of the output’s visual media.
- [var preferredVolume: Float](avassetwriterinput/preferredvolume.md)
  The volume to prefer for playback of the output’s audio data.
- [var mediaTimeScale: CMTimeScale](avassetwriterinput/mediatimescale.md)
  The time scale of the track in the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/marksoutputtrackasenabled)*