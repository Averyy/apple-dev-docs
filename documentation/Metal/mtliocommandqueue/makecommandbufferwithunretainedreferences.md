# makeCommandBufferWithUnretainedReferences()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates an input/output command buffer for the command queue that doesn’t retain the instances you pass to its methods.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeCommandBufferWithUnretainedReferences() -> any MTLIOCommandBuffer
```

## See Also

- [func makeCommandBuffer() -> any MTLIOCommandBuffer](mtliocommandqueue/makecommandbuffer.md)
  Creates an input/output command buffer for the command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandqueue/makecommandbufferwithunretainedreferences())*