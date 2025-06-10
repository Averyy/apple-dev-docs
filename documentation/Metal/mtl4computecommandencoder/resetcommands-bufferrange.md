# resetCommands(buffer:range:)

**Framework**: Metal  
**Kind**: method

Encodes a command that resets a range of commands in an indirect command buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func resetCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer`: An   the command resets.
- `range`: A range of commands within  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/resetcommands(buffer:range:))*