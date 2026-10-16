# copyCommands(sourceBuffer:sourceRange:destinationBuffer:destinationIndex:)

**Framework**: Metal  
**Kind**: method

Encodes a command that copies commands from one indirect command buffer into another.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copyCommands(sourceBuffer: any MTLIndirectCommandBuffer, sourceRange: Range<Int>, destinationBuffer: any MTLIndirectCommandBuffer, destinationIndex: Int)
```

## Parameters

- `sourceBuffer`: An [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) instance the command copies from.
- `sourceRange`: The range of commands in `sourceBuffer` to copy. The source range needs to start at a valid execution point.
- `destinationBuffer`: Another [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) instance the command copies to.
- `destinationIndex`: An index in `destinationBuffer` where the command copies content to. The destination index needs to be a valid execution point with enough remaining space in `destinationBuffer` to accommodate `sourceRange.count` commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copycommands(sourcebuffer:sourcerange:destinationbuffer:destinationindex:))*