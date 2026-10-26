# trackEdits

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

An array of edit segments for the given track.

**Availability**:
- macOS 14.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) NSArray<NSValue *> * trackEdits;
```

#### Discussion

Each value in the array contains a [`CMTimeMapping`](../../CoreMedia/cmtimemapping.md) object that describes the track edit. The [`target`](../../CoreMedia/cmtimemapping/target.md) time ranges for successive edits need to partition the time range from `0` to the track’s duration. In other words, for the first edit at index `0`, the [`start`](../../CoreMedia/cmtimerange/start.md) needs to be [`zero`](../../CoreMedia/cmtime/zero.md), and for each additional edit (index > 0), the [`start`](../../CoreMedia/cmtimerange/start.md) needs to match the value returned from [`CMTimeRangeGetEnd(_:)`](../../CoreMedia/cmtimerangegetend%28_%29.md) for the edit.

A track can have an empty [`trackEdits`](./trackedits.md) array, which means that there’s nothing in the track and the track duration is `0`. This property is `nil` for media asset formats that don’t support edit segments.

Each NSValue in the array contains a [`CMTimeMapping`](../../CoreMedia/cmtimemapping.md) object describing the track edit. The [`target`](../../CoreMedia/cmtimemapping/target.md) time ranges for successive edits must partition the time range from `0` to the track’s duration. In other words, for edit (index = 0) the [`start`](../../CoreMedia/cmtimerange/start.md) must be [`zero`](../../CoreMedia/cmtime/zero.md), while for edit (index > 0), the [`start`](../../CoreMedia/cmtimerange/start.md) must match the [`CMTimeRangeGetEnd(_:)`](../../CoreMedia/cmtimerangegetend%28_%29.md) for edit (index - 1). It is valid for a track to have an empty [`trackEdits`](./trackedits.md) array; this means that there is nothing at all in the track and the track duration is zero. If this property is implemented for media asset formats that do not support edit segments, it can return nil.

## See Also

### Inspecting track information
- [var mediaType: CMMediaType](./mediatype.md)
  The media type of the track.
- [var trackID: CMPersistentTrackID](./trackid.md)
  An integer that identifies the track within the media asset.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the track is enabled by default.
- [formatDescriptions](./formatdescriptions.md)
  An array of format descriptions for the track.
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
- [var requiresFrameReordering: Bool](./requiresframereordering.md)
  A Boolean value that indicates whether frame reordering occurs in the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/metrackinfo/trackedits)*