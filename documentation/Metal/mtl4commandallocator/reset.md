# reset()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Marks the command allocator’s heaps for reuse.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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