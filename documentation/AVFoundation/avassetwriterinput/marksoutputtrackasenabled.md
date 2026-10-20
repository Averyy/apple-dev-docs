# marksOutputTrackAsEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL marksOutputTrackAsEnabled;
```

#### Discussion

The default value is [`true`](../../Swift/true.md). If the format you’re writing supports disabling tracks, you can disable a track by setting this value to [`false`](../../Swift/false.md).

You can’t set this value after writing starts.

## See Also

### Configuring presentation
- [var naturalSize: CGSize](./naturalsize.md)
  The natural display dimensions of the output’s visual media.
- [var transform: CGAffineTransform](./transform.md)
  The transform to use for display of the output’s visual media.
- [var preferredVolume: Float](./preferredvolume.md)
  The volume to prefer for playback of the output’s audio data.
- [var mediaTimeScale: CMTimeScale](./mediatimescale.md)
  The time scale of the track in the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/marksoutputtrackasenabled)*