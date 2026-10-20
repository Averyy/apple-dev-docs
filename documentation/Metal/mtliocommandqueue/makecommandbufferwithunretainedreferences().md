# makeCommandBufferWithUnretainedReferences()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (id<MTLIOCommandBuffer>) commandBufferWithUnretainedReferences;
```

## See Also

### Creating a input/output command buffer
- [func makeCommandBuffer() -> any MTLIOCommandBuffer](./makecommandbuffer%28%29.md)
  Creates an input/output command buffer for the command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandqueue/makecommandbufferwithunretainedreferences())*