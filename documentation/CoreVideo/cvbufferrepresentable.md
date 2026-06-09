# CVBufferRepresentable

**Framework**: Core Video  
**Kind**: protocol

CVBufferRepresentable protocol is a sealed protocol intended to be implemented by the types in CoreVideo framework. This protocol facilitates Swift types that wrap a value of CVBuffer type.

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
protocol CVBufferRepresentable<Buffer> : ~Copyable
```

## Topics

### Associated Types
- [associatedtype Buffer : CVBuffer](cvbufferrepresentable/buffer.md)
### Instance Methods
- [func withUnsafeBuffer<R>((Self.Buffer) throws -> sending R) rethrows -> sending R](cvbufferrepresentable/withunsafebuffer(_:).md)
  Access the underlying `Buffer` object. This function should be used to bridge existing code that uses the Buffer type.

## Relationships

### Inherited By
- [CVImageBufferRepresentable](cvimagebufferrepresentable.md)
- [CVPixelBufferRepresentable](cvpixelbufferrepresentable.md)
### Conforming Types
- [CVMutablePixelBuffer](cvmutablepixelbuffer.md)
- [CVReadOnlyPixelBuffer](cvreadonlypixelbuffer.md)

## See Also

- [protocol CVAttachmentKeyDefinitions](cvattachmentkeydefinitions.md)
  Marks a type as a collection of attachment keys for an attachment bearer.
- [protocol CVAttachmentModePreference](cvattachmentmodepreference.md)
  Defines preferred mode for an attachment key.
- [protocol CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
  Allows Swift types to be used as buffer attachment value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbufferrepresentable)*