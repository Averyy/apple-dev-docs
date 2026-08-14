# CVImageStereoDisplayMaskRectangle

**Framework**: Core Video  
**Kind**: struct

Specifies the rectangular display area within a view of stereo image.

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
struct CVImageStereoDisplayMaskRectangle
```

#### Overview

To address window violations in stereo video, points insetting the left and right edges of the rectangle are supported through in addition to the mask rectangle, allowing the description of the “extended raster rectangle”.

## Topics

### Structures
- [CVImageStereoDisplayMaskRectangle.EdgePoint](cvimagestereodisplaymaskrectangle/edgepoint.md)
  Specifies inset point on a vertical edge of the rectangle.
### Initializers
- [init(maskRectangle: CVImageDisplayMaskRectangle, leftEdgePoints: [CVImageStereoDisplayMaskRectangle.EdgePoint], rightEdgePoints: [CVImageStereoDisplayMaskRectangle.EdgePoint])](cvimagestereodisplaymaskrectangle/init(maskrectangle:leftedgepoints:rightedgepoints:).md)
### Instance Properties
- [var leftEdgePoints: [CVImageStereoDisplayMaskRectangle.EdgePoint]](cvimagestereodisplaymaskrectangle/leftedgepoints.md)
  Inset points on the left edge of the rectangle.
- [var maskRectangle: CVImageDisplayMaskRectangle](cvimagestereodisplaymaskrectangle/maskrectangle.md)
  Rectangular display area within the image.
- [var rightEdgePoints: [CVImageStereoDisplayMaskRectangle.EdgePoint]](cvimagestereodisplaymaskrectangle/rightedgepoints.md)
  Inset points on the right edge of the rectangle.

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
- [struct CVImageDisplayMaskRectangle](cvimagedisplaymaskrectangle.md)
  Specifies the rectangular display area within the image.
- [struct CVImageChromaField](cvimagechromafield.md)
  Information about chroma field in the 2VUY format image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagestereodisplaymaskrectangle)*