# pixelFormat(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Type Method

Creates a tag containing pixel format information.

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
static func pixelFormat(_ value: OSType) -> CMTypedTag<OSType>
```

## Return Value

A new typed tag containing the pixel format represented by `value`.

## Parameters

- `value`: The pixel format for this tag. Use a constant from the framework that renders video content. For example, rendering to a [CVPixelBuffer](../../CoreVideo/cvpixelbuffer-q2e.md) should use a constant from [Pixel Format Identifiers](../../CoreVideo/pixel-format-identifiers.md).

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
- [init(rawCategory: CMTag.RawCategory, rawTagValue: CMTag.Value)](./init%28rawcategory,rawtagvalue%29.md)
  Creates a new tag from a category and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtag-swift.class/pixelformat(_:))*