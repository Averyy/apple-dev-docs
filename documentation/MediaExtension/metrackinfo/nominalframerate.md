# nominalFrameRate

**Framework**: MediaExtension  
**Kind**: property

The frame rate of the track in frames per second, as a 32-bit floating point number.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var nominalFrameRate: Float32 { get set }
```

#### Discussion

For field-based video tracks that carry one field per media sample, the value of this property is the field rate, not the frame rate. `MediaToolbox` uses this property to calculate the maximum playback speed.

## See Also

- [var mediaType: CMMediaType](metrackinfo/mediatype.md)
  The media type of the track.
- [var trackID: CMPersistentTrackID](metrackinfo/trackid.md)
  An integer that identifies the track within the media asset.
- [var isEnabled: Bool](metrackinfo/isenabled.md)
  A Boolean value that indicates whether the track is enabled by default.
- [var naturalTimescale: CMTimeScale](metrackinfo/naturaltimescale.md)
  The natural timescale of the track.
- [var extendedLanguageTag: String?](metrackinfo/extendedlanguagetag.md)
  A string that indicates the language tag associated with the track, as an IETF BCP 47 (RFC 4646) language identifier.
- [var naturalSize: CGSize](metrackinfo/naturalsize.md)
  Indicates the natural dimensions of the media data referenced by the track.
- [var preferredTransform: CGAffineTransform](metrackinfo/preferredtransform.md)
  Indicates the preferred affine display transform of the track media for visual display.
- [var requiresFrameReordering: Bool](metrackinfo/requiresframereordering.md)
  A Boolean value that indicates whether frame reordering occurs in the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/metrackinfo/nominalframerate)*