# MTLTensorBufferAttachments

**Framework**: Metal  
**Kind**: class

An object that associates each plane of a tensor with a buffer and byte offset for buffer-backed tensor creation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class MTLTensorBufferAttachments
```

## Topics

### Instance Methods
- [func buffer(for: MTLTensorPlaneType) -> (any MTLBuffer)?](mtltensorbufferattachments/buffer(for:).md)
  Returns the buffer backing the given plane, or `nil` if none has been set.
- [func offset(for: MTLTensorPlaneType) -> Int](mtltensorbufferattachments/offset(for:).md)
  Returns the byte offset into the buffer for the given plane.
- [func reset()](mtltensorbufferattachments/reset.md)
  Empties the container of all its elements.
- [func setBuffer(any MTLBuffer, offset: Int, for: MTLTensorPlaneType)](mtltensorbufferattachments/setbuffer(_:offset:for:).md)
  Sets the buffer and byte offset to use as backing storage for the given plane.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorbufferattachments)*