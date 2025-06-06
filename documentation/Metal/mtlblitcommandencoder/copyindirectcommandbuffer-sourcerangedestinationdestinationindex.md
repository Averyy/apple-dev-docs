# copyIndirectCommandBuffer(_:sourceRange:destination:destinationIndex:)

**Framework**: Metal  
**Kind**: method

Encodes a command that copies commands from one indirect command buffer into another.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+

## Declaration

```swift
func copyIndirectCommandBuffer(_ buffer: any MTLIndirectCommandBuffer, sourceRange: Range<Int>, destination: any MTLIndirectCommandBuffer, destinationIndex: Int)
```

#### Discussion

You can copy commands from one indirect command buffer to another, but only a compatible one. You can create compatible indirect command buffers by passing [`MTLIndirectCommandBufferDescriptor`](mtlindirectcommandbufferdescriptor.md) instances with the same configuration to the [`makeIndirectCommandBuffer(descriptor:maxCommandCount:options:)`](mtldevice/makeindirectcommandbuffer(descriptor:maxcommandcount:options:).md) method of [`MTLDevice`](mtldevice.md).

## Parameters

- `buffer`: An indirect command buffer the command copies from.
- `sourceRange`: The range of commands in the source buffer to copy.   The source range needs to start on a valid execution point.
- `destination`: Another indirect command buffer the command copies to.
- `destinationIndex`: An index in   where the command copies content from   to. The destination index needs to be a valid execution point with enough remaining space in   to accommodate   indexes.

## See Also

- [func resetCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlblitcommandencoder/resetcommandsinbuffer(_:range:).md)
  Encodes a command that resets a range of commands in an indirect command buffer.
- [func optimizeIndirectCommandBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlblitcommandencoder/optimizeindirectcommandbuffer(_:range:).md)
  Encodes a command that can improve the performance of a range of commands within an indirect command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copyindirectcommandbuffer(_:sourcerange:destination:destinationindex:))*