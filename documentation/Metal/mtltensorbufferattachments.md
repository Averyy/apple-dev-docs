# MTLTensorBufferAttachments

**Framework**: Metal  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTLTensorBufferAttachments : NSObject
```

## Topics

### Instance Methods
- [func buffer(for: MTLTensorPlaneType) -> (any MTLBuffer)?](./mtltensorbufferattachments/buffer%28for%29.md)
  Returns the buffer backing the given plane, or `nil` if none has been set.
- [func offset(for: MTLTensorPlaneType) -> Int](./mtltensorbufferattachments/offset%28for%29.md)
  Returns the byte offset into the buffer for the given plane.
- [func reset()](./mtltensorbufferattachments/reset%28%29.md)
  Empties the container of all its elements.
- [func setBuffer(any MTLBuffer, offset: Int, for: MTLTensorPlaneType)](./mtltensorbufferattachments/setbuffer%28_,offset,for%29.md)
  Sets the buffer and byte offset to use as backing storage for the given plane.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorbufferattachments)*