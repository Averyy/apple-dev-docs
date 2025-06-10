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

- [Choosing a Resource Storage Mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
- [Setting Resource Storage Modes](setting-resource-storage-modes.md)
- [Creating Sparse Heaps and Sparse Textures](creating-sparse-heaps-and-sparse-textures.md)
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)
- [Adjusting for GPU Memory Bandwidth Tradeoffs](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)
- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)
- [Transferring Data Between Connected GPUs](transferring-data-between-connected-gpus.md)
- [Creating a Counter Sample Buffer to Store a GPU’s Counter Data During a Pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)
- [Optimizing Texture Data](optimizing-texture-data.md)
- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Discussion

Metal may apply additional optimizations to private resources that aren’t allowed on shared or managed resources.

For more guidance on how to choose storage modes, see [`Setting Resource Storage Modes`](setting-resource-storage-modes.md).

## See Also

- [MTLStorageMode.shared](mtlstoragemode/shared.md)
  The CPU and GPU share access to the resource, allocated in system memory.
- [MTLStorageMode.managed](mtlstoragemode/managed.md)
  The CPU and GPU may maintain separate copies of the resource, and any changes must be explicitly synchronized.
- [MTLStorageMode.memoryless](mtlstoragemode/memoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoragemode/private)*