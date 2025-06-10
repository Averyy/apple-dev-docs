# CMProjectionType

**Framework**: Core Media  
**Kind**: enum

Constants describing the projection surface information in a 3D video buffer or channel.

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
enum CMProjectionType
```

## Topics

### Projection Surfaces
- [CMProjectionType.rectangular](cmprojectiontype/rectangular.md)
  Video content displays on a flat, rectangular 2D surface.
- [CMProjectionType.equirectangular](cmprojectiontype/equirectangular.md)
  Video content displays as a 360 degree equirectangular projection.
- [CMProjectionType.halfEquirectangular](cmprojectiontype/halfequirectangular.md)
  Video content displays as a 180 degree equirectangular projection.
- [CMProjectionType.fisheye](cmprojectiontype/fisheye.md)
  Video content displays as a fisheye projection.
### Enumeration Cases
- [CMProjectionType.parametricImmersive](cmprojectiontype/parametricimmersive.md)
### Initializers
- [init?(rawValue: UInt64)](cmprojectiontype/init(rawvalue:).md)

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
- [struct CMStereoViewComponents](cmstereoviewcomponents.md)
  Constants describing the stereo views contained within a buffer or channel.
- [struct CMStereoViewInterpretationOptions](cmstereoviewinterpretationoptions.md)
  Create a set of stereo view interpretation options from a constant.
- [enum CMPackingType](cmpackingtype.md)
  The type of packing within each video frame, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmprojectiontype)*