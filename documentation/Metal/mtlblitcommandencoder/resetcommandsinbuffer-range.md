# resetCommandsInBuffer(_:range:)

**Framework**: Metal  
**Kind**: method

Encodes a command that resets a range of commands in an indirect command buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+

## Declaration

```swift
func resetCommandsInBuffer(_ buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer`: An indirect command buffer the command resets.
- `range`: A range of commands within  .

## See Also

- [func copyIndirectCommandBuffer(any MTLIndirectCommandBuffer, sourceRange: Range<Int>, destination: any MTLIndirectCommandBuffer, destinationIndex: Int)](mtlblitcommandencoder/copyindirectcommandbuffer(_:sourcerange:destination:destinationindex:).md)
  Encodes a command that copies commands from one indirect command buffer into another.
- [func optimizeIndirectCommandBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlblitcommandencoder/optimizeindirectcommandbuffer(_:range:).md)
  Encodes a command that can improve the performance of a range of commands within an indirect command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/resetcommandsinbuffer(_:range:))*