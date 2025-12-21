# beginCommandBuffer(allocator:)

**Framework**: Metal  
**Kind**: method  
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

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Discussion

Attaches the command buffer to the specified [`MTL4CommandAllocator`](mtl4commandallocator.md) and declares that the application is ready to encode commands into the command buffer.

Command allocators only service a single command buffer at a time. If you need to issue multiple calls to this method simultaneously, for example, in a multi-threaded command encoding scenario, create multiple instances of `MTLCommandAllocator` and use one for each call.

You can safely reuse command allocators after ending the command buffer using it by calling [`endCommandBuffer()`](mtl4commandbuffer/endcommandbuffer().md).

After calling this method, any prior calls to [`useResidencySet(_:)`](mtl4commandbuffer/useresidencyset(_:).md) and [`useResidencySets:count:`](mtl4commandbuffer/useresidencysets:count:.md) on this command buffer instance no longer apply. Make sure to call these methods again to signal your residency requirements to Metal.

## Parameters

- `allocator`:   to attach to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/begincommandbuffer(allocator:))*