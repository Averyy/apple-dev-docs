# resetCommands(buffer:range:)

**Framework**: Metal  
**Kind**: method

Encodes a command that resets a range of commands in an indirect command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func resetCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer`: An   the command resets.
- `range`: A range of commands within  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/resetcommands(buffer:range:))*