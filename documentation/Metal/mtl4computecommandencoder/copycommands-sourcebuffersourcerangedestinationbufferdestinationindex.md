# copyCommands(sourceBuffer:sourceRange:destinationBuffer:destinationIndex:)

**Framework**: Metal  
**Kind**: method

Encodes a command that copies commands from one indirect command buffer into another.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copyCommands(sourceBuffer: any MTLIndirectCommandBuffer, sourceRange: Range<Int>, destinationBuffer: any MTLIndirectCommandBuffer, destinationIndex: Int)
```

## Parameters

- `sourceRange`: The range of commands in   to copy.   The copy operation requires that the source range starts at a valid execution point.
- `destinationIndex`: An index in   into where the command copies content to. The copy operation requires   that the destination index is a valid execution point with enough space left in    to accommodate   commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copycommands(sourcebuffer:sourcerange:destinationbuffer:destinationindex:))*