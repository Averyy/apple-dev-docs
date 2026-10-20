# CVBuffer.CreationAttributes

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

Attributes needed for creating a pixel buffer.

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
struct CreationAttributes
```

## Topics

### Initializers
- [init?(CVBuffer.Attributes)](./creationattributes/init%28_%29.md)
  Convert Attributes to CreationAttributes. This init will fail if [`pixelFormatType`](./creationattributes/pixelformattype.md) or [`size`](./creationattributes/size.md) properties are absent.
- [init(pixelFormatType: CVPixelFormatType, size: CVImageSize, compatibility: CVPixelFormatDescription.Compatibility, bytesPerRowAlignment: Int?, planeAlignment: Int?, extendedPixels: CVPixelBufferPadding?)](./creationattributes/init%28pixelformattype,size,compatibility,bytesperrowalignment,planealignment,extendedpixels%29.md)
### Instance Properties
- [var backing: CVBuffer.CreationAttributes.Backing](./creationattributes/backing-swift.property.md)
  Defines how the memory for the pixel buffer backing is allocated. IOSurface backed pixel buffers can be shared between CPU and GPU also across process boundaries. Defaults to `Backing.ioSurface`.
- [var bytesPerRowAlignment: Int?](./creationattributes/bytesperrowalignment.md)
  The number of bytes per row in the pixel buffer must be a multiple of this number.
- [var compatibility: CVPixelFormatDescription.Compatibility](./creationattributes/compatibility.md)
  Defines interoperability of pixel buffers with other frameworks
- [var extendedPixels: CVPixelBufferPadding?](./creationattributes/extendedpixels.md)
  Sets the amount of extended pixel padding in the pixel buffer.
- [var pixelFormatType: CVPixelFormatType](./creationattributes/pixelformattype.md)
  Format of the pixel buffer bytes
- [var planeAlignment: Int?](./creationattributes/planealignment.md)
  Planes start on a byte number that’s a multiple of this value.
- [var size: CVImageSize](./creationattributes/size.md)
  Size of the buffer in pixels
### Enumerations
- [CVBuffer.CreationAttributes.Backing](./creationattributes/backing-swift.enum.md)
  Type of backing storage used by the pixel buffer

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer/creationattributes)*