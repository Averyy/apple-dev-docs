# setIndirectCommandBuffers(_:range:)

**Framework**: Metal  
**Kind**: method

Encodes an array of indirect command buffers into the argument buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+

## Declaration

```swift
func setIndirectCommandBuffers(_ buffers: [(any MTLIndirectCommandBuffer)?], range: Range<Int>)
```

## Parameters

- `buffers`: An array of indirect command buffers the method encodes.
- `range`: A range of indices within the argument buffer for each element in  .   The values correspond to either the index IDs of declarations in   Metal Shading Language (MSL) or the   property   of   instances.

## See Also

- [func setIndirectCommandBuffer((any MTLIndirectCommandBuffer)?, index: Int)](mtlargumentencoder/setindirectcommandbuffer(_:index:).md)
  Encodes a reference to an indirect command buffer into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setindirectcommandbuffers(_:range:))*