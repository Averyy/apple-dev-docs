# CMStereoViewInterpretationOptions

**Framework**: Core Media  
**Kind**: struct

Create a set of stereo view interpretation options from a constant.

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
struct CMStereoViewInterpretationOptions
```

## Topics

### Stereo View Options
- [static var additionalViews: CMStereoViewInterpretationOptions](cmstereoviewinterpretationoptions/additionalviews.md)
  A flag indicating that the video content contains additional views beyond the left or right eye.
- [static var stereoOrderReversed: CMStereoViewInterpretationOptions](cmstereoviewinterpretationoptions/stereoorderreversed.md)
  Changes the default ordering of eye data, switching it from left-to-right to right-to-left.
### Initializers
- [init(rawValue: UInt64)](cmstereoviewinterpretationoptions/init(rawvalue:).md)
  Create a new option set with a given value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [enum CMPackingType](cmpackingtype.md)
  The type of packing within each video frame, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmstereoviewinterpretationoptions)*