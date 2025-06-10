# CVBuffer.CreationAttributes

**Framework**: Core Video  
**Kind**: struct

Attributes needed for creating a pixel buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)
- Unknown ?+ - Deprecated

## Declaration

```swift
struct CreationAttributes
```

## Topics

### Initializers
- [init?(CVBuffer.Attributes)](cvbuffer/creationattributes/init(_:).md)
  Convert Attributes to CreationAttributes. This init will fail if [`pixelFormatType`](cvbuffer/creationattributes/pixelformattype.md) or [`size`](cvbuffer/creationattributes/size.md) properties are absent.
- [init(pixelFormatType: CVPixelFormatType, size: CVImageSize, compatibility: CVPixelFormatDescription.Compatibility, bytesPerRowAlignment: Int?, planeAlignment: Int?, extendedPixels: CVPixelBufferPadding?)](cvbuffer/creationattributes/init(pixelformattype:size:compatibility:bytesperrowalignment:planealignment:extendedpixels:).md)
### Instance Properties
- [var backing: CVBuffer.CreationAttributes.Backing](cvbuffer/creationattributes/backing-swift.property.md)
  Defines how the memory for the pixel buffer backing is allocated. IOSurface backed pixel buffers can be shared between CPU and GPU also across process boundaries. Defaults to `Backing.ioSurface`.
- [var bytesPerRowAlignment: Int?](cvbuffer/creationattributes/bytesperrowalignment.md)
  The number of bytes per row in the pixel buffer must be a multiple of this number.
- [var compatibility: CVPixelFormatDescription.Compatibility](cvbuffer/creationattributes/compatibility.md)
  Defines interoperability of pixel buffers with other frameworks
- [var extendedPixels: CVPixelBufferPadding?](cvbuffer/creationattributes/extendedpixels.md)
  Sets the amount of extended pixel padding in the pixel buffer.
- [var pixelFormatType: CVPixelFormatType](cvbuffer/creationattributes/pixelformattype.md)
  Format of the pixel buffer bytes
- [var planeAlignment: Int?](cvbuffer/creationattributes/planealignment.md)
  Planes start on a byte number that’s a multiple of this value.
- [var size: CVImageSize](cvbuffer/creationattributes/size.md)
  Size of the buffer in pixels
### Enumerations
- [CVBuffer.CreationAttributes.Backing](cvbuffer/creationattributes/backing-swift.enum.md)
  Type of backing storage used by the pixel buffer

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer/creationattributes)*