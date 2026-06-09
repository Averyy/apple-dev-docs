# CVImageBuffer

**Framework**: Core Video  
**Kind**: typealias

A reference to a Core Video image buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
typealias CVImageBuffer = CVBuffer
```

#### Discussion

An image buffer is an abstract type representing Core Video buffers that hold images. In Core Video, pixel buffers, OpenGL buffers, and OpenGL textures all derive from the image buffer type.

## See Also

- [struct CVImageSize](cvimagesize.md)
  Size of image buffer expressed as pixel count.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebuffer)*