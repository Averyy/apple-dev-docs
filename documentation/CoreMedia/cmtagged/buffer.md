# CMTagged.Buffer

**Framework**: Core Media  
**Kind**: struct

Carries a media buffer content and an array of tags.

**Availability**:
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)
- Unknown ?+ - Deprecated
- iOS 26.0+ (Beta)

## Declaration

```swift
struct Buffer<Content> where Content : CMTagged.BufferContent
```

## Topics

### Initializers
- [init(tags: [CMTag], content: Content)](cmtagged/buffer/init(tags:content:).md)
- [init(unsafeBuffer: sending CMTaggedBuffer)](cmtagged/buffer/init(unsafebuffer:).md)
  Create immutable tagged buffer from existing tagged buffer.
### Instance Properties
- [var content: Content](cmtagged/buffer/content.md)
  Buffer containing media.
- [var taggedBuffer: CMTaggedBuffer](cmtagged/buffer/taggedbuffer.md)
- [var tags: [CMTag]](cmtagged/buffer/tags.md)
  Tags associated with the buffer.
### Instance Methods
- [func withUnsafeTaggedBuffer<R>((CMTaggedBuffer) throws -> sending R) rethrows -> sending R](cmtagged/buffer/withunsafetaggedbuffer(_:).md)
  Access the underlying CMTaggedBuffer instance.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagged/buffer)*