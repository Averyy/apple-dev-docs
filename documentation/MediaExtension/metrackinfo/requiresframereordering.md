# requiresFrameReordering

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether frame reordering occurs in the track.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var requiresFrameReordering: Bool { get set }
```

```objc
@property (nonatomic) BOOL requiresFrameReordering;
```

## Discussion

The value is [`true`](../../Swift/true.md) if frame reordering occurs, otherwise [`false`](../../Swift/false.md). This property is only valid for tracks with video media type and is [`false`](../../Swift/false.md) for other track types.

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
- [var preferredTransform: CGAffineTransform](./preferredtransform.md)
  Indicates the preferred affine display transform of the track media for visual display.
- [var nominalFrameRate: Float32](./nominalframerate.md)
  The frame rate of the track in frames per second, as a 32-bit floating point number.
- [formatDescriptions](./formatdescriptions.md)
  An array of format descriptions for the track.
- [trackEdits](./trackedits.md)
  An array of edit segments for the given track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/metrackinfo/requiresframereordering)*