# CMPackingType

**Framework**: Core Media  
**Kind**: enum

The type of packing within each video frame, if any.

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
enum CMPackingType
```

#### Overview

Frame-packed video contains both the left and right eye images on a single video track. With frame-packed video, use the appropriate Frame Arrangement.

## Topics

### Frame Arrangement
- [CMPackingType.none](cmpackingtype/none.md)
  Each frame contains only a single image, and isn’t frame-packed.
- [CMPackingType.sideBySide](cmpackingtype/sidebyside.md)
  The video contains packed frames that have a left eye image on the left and right eye image on the right.
- [CMPackingType.overUnder](cmpackingtype/overunder.md)
  The video contains packed frames that have a left eye image on the top and right eye image on the bottom.
### Initializers
- [init?(rawValue: UInt64)](cmpackingtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CMMetadata APIs](cmmetadata.md)
  The APIs for working with the framework’s Metadata Identifier Services and Metadata Data Type Registry.
- [CMTag APIs](cmtag-api.md)
  Types and interfaces for working with Core Media tags.
- [class CMTag](cmtag-swift.class.md)
  A tag to set additional metadata on media buffers.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmpackingtype)*