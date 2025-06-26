# CVPixelBufferRepresentable

**Framework**: Core Video  
**Kind**: protocol

CVPixelBufferRepresentable protocol is a sealed protocol intended to be implemented by the types in CoreVideo framework. This protocol facilitates Swift types that wrap a value of CVPixelBuffer type.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol CVPixelBufferRepresentable : CVImageBufferRepresentable, ~Copyable
```

## Topics

### Instance Properties
- [var creationAttributes: CVPixelBufferCreationAttributes](cvpixelbufferrepresentable/creationattributes.md)
  Attributes used for creating this pixel buffer
- [var extendedPixels: CVPixelBufferPadding](cvpixelbufferrepresentable/extendedpixels.md)
  Padding pixels around this pixel buffer
- [var isPlanar: Bool](cvpixelbufferrepresentable/isplanar.md)
  True if the buffer was created with support for one or more planes.
- [var pixelFormatType: CVPixelFormatType](cvpixelbufferrepresentable/pixelformattype.md)
  Pixel format of this pixel buffer
- [var planeCount: Int](cvpixelbufferrepresentable/planecount.md)
  Number of planes in this pixel buffer. This value will always be greater than 0. `planeCount` is more efficient to access than count property of `planes`. A non-planar pixel buffer implicitly defines a single plane. To check if the pixel buffer was defined with planes use [`isPlanar`](cvpixelbufferrepresentable/isplanar.md) property.
- [var planeProperties: [CVPixelBufferPlaneProperties]](cvpixelbufferrepresentable/planeproperties.md)
  Properties of all the planes in this pixel buffer. This array will contain at least one element. In case of non-planar pixel buffers, the first value represents the entire pixel data.
- [var size: CVImageSize](cvpixelbufferrepresentable/size.md)
  Size of the pixel buffer in pixels
### Instance Methods
- [func accessUnsafeRawPlaneBytes<R>(([(properties: CVPixelBufferPlaneProperties, bytes: UnsafeRawBufferPointer)]) throws -> sending R) rethrows -> sending R](cvpixelbufferrepresentable/accessunsaferawplanebytes(_:).md)
  Access the pixels in the planes contained within this buffer. The base address is locked for reading during the execution of the block.
- [func isCompatibleWith(CVPixelBufferAttributes) -> Bool](cvpixelbufferrepresentable/iscompatiblewith(_:)-9fsoy.md)
  Returns `true` if the pixel buffer is compatible with the specified attributes.
- [func isCompatibleWith(CVPixelBufferCreationAttributes) -> Bool](cvpixelbufferrepresentable/iscompatiblewith(_:)-b775.md)
  Returns `true` if the pixel buffer is compatible with the specified creation attributes.
- [func withUnsafeBackingIOSurfaceIfPresent<R>((IOSurface) throws -> sending R) rethrows -> sending R?](cvpixelbufferrepresentable/withunsafebackingiosurfaceifpresent(_:).md)
  Access the IOSurface backing the pixel buffer if present.

## Relationships

### Inherits From
- [CVBufferRepresentable](cvbufferrepresentable.md)
- [CVImageBufferRepresentable](cvimagebufferrepresentable.md)
### Conforming Types
- [CVMutablePixelBuffer](cvmutablepixelbuffer.md)
- [CVReadOnlyPixelBuffer](cvreadonlypixelbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferrepresentable)*