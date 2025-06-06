# setIndirectCommandBuffer(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a reference to an indirect command buffer into the argument buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func setIndirectCommandBuffer(_ indirectCommandBuffer: (any MTLIndirectCommandBuffer)?, index: Int)
```

## Parameters

- `indirectCommandBuffer`: An indirect command-buffer the method encodes.
- `index`: The index of an inline, constant-data argument within the argument buffer.   The value corresponds to either the index ID of a declaration in   Metal Shading Language (MSL) or the   property of   an   instance.

## See Also

- [func setIndirectCommandBuffers([(any MTLIndirectCommandBuffer)?], range: Range<Int>)](mtlargumentencoder/setindirectcommandbuffers(_:range:).md)
  Encodes an array of indirect command buffers into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setindirectcommandbuffer(_:index:))*