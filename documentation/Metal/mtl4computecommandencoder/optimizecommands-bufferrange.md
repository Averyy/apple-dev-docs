# optimizeCommands(buffer:range:)

**Framework**: Metal  
**Kind**: method

Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func optimizeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer`: An   instance that this command optimizes.
- `range`: A range of commands within  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizecommands(buffer:range:))*