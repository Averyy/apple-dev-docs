# CVImageSize

**Framework**: Core Video  
**Kind**: struct

Size of image buffer expressed as pixel count.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct CVImageSize
```

#### Overview

This should be used when the sizes must be specified as exact integer width & height. Otherwise, prefer `CGSize` as it is more widely used.

## Topics

### Initializers
- [init(CGSize, rounded: FloatingPointRoundingRule)](cvimagesize/init(_:rounded:).md)
  Convert `CGSize` to [`CVImageSize`](cvimagesize.md) using the given rounding rule.
- [init(width: Int, height: Int)](cvimagesize/init(width:height:).md)
  Create an instance with given width and height
### Instance Properties
- [var height: Int](cvimagesize/height.md)
  Image height in pixels
- [var width: Int](cvimagesize/width.md)
  Image width in pixels
### Type Properties
- [static let zero: CVImageSize](cvimagesize/zero.md)
  Size with zero width and height

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [typealias CVImageBuffer](cvimagebuffer.md)
  A reference to a Core Video image buffer.
- [enum CVImageBufferOriginPosition](cvimagebufferoriginposition.md)
- [struct CVImageCleanAperture](cvimagecleanaperture.md)
  An image’s clean aperture is a region of video to display.
- [struct CVImagePixelAspectRatio](cvimagepixelaspectratio.md)
  Aspect ratio of each pixel in the image buffer.
- [struct CVImageDisplayMaskRectangle](cvimagedisplaymaskrectangle.md)
  Specifies the rectangular display area within the image.
- [struct CVImageStereoDisplayMaskRectangle](cvimagestereodisplaymaskrectangle.md)
  Specifies the rectangular display area within a view of stereo image.
- [struct CVImageChromaField](cvimagechromafield.md)
  Information about chroma field in the 2VUY format image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagesize)*