# CVImageCleanAperture

**Framework**: Core Video  
**Kind**: struct

An image’s clean aperture is a region of video to display.

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
@frozen
struct CVImageCleanAperture
```

#### Overview

This represents a rectangle within the image that’s free from transition artifacts caused by the encoding of the signal.

## Topics

### Initializers
- [init(width: Float, height: Float, horizontalOffset: Float, verticalOffset: Float)](cvimagecleanaperture/init(width:height:horizontaloffset:verticaloffset:).md)
### Instance Properties
- [var height: Float](cvimagecleanaperture/height.md)
  Height of the clean aperture.
- [var horizontalOffset: Float](cvimagecleanaperture/horizontaloffset.md)
  Horizontal offset from the center of the image buffer.
- [var verticalOffset: Float](cvimagecleanaperture/verticaloffset.md)
  Vertical offset from the center of the image buffer.
- [var width: Float](cvimagecleanaperture/width.md)
  Width of the clean aperture.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [typealias CVImageBuffer](cvimagebuffer.md)
  A reference to a Core Video image buffer.
- [struct CVImageSize](cvimagesize.md)
  Size of image buffer expressed as pixel count.
- [enum CVImageBufferOriginPosition](cvimagebufferoriginposition.md)
- [struct CVImagePixelAspectRatio](cvimagepixelaspectratio.md)
  Aspect ratio of each pixel in the image buffer.
- [struct CVImageDisplayMaskRectangle](cvimagedisplaymaskrectangle.md)
  Specifies the rectangular display area within the image.
- [struct CVImageStereoDisplayMaskRectangle](cvimagestereodisplaymaskrectangle.md)
  Specifies the rectangular display area within a view of stereo image.
- [struct CVImageChromaField](cvimagechromafield.md)
  Information about chroma field in the 2VUY format image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagecleanaperture)*