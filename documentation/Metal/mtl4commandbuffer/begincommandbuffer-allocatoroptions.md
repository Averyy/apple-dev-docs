# beginCommandBuffer(allocator:options:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Prepares a command buffer for encoding with additional options.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func beginCommandBuffer(allocator: any MTL4CommandAllocator, options: MTL4CommandBufferOptions)
```

#### Discussion

Attaches the command buffer to the specified [`MTL4CommandAllocator`](mtl4commandallocator.md) and declares that the application is ready to encode commands into the command buffer.

Command allocators only service a single command buffer at a time. If you need to issue multiple calls to this method simultaneously, for example, in a multi-threaded command encoding scenario, create multiple instances of `MTLCommandAllocator` and use one for each call.

You can safely reuse command allocators after ending the command buffer using it by calling [`endCommandBuffer()`](mtl4commandbuffer/endcommandbuffer().md).

After calling this method, any prior calls to [`useResidencySet(_:)`](mtl4commandbuffer/useresidencyset(_:).md) and [`useResidencySets:count:`](mtl4commandbuffer/useresidencysets:count:.md) on this command buffer instance no longer apply. Make sure to call these methods again to signal your residency requirements to Metal.

The options you provide configure the command buffer only until the command buffer ends, in the next call to [`endCommandBuffer()`](mtl4commandbuffer/endcommandbuffer().md).

## Parameters

- `allocator`:   to attach to.
- `options`:   to configure the command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/begincommandbuffer(allocator:options:))*