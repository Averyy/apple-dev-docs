# CVImageChromaField

**Framework**: Core Video  
**Kind**: struct

Information about chroma field in the 2VUY format image data.

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
struct CVImageChromaField
```

## Topics

### Initializers
- [init(fieldLocation: CVImageChromaField.FieldLocation, subsampling: CVImageChromaField.ChromaSubsampling)](cvimagechromafield/init(fieldlocation:subsampling:).md)
### Instance Properties
- [var fieldLocation: CVImageChromaField.FieldLocation](cvimagechromafield/fieldlocation-swift.property.md)
- [var subsampling: CVImageChromaField.ChromaSubsampling](cvimagechromafield/subsampling.md)
### Enumerations
- [CVImageChromaField.ChromaSubsampling](cvimagechromafield/chromasubsampling.md)
  Original format of subsampled data in the image buffer before conversion to 422/2vuy format.
- [CVImageChromaField.FieldLocation](cvimagechromafield/fieldlocation-swift.enum.md)
  Indicates chroma sample location for progressive-scan & interlaced image data.
- [CVImageChromaField.SampleLocation](cvimagechromafield/samplelocation.md)
  Indicates the locations of the chroma sample in the image buffer.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
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
- [struct CVImageStereoDisplayMaskRectangle](cvimagestereodisplaymaskrectangle.md)
  Specifies the rectangular display area within a view of stereo image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagechromafield)*