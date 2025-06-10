# CMTaggedDynamicBuffer

**Framework**: Core Media  
**Kind**: struct

Contains a collection of tags associated with a read-only media buffer.

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
struct CMTaggedDynamicBuffer
```

## Topics

### Initializers
- [init(tags: [CMTag], content: CVReadOnlyPixelBuffer)](cmtaggeddynamicbuffer/init(tags:content:)-1hscu.md)
- [init(tags: [CMTag], content: CMTaggedDynamicBuffer.Content)](cmtaggeddynamicbuffer/init(tags:content:)-1ttie.md)
- [init(tags: [CMTag], content: CMReadySampleBuffer<CVReadOnlyPixelBuffer>)](cmtaggeddynamicbuffer/init(tags:content:)-5jtjt.md)
- [init(tags: [CMTag], content: CMReadySampleBuffer<CMReadOnlyDataBlockBuffer>)](cmtaggeddynamicbuffer/init(tags:content:)-5xcim.md)
- [init(unsafeBuffer: sending CMTaggedBuffer)](cmtaggeddynamicbuffer/init(unsafebuffer:).md)
### Instance Properties
- [var content: CMTaggedDynamicBuffer.Content](cmtaggeddynamicbuffer/content-swift.property.md)
  Buffer containing media.
- [var tags: [CMTag]](cmtaggeddynamicbuffer/tags.md)
  Tags associated with the content.
### Instance Methods
- [func withUnsafeTaggedBuffer<R>((CMTaggedBuffer) throws -> sending R) rethrows -> sending R](cmtaggeddynamicbuffer/withunsafetaggedbuffer(_:).md)
### Enumerations
- [CMTaggedDynamicBuffer.Content](cmtaggeddynamicbuffer/content-swift.enum.md)
  A read-only buffer associated with the tags.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggeddynamicbuffer)*