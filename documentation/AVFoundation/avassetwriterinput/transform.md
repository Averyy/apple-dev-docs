# transform

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) CGAffineTransform transform;
```

#### Discussion

By default, the input uses the [`CGAffineTransformIdentity`](../../CoreGraphics/cgaffinetransformidentity.md) transform.

You can’t set this value after writing starts.

## See Also

### Configuring presentation
- [var naturalSize: CGSize](./naturalsize.md)
  The natural display dimensions of the output’s visual media.
- [var preferredVolume: Float](./preferredvolume.md)
  The volume to prefer for playback of the output’s audio data.
- [var mediaTimeScale: CMTimeScale](./mediatimescale.md)
  The time scale of the track in the output file.
- [var marksOutputTrackAsEnabled: Bool](./marksoutputtrackasenabled.md)
  A Boolean value that indicates whether to enable a track in the output for playback and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/transform)*