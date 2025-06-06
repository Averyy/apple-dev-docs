# CMTag

**Framework**: Core Media  
**Kind**: class

A tag to set additional metadata on media buffers.

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
class CMTag
```

#### Overview

The Core Media framework uses tags to describe the properties of media channels. Each tag consists of a category and a value, both of which are 64 bits in size.

> ❗ **Important**:  Tag data can only contain values that can be safely stored on disk. In particular, [`CMTag`](cmtag-swift.class.md) values can’t contain a pointer. If you need to refer to another media element or in-memory data as part of a tag, use a buffer index or other constant.

 Tag data can only contain values that can be safely stored on disk. In particular, [`CMTag`](cmtag-swift.class.md) values can’t contain a pointer. If you need to refer to another media element or in-memory data as part of a tag, use a buffer index or other constant.

It’s recommended to use [`CMTypedTag`](cmtypedtag.md) instances where possible to preserve type safety.

## Topics

### Creating Tags
- [static func channelID(Int64) -> CMTypedTag<Int64>](cmtag-swift.class/channelid(_:).md)
  Creates a new channel ID tag from an integer.
- [static func mediaSubType(CMFormatDescription.MediaSubType) -> CMTypedTag<CMFormatDescription.MediaSubType>](cmtag-swift.class/mediasubtype(_:).md)
  Creates a tag containing media subtype metadata.
- [static func mediaType(CMFormatDescription.MediaType) -> CMTypedTag<CMFormatDescription.MediaType>](cmtag-swift.class/mediatype(_:).md)
  Creates a tag containing media type metadata.
- [static func packingType(CMPackingType) -> CMTypedTag<CMPackingType>](cmtag-swift.class/packingtype(_:).md)
  Creates a tag containing frame-packing information.
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
### Inspecting Tags
- [let rawCategory: CMTag.RawCategory](cmtag-swift.class/rawcategory-swift.property.md)
  The raw 64-bit representation of the tag’s category.
- [let rawTagValue: CMTag.Value](cmtag-swift.class/rawtagvalue.md)
  The tag’s contained value.
- [func value<T>(onlyIfMatching: CMTypedTag<T>.Category) -> T?](cmtag-swift.class/value(onlyifmatching:).md)
  Retrieves a tag’s value as a specific type, if and only if it matches a category.
### Wrapped Values
- [CMTag.Value](cmtag-swift.class/value.md)
  A wrapper type for a value associated with a tag.
### Type Aliases
- [typealias RawCategory](cmtag-swift.class/rawcategory-swift.typealias.md)
  The raw 64-bit representation of a tag’s category.

## Relationships

### Inherited By
- [CMTypedTag](cmtypedtag.md)
### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [CMMetadata APIs](cmmetadata.md)
  The APIs for working with the framework’s Metadata Identifier Services and Metadata Data Type Registry.
- [CMTag APIs](cmtag-api.md)
  Types and interfaces for working with Core Media tags.
- [class CMTypedTag](cmtypedtag.md)
  A tag to set additional metadata on media buffers, with an associated Swift type for its value.
- [CMTagCollection APIs](cmtagcollection.md)
  Objective-C types and interfaces for working with Core Media tag collections.
- [enum CMProjectionType](cmprojectiontype.md)
  Constants describing the projection surface information in a 3D video buffer or channel.
- [struct CMStereoViewComponents](cmstereoviewcomponents.md)
  Constants describing the stereo views contained within a buffer or channel.
- [struct CMStereoViewInterpretationOptions](cmstereoviewinterpretationoptions.md)
  Create a set of stereo view interpretation options from a constant.
- [enum CMPackingType](cmpackingtype.md)
  The type of packing within each video frame, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtag-swift.class)*