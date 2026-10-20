# CVReadOnlyPixelBuffer

**Framework**: Core Video  
**Kind**: class  
**Role**: Class

CVReadOnlyPixelBuffer provides an immutable view of the pixel data held by the pixel buffer.

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
final class CVReadOnlyPixelBuffer
```

## Topics

### Initializers
- [init(consuming CVMutablePixelBuffer)](./cvreadonlypixelbuffer/init%28_%29.md)
  Initialize a read-only pixel buffer by consuming a mutable pixel buffer value.
- [init(unsafeBuffer: sending CVPixelBuffer)](./cvreadonlypixelbuffer/init%28unsafebuffer%29.md)
  Initialize a read-only pixel buffer by transferring existing CVPixelBuffer value.
### Instance Methods
- [func withUnsafeBuffer<R>((CVPixelBuffer) throws -> sending R) rethrows -> sending R](./cvreadonlypixelbuffer/withunsafebuffer%28_%29.md)

## Relationships

### Conforms To
- [CMSampleBuffer.Content](../CoreMedia/cmsamplebuffer/content.md)
- [CMSampleBuffer.ContentWithFormatDescription](../CoreMedia/cmsamplebuffer/contentwithformatdescription.md)
- [CVBufferRepresentable](./cvbufferrepresentable.md)
- [CVImageBufferRepresentable](./cvimagebufferrepresentable.md)
- [CVPixelBufferRepresentable](./cvpixelbufferrepresentable.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [InferenceValue.ViewRepresentable](../CoreAI/inferencevalue/viewrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Swift overlay types
- [struct CVMutablePixelBuffer](./cvmutablepixelbuffer.md)
  CVMutablePixelBuffer provides read-write access to the pixel data and attachments.
- [struct CVPixelBufferAttributes](./cvpixelbufferattributes.md)
  A partial set of pixel buffer creation attributes. This struct is useful for conveying partial requirements for pixel buffers to clients. This struct makes all properties of `CVPixelBuffer/CreationAttributes` optional.
- [struct CVPixelBufferCreationAttributes](./cvpixelbuffercreationattributes.md)
  Attributes needed for creating a pixel buffer.
- [struct CVPixelBufferPadding](./cvpixelbufferpadding.md)
  Padding pixels around the CVPixelBuffer
- [struct CVPixelBufferPlaneProperties](./cvpixelbufferplaneproperties.md)
  Properties of a plane of pixels in pixel buffer
- [struct CVProResRawMetadata](./cvproresrawmetadata.md)
  Metadata associated with ProRes RAW images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvreadonlypixelbuffer)*