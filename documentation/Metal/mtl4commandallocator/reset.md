# reset()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Marks the command allocator’s heaps for reuse.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func reset()
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Discussion

Calling this method allows new [`MTL4CommandBuffer`](mtl4commandbuffer.md) to reuse its existing internal memory heaps to encode new GPU commands.

You are responsible to ensure that all command buffers with memory originating from this allocator instance are complete before calling resetting it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandallocator/reset())*