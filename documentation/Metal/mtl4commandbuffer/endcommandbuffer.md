# endCommandBuffer()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Closes a command buffer to prepare it for submission to a command queue.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func endCommandBuffer()
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Discussion

Explicitly ending the command buffer allows you to reuse the [`MTL4CommandAllocator`](mtl4commandallocator.md) to start servicing other command buffers. It is an error to call `commit` on a command buffer previously recording before calling this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/endcommandbuffer())*