# CMSampleBuffer.ContentType

**Framework**: Core Media  
**Kind**: enum

Describes the type of content carried by a sample buffer instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
enum ContentType
```

## Topics

### Enumeration Cases
- [CMSampleBuffer.ContentType.dataBuffer](cmsamplebuffer/contenttype-swift.enum/databuffer.md)
  Sample buffer is carrying a block buffer containing bytes.
- [CMSampleBuffer.ContentType.markerOnly](cmsamplebuffer/contenttype-swift.enum/markeronly.md)
  Marker sample buffers have neither data nor format description. These buffers are used for signaling events via the attachments when sample buffer content is not available.
- [CMSampleBuffer.ContentType.pixelBuffer](cmsamplebuffer/contenttype-swift.enum/pixelbuffer.md)
  Sample buffer is carrying a CoreVideo pixel buffer.
- [CMSampleBuffer.ContentType.sampleReference](cmsamplebuffer/contenttype-swift.enum/samplereference.md)
  Sample buffer references sample data at a URL.
- [CMSampleBuffer.ContentType.taggedBuffers](cmsamplebuffer/contenttype-swift.enum/taggedbuffers.md)
  Sample buffer is carrying a group of tagged buffers.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/contenttype-swift.enum)*