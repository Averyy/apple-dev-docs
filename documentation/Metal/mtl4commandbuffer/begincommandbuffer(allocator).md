# beginCommandBuffer(allocator:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Prepares a command buffer for encoding.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func beginCommandBuffer(allocator: any MTL4CommandAllocator)
```

```objc
- (void) beginCommandBufferWithAllocator:(id<MTL4CommandAllocator>) allocator;
```

## Mentions

- [Understanding the Metal 4 core API](../understanding-the-metal-4-core-api.md)

## Discussion

Attaches the command buffer to the specified [`MTL4CommandAllocator`](../mtl4commandallocator.md) and declares that the application is ready to encode commands into the command buffer.

Command allocators only service a single command buffer at a time. If you need to issue multiple calls to this method simultaneously, for example, in a multi-threaded command encoding scenario, create multiple instances of [`MTL4CommandAllocator`](../mtl4commandallocator.md) and use one for each call.

You can safely reuse command allocators after ending the command buffer using it by calling [`endCommandBuffer()`](./endcommandbuffer%28%29.md).

After calling this method, any prior calls to [`useResidencySet(_:)`](./useresidencyset%28_%29.md) and [`useResidencySets:count:`](./useresidencysets_count_.md) on this command buffer instance no longer apply. Make sure to call these methods again to signal your residency requirements to Metal.

## Parameters

- `allocator`: [`MTL4CommandAllocator`](../mtl4commandallocator.md) to attach to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/begincommandbuffer(allocator:))*