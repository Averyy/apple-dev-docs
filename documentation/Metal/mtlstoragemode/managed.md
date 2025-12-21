# MTLStorageMode.managed

**Framework**: Metal  
**Kind**: case

The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.11+

## Declaration

```swift
case managed
```

## Mentions

- [Synchronizing a managed resource in macOS](synchronizing-a-managed-resource-in-macos.md)
- [Optimizing texture data](optimizing-texture-data.md)
- [Adjusting for GPU memory bandwidth tradeoffs](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)
- [Choosing a resource storage mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Setting resource storage modes](setting-resource-storage-modes.md)

#### Discussion

On Intel-based Mac computers, this is the default storage mode for [`MTLTexture`](mtltexture.md) objects. In iOS and tvOS, the managed storage mode isn’t available. With managed storage, you synchronize changes between the CPU and GPU manually. For instructions and examples of resource synchronization, see [`Synchronizing a managed resource in macOS`](synchronizing-a-managed-resource-in-macos.md).

For more guidance on how to choose storage modes, see [`Setting resource storage modes`](setting-resource-storage-modes.md).

## See Also

- [MTLStorageMode.shared](mtlstoragemode/shared.md)
  The CPU and GPU share access to the resource, allocated in system memory.
- [MTLStorageMode.private](mtlstoragemode/private.md)
  The resource is only available to the GPU.
- [MTLStorageMode.memoryless](mtlstoragemode/memoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoragemode/managed)*