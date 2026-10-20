# beginCommandBuffer(allocator:options:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Prepares a command buffer for encoding with additional options.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func beginCommandBuffer(allocator: any MTL4CommandAllocator, options: MTL4CommandBufferOptions)
```

```objc
- (void) beginCommandBufferWithAllocator:(id<MTL4CommandAllocator>) allocator options:(MTL4CommandBufferOptions *) options;
```

#### Discussion

Attaches the command buffer to the specified [`MTL4CommandAllocator`](../mtl4commandallocator.md) and declares that the application is ready to encode commands into the command buffer.

Command allocators only service a single command buffer at a time. If you need to issue multiple calls to this method simultaneously, for example, in a multi-threaded command encoding scenario, create multiple instances of [`MTL4CommandAllocator`](../mtl4commandallocator.md) and use one for each call.

You can safely reuse command allocators after ending the command buffer using it by calling [`endCommandBuffer()`](./endcommandbuffer%28%29.md).

After calling this method, any prior calls to [`useResidencySet(_:)`](./useresidencyset%28_%29.md) and [`useResidencySets:count:`](./useresidencysets_count_.md) on this command buffer instance no longer apply. Make sure to call these methods again to signal your residency requirements to Metal.

The options you provide configure the command buffer only until the command buffer ends, in the next call to [`endCommandBuffer()`](./endcommandbuffer%28%29.md).

## Parameters

- `allocator`: [`MTL4CommandAllocator`](../mtl4commandallocator.md) to attach to.
- `options`: [`MTL4CommandBufferOptions`](../mtl4commandbufferoptions.md) to configure the command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/begincommandbuffer(allocator:options:))*