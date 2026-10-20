# CMTypedTag.Category

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

An identifier for a media tag category.

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
struct Category
```

## Topics

### Creating Typed Categories
- [static var channelID: CMTypedTag<Int64>.Category](./category-swift.struct/channelid.md)
  A category used for tagging a channel ID.
- [static var mediaSubType: CMTypedTag<CMFormatDescription.MediaSubType>.Category](./category-swift.struct/mediasubtype.md)
  A category used for tagging media subtype metadata.
- [static var mediaType: CMTypedTag<CMFormatDescription.MediaType>.Category](./category-swift.struct/mediatype.md)
  A category used for tagging media type metadata.
- [static var packingType: CMTypedTag<CMPackingType>.Category](./category-swift.struct/packingtype.md)
  A category used for tagging frame-packing information.
- [static var pixelFormat: CMTypedTag<OSType>.Category](./category-swift.struct/pixelformat.md)
  A category used for tagging pixel format information.
- [static var projectionType: CMTypedTag<CMProjectionType>.Category](./category-swift.struct/projectiontype.md)
  A category used for tagging projection surface information.
- [static var stereoView: CMTypedTag<CMStereoViewComponents>.Category](./category-swift.struct/stereoview.md)
  A category used for tagging eye information for 3D video.
- [static var stereoViewInterpretation: CMTypedTag<CMStereoViewInterpretationOptions>.Category](./category-swift.struct/stereoviewinterpretation.md)
  A category used for tagging how to interpret stereo view metadata.
- [static var trackID: CMTypedTag<CMPersistentTrackID>.Category](./category-swift.struct/trackid.md)
  A category used for tagging a track ID.
- [static var videoLayerID: CMTypedTag<Int64>.Category](./category-swift.struct/videolayerid.md)
  A category used for tagging a video layer ID.
### Getting Raw Categories
- [let rawCategory: CMTypedTag<TypedValue>.RawCategory](./category-swift.struct/rawcategory.md)
  The raw 64-bit representation of the tag’s category.
### Transforming Tag Values
- [func tagValue(for: TypedValue) -> CMTag.Value](./category-swift.struct/tagvalue%28for%29.md)
  Convert a typed value to a raw tag value for this category.
- [func value(for: CMTag.Value) -> TypedValue?](./category-swift.struct/value%28for%29.md)
  Convert a tag value into a typed value valid for this category, if possible.
### Initializers
- [init(rawCategory: CMTypedTag<TypedValue>.RawCategory, valueForTagValue: (CMTag.Value) -> TypedValue?, tagValueForValue: (TypedValue) -> CMTag.Value)](./category-swift.struct/init%28rawcategory,valuefortagvalue,tagvalueforvalue%29.md)
  Creates a new tag category instance with defined mappings between a raw and typed tag value.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtypedtag/category-swift.struct)*