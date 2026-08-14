# CVImagePixelAspectRatio

**Framework**: Core Video  
**Kind**: struct

Aspect ratio of each pixel in the image buffer.

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
struct CVImagePixelAspectRatio
```

## Topics

### Initializers
- [init(horizontalSpacing: Float, verticalSpacing: Float)](cvimagepixelaspectratio/init(horizontalspacing:verticalspacing:).md)
### Instance Properties
- [var horizontalSpacing: Float](cvimagepixelaspectratio/horizontalspacing.md)
  The horizontal component of the image buffer aspect ratio.
- [var verticalSpacing: Float](cvimagepixelaspectratio/verticalspacing.md)
  The vertical component of the image buffer aspect ratio.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
- [Copyable](../swift/copyable.md)
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
- [struct CVImageDisplayMaskRectangle](cvimagedisplaymaskrectangle.md)
  Specifies the rectangular display area within the image.
- [struct CVImageStereoDisplayMaskRectangle](cvimagestereodisplaymaskrectangle.md)
  Specifies the rectangular display area within a view of stereo image.
- [struct CVImageChromaField](cvimagechromafield.md)
  Information about chroma field in the 2VUY format image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagepixelaspectratio)*