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

- [Optimizing Texture Data](optimizing-texture-data.md)
- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
- [Setting Resource Storage Modes](setting-resource-storage-modes.md)
- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)
- [Adjusting for GPU Memory Bandwidth Tradeoffs](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)
- [Choosing a Resource Storage Mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Discussion

This is the default storage mode for [`MTLBuffer`](mtlbuffer.md) instances on integrated GPUs and both [`MTLBuffer`](mtlbuffer.md) and [`MTLTexture`](mtltexture.md) instances on Apple silicon GPUs. On non-Apple family GPUs, the shared storage mode isn’t available for [`MTLTexture`](mtltexture.md) instances.

When either the CPU or GPU changes the contents of the resource, you’re responsible for synchronizing access to the texture from the other participant. Ensure that all changes you schedule on either the CPU or GPU for a resource that uses shared memory complete before accessing that resource on the other processor.

For more guidance on how to choose storage modes, see [`Setting Resource Storage Modes`](setting-resource-storage-modes.md).

## See Also

- [MTLStorageMode.managed](mtlstoragemode/managed.md)
  The CPU and GPU may maintain separate copies of the resource, and any changes must be explicitly synchronized.
- [MTLStorageMode.private](mtlstoragemode/private.md)
  The resource is only available to the GPU.
- [MTLStorageMode.memoryless](mtlstoragemode/memoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoragemode/shared)*