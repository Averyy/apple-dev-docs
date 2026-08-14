# CVImageDisplayMaskRectangle

**Framework**: Core Video  
**Kind**: struct

Specifies the rectangular display area within the image.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct CVImageDisplayMaskRectangle
```

#### Overview

The mask is specified relative to a reference raster width and height that should be scaled to the image buffer dimensions. The origin (0, 0) is at the top-left.

## Topics

### Initializers
- [init(left: UInt16, top: UInt16, width: UInt16, height: UInt16, referenceRasterWidth: UInt16, referenceRasterHeight: UInt16)](cvimagedisplaymaskrectangle/init(left:top:width:height:referencerasterwidth:referencerasterheight:).md)
### Instance Properties
- [var height: UInt16](cvimagedisplaymaskrectangle/height.md)
  The height of the rectangle starting at rectangle’s top offset toward the rectangle’s bottom edge.
- [var left: UInt16](cvimagedisplaymaskrectangle/left.md)
  The horizontal pixel offset of the rectangle from the left of the bounding raster.
- [var referenceRasterHeight: UInt16](cvimagedisplaymaskrectangle/referencerasterheight.md)
  Specifies the height in pixels of the 2D coordinate system to define the rectangle.
- [var referenceRasterWidth: UInt16](cvimagedisplaymaskrectangle/referencerasterwidth.md)
  The width in pixels of the 2D coordinate system to define the rectangle.
- [var top: UInt16](cvimagedisplaymaskrectangle/top.md)
  The vertical pixel offset of the rectangle from the top of the bounding raster.
- [var width: UInt16](cvimagedisplaymaskrectangle/width.md)
  The width of the rectangle starting at rectangle’s left offset toward the rectangle’s right edge.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [typealias CVImageBuffer](cvimagebuffer.md)
  A reference to a Core Video image buffer.
- [struct CVImageSize](cvimagesize.md)
  Size of image buffer expressed as pixel count.
- [enum CVImageBufferOriginPosition](cvimagebufferoriginposition.md)
- [struct CVImageCleanAperture](cvimagecleanaperture.md)
  An image’s clean aperture is a region of video to display.
- [struct CVImagePixelAspectRatio](cvimagepixelaspectratio.md)
  Aspect ratio of each pixel in the image buffer.
- [struct CVImageStereoDisplayMaskRectangle](cvimagestereodisplaymaskrectangle.md)
  Specifies the rectangular display area within a view of stereo image.
- [struct CVImageChromaField](cvimagechromafield.md)
  Information about chroma field in the 2VUY format image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagedisplaymaskrectangle)*