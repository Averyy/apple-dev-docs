# MTLStorageMode.private

**Framework**: Metal  
**Kind**: case

The resource is only available to the GPU.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case `private`
```

## Mentions

- [Choosing a resource storage mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
- [Choosing a resource storage mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
- [Adjusting for GPU memory bandwidth tradeoffs](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)
- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)
- [Copying data to a private resource](copying-data-to-a-private-resource.md)
- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
- [Creating sparse heaps and sparse textures](creating-sparse-heaps-and-sparse-textures.md)
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)
- [Optimizing texture data](optimizing-texture-data.md)
- [Setting resource storage modes](setting-resource-storage-modes.md)
- [Transferring data between connected GPUs](transferring-data-between-connected-gpus.md)

#### Discussion

Metal may apply additional optimizations to private resources that aren’t allowed on shared or managed resources.

For more guidance on how to choose storage modes, see [`Setting resource storage modes`](setting-resource-storage-modes.md).

## See Also

- [MTLStorageMode.shared](mtlstoragemode/shared.md)
  The CPU and GPU share access to the resource, allocated in system memory.
- [MTLStorageMode.managed](mtlstoragemode/managed.md)
  The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized.
- [MTLStorageMode.memoryless](mtlstoragemode/memoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoragemode/private)*