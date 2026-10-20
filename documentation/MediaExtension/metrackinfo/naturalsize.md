# naturalSize

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

Indicates the natural dimensions of the media data referenced by the track.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var naturalSize: CGSize { get set }
```

```objc
@property (nonatomic) CGSize naturalSize;
```

#### Discussion

This property is only valid for tracks with visual media types and is [`zero`](../../CoreFoundation/cgsize/zero.md) for other track types.

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
- [var preferredTransform: CGAffineTransform](./preferredtransform.md)
  Indicates the preferred affine display transform of the track media for visual display.
- [var nominalFrameRate: Float32](./nominalframerate.md)
  The frame rate of the track in frames per second, as a 32-bit floating point number.
- [var requiresFrameReordering: Bool](./requiresframereordering.md)
  A Boolean value that indicates whether frame reordering occurs in the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/metrackinfo/naturalsize)*