# MTLStorageMode.shared

**Framework**: Metal  
**Kind**: case

The CPU and GPU share access to the resource, allocated in system memory.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case shared
```

## Mentions

- [Choosing a resource storage mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
- [Optimizing texture data](optimizing-texture-data.md)
- [Setting resource storage modes](setting-resource-storage-modes.md)
- [Adjusting for GPU memory bandwidth tradeoffs](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)
- [Choosing a resource storage mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)
- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Synchronizing a managed resource in macOS](synchronizing-a-managed-resource-in-macos.md)

#### Discussion

This is the default storage mode for [`MTLBuffer`](mtlbuffer.md) instances on integrated GPUs and both [`MTLBuffer`](mtlbuffer.md) and [`MTLTexture`](mtltexture.md) instances on Apple silicon GPUs. On non-Apple family GPUs, the shared storage mode isn’t available for [`MTLTexture`](mtltexture.md) instances.

When either the CPU or GPU changes the contents of the resource, you’re responsible for synchronizing access to the texture from the other participant. Ensure that all changes you schedule on either the CPU or GPU for a resource that uses shared memory complete before accessing that resource on the other processor.

For more guidance on how to choose storage modes, see [`Setting resource storage modes`](setting-resource-storage-modes.md).

## See Also

- [MTLStorageMode.managed](mtlstoragemode/managed.md)
  The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized.
- [MTLStorageMode.private](mtlstoragemode/private.md)
  The resource is only available to the GPU.
- [MTLStorageMode.memoryless](mtlstoragemode/memoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoragemode/shared)*