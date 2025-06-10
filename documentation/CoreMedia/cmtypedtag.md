# CMTypedTag

**Framework**: Core Media  
**Kind**: class

A tag to set additional metadata on media buffers, with an associated Swift type for its value.

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
class CMTypedTag<TypedValue> where TypedValue : Sendable
```

## Topics

### Creating Typed Tags
- [init(category: CMTypedTag<TypedValue>.Category, value: TypedValue)](cmtypedtag/init(category:value:).md)
  Creates a new instance with the given category and value.
### Inspecting Typed Tags
- [let category: CMTypedTag<TypedValue>.Category](cmtypedtag/category-swift.property.md)
  The category of the tag.
- [var value: TypedValue](cmtypedtag/value.md)
  The value of the tag, represented as its appropriate type.
### Typed Tag Categories
- [CMTypedTag.Category](cmtypedtag/category-swift.struct.md)
  An identifier for a media tag category.

## Relationships

### Inherits From
- [CMTag](cmtag-swift.class.md)
### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CMMetadata APIs](cmmetadata.md)
  The APIs for working with the framework’s Metadata Identifier Services and Metadata Data Type Registry.
- [CMTag APIs](cmtag-api.md)
  Types and interfaces for working with Core Media tags.
- [class CMTag](cmtag-swift.class.md)
  A tag to set additional metadata on media buffers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtypedtag)*