# packingType(_:)

**Framework**: Core Media  
**Kind**: method

Creates a tag containing frame-packing information.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func packingType(_ value: CMPackingType) -> CMTypedTag<CMPackingType>
```

#### Return Value

A new typed tag containing the frame-packing type of `value`.

## Parameters

- `value`: The type of frame-packing for this tag.

## See Also

- [static func channelID(Int64) -> CMTypedTag<Int64>](cmtag-swift.class/channelid(_:).md)
  Creates a new channel ID tag from an integer.
- [static func mediaSubType(CMFormatDescription.MediaSubType) -> CMTypedTag<CMFormatDescription.MediaSubType>](cmtag-swift.class/mediasubtype(_:).md)
  Creates a tag containing media subtype metadata.
- [static func mediaType(CMFormatDescription.MediaType) -> CMTypedTag<CMFormatDescription.MediaType>](cmtag-swift.class/mediatype(_:).md)
  Creates a tag containing media type metadata.
- [static func pixelFormat(OSType) -> CMTypedTag<OSType>](cmtag-swift.class/pixelformat(_:).md)
  Creates a tag containing pixel format information.
- [static func projectionType(CMProjectionType) -> CMTypedTag<CMProjectionType>](cmtag-swift.class/projectiontype(_:).md)
  Creates a tag containing projection surface information.
- [static func stereoView(CMStereoViewComponents) -> CMTypedTag<CMStereoViewComponents>](cmtag-swift.class/stereoview(_:).md)
  Creates a tag containing eye information for 3D video.
- [static func stereoViewInterpretation(CMStereoViewInterpretationOptions) -> CMTypedTag<CMStereoViewInterpretationOptions>](cmtag-swift.class/stereoviewinterpretation(_:).md)
  Creates a tag containing information on how to interpret stereo view metadata.
- [static func trackID(CMPersistentTrackID) -> CMTypedTag<CMPersistentTrackID>](cmtag-swift.class/trackid(_:).md)
  Creates a tag containing a track ID.
- [static func videoLayerID(Int64) -> CMTypedTag<Int64>](cmtag-swift.class/videolayerid(_:).md)
  Creates a tag containing a video layer ID.
- [init(rawCategory: CMTag.RawCategory, rawTagValue: CMTag.Value)](cmtag-swift.class/init(rawcategory:rawtagvalue:).md)
  Creates a new tag from a category and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtag-swift.class/packingtype(_:))*