# preferredTransform

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

Indicates the preferred affine display transform of the track media for visual display.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var preferredTransform: CGAffineTransform { get set }
```

```objc
@property (nonatomic) CGAffineTransform preferredTransform;
```

#### Discussion

This property is only valid for tracks with visual media types and is [`CGAffineTransformIdentity`](../../CoreGraphics/cgaffinetransformidentity.md) for other track types.

## See Also

### Inspecting track information
- [var mediaType: CMMediaType](./mediatype.md)
  The media type of the track.
- [var trackID: CMPersistentTrackID](./trackid.md)
  An integer that identifies the track within the media asset.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the track is enabled by default.
- [var naturalTimescale: CMTimeScale](./naturaltimescale.md)
  The natural timescale of the track.
- [var extendedLanguageTag: String?](./extendedlanguagetag.md)
  A string that indicates the language tag associated with the track, as an IETF BCP 47 (RFC 4646) language identifier.
- [var naturalSize: CGSize](./naturalsize.md)
  Indicates the natural dimensions of the media data referenced by the track.
- [var nominalFrameRate: Float32](./nominalframerate.md)
  The frame rate of the track in frames per second, as a 32-bit floating point number.
- [var requiresFrameReordering: Bool](./requiresframereordering.md)
  A Boolean value that indicates whether frame reordering occurs in the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/metrackinfo/preferredtransform)*