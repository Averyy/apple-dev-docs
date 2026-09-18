# endCommandBuffer()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Finalizes a command buffer which makes it ready for you to submit it to a command queue.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func endCommandBuffer()
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Discussion

Metal generates an error if you submit a command buffer to a queue, such as with its [`commit:count:`](mtl4commandqueue/commit:count:.md) method, before calling this method.

> **Note**: Ending a command buffer also marks its [`MTL4CommandAllocator`](mtl4commandallocator.md) as available for you to assign it to work with another command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/endcommandbuffer())*