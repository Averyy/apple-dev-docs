# init(rawCategory:rawTagValue:)

**Framework**: Core Media  
**Kind**: init  
**Role**: Initializer

Creates a new tag from a category and value.

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
init(rawCategory: CMTag.RawCategory, rawTagValue: CMTag.Value)
```

#### Discussion

> ❗ **Important**:  To ensure that your tags have a valid category, create new [`CMTag`](../cmtag-swift.class.md) instances with a static method listed in Creating Tags.

## Parameters

- `rawCategory`: The category of the created tag.
- `rawTagValue`: The value of the created tag.

## See Also

### Creating Tags
- [static func channelID(Int64) -> CMTypedTag<Int64>](./channelid%28_%29.md)
  Creates a new channel ID tag from an integer.
- [static func mediaSubType(CMFormatDescription.MediaSubType) -> CMTypedTag<CMFormatDescription.MediaSubType>](./mediasubtype%28_%29.md)
  Creates a tag containing media subtype metadata.
- [static func mediaType(CMFormatDescription.MediaType) -> CMTypedTag<CMFormatDescription.MediaType>](./mediatype%28_%29.md)
  Creates a tag containing media type metadata.
- [static func packingType(CMPackingType) -> CMTypedTag<CMPackingType>](./packingtype%28_%29.md)
  Creates a tag containing frame-packing information.
- [static func pixelFormat(OSType) -> CMTypedTag<OSType>](./pixelformat%28_%29.md)
  Creates a tag containing pixel format information.
- [static func projectionType(CMProjectionType) -> CMTypedTag<CMProjectionType>](./projectiontype%28_%29.md)
  Creates a tag containing projection surface information.
- [static func stereoView(CMStereoViewComponents) -> CMTypedTag<CMStereoViewComponents>](./stereoview%28_%29.md)
  Creates a tag containing eye information for 3D video.
- [static func stereoViewInterpretation(CMStereoViewInterpretationOptions) -> CMTypedTag<CMStereoViewInterpretationOptions>](./stereoviewinterpretation%28_%29.md)
  Creates a tag containing information on how to interpret stereo view metadata.
- [static func trackID(CMPersistentTrackID) -> CMTypedTag<CMPersistentTrackID>](./trackid%28_%29.md)
  Creates a tag containing a track ID.
- [static func videoLayerID(Int64) -> CMTypedTag<Int64>](./videolayerid%28_%29.md)
  Creates a tag containing a video layer ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtag-swift.class/init(rawcategory:rawtagvalue:))*