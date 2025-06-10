# CVReadOnlyPixelBuffer

**Framework**: Core Video  
**Kind**: class

CVReadOnlyPixelBuffer provides an immutable view of the pixel data held by the pixel buffer.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvreadonlypixelbuffer)*