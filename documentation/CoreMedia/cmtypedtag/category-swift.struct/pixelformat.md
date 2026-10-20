# pixelFormat

**Framework**: Core Media  
**Kind**: property  
**Role**: Type Property

A category used for tagging pixel format information.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var pixelFormat: CMTypedTag<OSType>.Category { get }
```

Available when `TypedValue` conforms to `Sendable`.

## See Also

### Creating Typed Categories
- [static var channelID: CMTypedTag<Int64>.Category](./channelid.md)
  A category used for tagging a channel ID.
- [static var mediaSubType: CMTypedTag<CMFormatDescription.MediaSubType>.Category](./mediasubtype.md)
  A category used for tagging media subtype metadata.
- [static var mediaType: CMTypedTag<CMFormatDescription.MediaType>.Category](./mediatype.md)
  A category used for tagging media type metadata.
- [static var packingType: CMTypedTag<CMPackingType>.Category](./packingtype.md)
  A category used for tagging frame-packing information.
- [static var projectionType: CMTypedTag<CMProjectionType>.Category](./projectiontype.md)
  A category used for tagging projection surface information.
- [static var stereoView: CMTypedTag<CMStereoViewComponents>.Category](./stereoview.md)
  A category used for tagging eye information for 3D video.
- [static var stereoViewInterpretation: CMTypedTag<CMStereoViewInterpretationOptions>.Category](./stereoviewinterpretation.md)
  A category used for tagging how to interpret stereo view metadata.
- [static var trackID: CMTypedTag<CMPersistentTrackID>.Category](./trackid.md)
  A category used for tagging a track ID.
- [static var videoLayerID: CMTypedTag<Int64>.Category](./videolayerid.md)
  A category used for tagging a video layer ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtypedtag/category-swift.struct/pixelformat)*