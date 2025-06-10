# CVBuffer

**Framework**: Core Video  
**Kind**: class

A reference to a Core Video buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class CVBuffer
```

#### Overview

This is an abstract type from which all Core Video buffers derive.

## Topics

### Structures
- [CVBuffer.Attributes](cvbuffer/attributes.md)
  A partial set of pixel buffer creation attributes. This struct is useful for conveying partial requirements for pixel buffers to clients. This struct makes all properties of `CVPixelBuffer/CreationAttributes` optional.
- [CVBuffer.CreationAttributes](cvbuffer/creationattributes.md)
  Attributes needed for creating a pixel buffer.
### Type Aliases
- [typealias OriginPosition](cvbuffer/originposition.md)
- [typealias Padding](cvbuffer/padding.md)
- [typealias PlaneProperties](cvbuffer/planeproperties.md)
- [typealias Size](cvbuffer/size.md)

## Relationships

### Conforms To
- [CMAttachmentBearerProtocol](../CoreMedia/CMAttachmentBearerProtocol.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [enum CVAttachmentMode](cvattachmentmode.md)
  The propagation modes of a Core Video buffer attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer)*