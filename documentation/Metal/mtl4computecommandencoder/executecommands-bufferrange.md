# executeCommands(buffer:range:)

**Framework**: Metal  
**Kind**: method

Encodes a command to execute commands from an indirect command buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func executeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer`: An   instance that contains other commands the current command runs.
- `range`: A span of integers that represent the command entries in buffer the current command runs.   The number of commands needs to be less than or equal to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/executecommands(buffer:range:))*