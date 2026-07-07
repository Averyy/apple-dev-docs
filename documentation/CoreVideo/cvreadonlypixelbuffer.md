# CVReadOnlyPixelBuffer

**Framework**: Core Video  
**Kind**: class

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
- [init(consuming CVMutablePixelBuffer)](cvreadonlypixelbuffer/init(_:).md)
  Initialize a read-only pixel buffer by consuming a mutable pixel buffer value.
- [init(unsafeBuffer: sending CVPixelBuffer)](cvreadonlypixelbuffer/init(unsafebuffer:).md)
  Initialize a read-only pixel buffer by transferring existing CVPixelBuffer value.
### Instance Methods
- [func withUnsafeBuffer<R>((CVPixelBuffer) throws -> sending R) rethrows -> sending R](cvreadonlypixelbuffer/withunsafebuffer(_:).md)

## Relationships

### Conforms To
- [CMSampleBuffer.Content](../CoreMedia/CMSampleBuffer/Content.md)
- [CMSampleBuffer.ContentWithFormatDescription](../CoreMedia/CMSampleBuffer/ContentWithFormatDescription.md)
- [CVBufferRepresentable](cvbufferrepresentable.md)
- [CVImageBufferRepresentable](cvimagebufferrepresentable.md)
- [CVPixelBufferRepresentable](cvpixelbufferrepresentable.md)
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [InferenceValue.ViewRepresentable](../CoreAI/InferenceValue/ViewRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CVMutablePixelBuffer](cvmutablepixelbuffer.md)
  CVMutablePixelBuffer provides read-write access to the pixel data and attachments.
- [struct CVPixelBufferAttributes](cvpixelbufferattributes.md)
  A partial set of pixel buffer creation attributes. This struct is useful for conveying partial requirements for pixel buffers to clients. This struct makes all properties of `CVPixelBuffer/CreationAttributes` optional.
- [struct CVPixelBufferCreationAttributes](cvpixelbuffercreationattributes.md)
  Attributes needed for creating a pixel buffer.
- [struct CVPixelBufferPadding](cvpixelbufferpadding.md)
  Padding pixels around the CVPixelBuffer
- [struct CVPixelBufferPlaneProperties](cvpixelbufferplaneproperties.md)
  Properties of a plane of pixels in pixel buffer
- [struct CVProResRawMetadata](cvproresrawmetadata.md)
  Metadata associated with ProRes RAW images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvreadonlypixelbuffer)*