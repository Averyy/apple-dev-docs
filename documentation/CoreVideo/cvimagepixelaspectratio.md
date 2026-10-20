# CVImagePixelAspectRatio

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

Aspect ratio of each pixel in the image buffer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@frozen
struct CVImagePixelAspectRatio
```

## Topics

### Initializers
- [init(horizontalSpacing: Float, verticalSpacing: Float)](./cvimagepixelaspectratio/init%28horizontalspacing,verticalspacing%29.md)
### Instance Properties
- [var horizontalSpacing: Float](./cvimagepixelaspectratio/horizontalspacing.md)
  The horizontal component of the image buffer aspect ratio.
- [var verticalSpacing: Float](./cvimagepixelaspectratio/verticalspacing.md)
  The vertical component of the image buffer aspect ratio.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CVAttachmentValueRepresentable](./cvattachmentvaluerepresentable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data types
- [typealias CVImageBuffer](./cvimagebuffer.md)
  A reference to a Core Video image buffer.
- [struct CVImageSize](./cvimagesize.md)
  Size of image buffer expressed as pixel count.
- [enum CVImageBufferOriginPosition](./cvimagebufferoriginposition.md)
- [struct CVImageCleanAperture](./cvimagecleanaperture.md)
  An image’s clean aperture is a region of video to display.
- [struct CVImageDisplayMaskRectangle](./cvimagedisplaymaskrectangle.md)
  Specifies the rectangular display area within the image.
- [struct CVImageStereoDisplayMaskRectangle](./cvimagestereodisplaymaskrectangle.md)
  Specifies the rectangular display area within a view of stereo image.
- [struct CVImageChromaField](./cvimagechromafield.md)
  Information about chroma field in the 2VUY format image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagepixelaspectratio)*