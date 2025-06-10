# Choosing a Resource Storage Mode for Apple GPUs

**Framework**: Metal

Select an appropriate storage mode for your textures and buffers on Apple GPUs.

#### Overview

Apple GPUs have a unified memory model in which the CPU and the GPU share system memory. However, CPU and GPU access to that memory depends on the storage mode you choose for your resources. The [`MTLStorageMode.shared`](mtlstoragemode/shared.md) mode defines system memory that both the CPU and the GPU can access. The [`MTLStorageMode.private`](mtlstoragemode/private.md) mode defines system memory that only the GPU can access.

The [`MTLStorageMode.memoryless`](mtlstoragemode/memoryless.md) mode defines tile memory within the GPU that only the GPU can access. Tile memory has higher bandwidth, lower latency, and consumes less power than system memory.

![A diagram that shows the three types of Apple GPU resource storage modes: shared at the top, private in the middle, and memoryless at the bottom. The shared mode resource is in between a GPU and CPU with bidirectional arrows pointing to and from each. The private mode resource is next to a GPU with a bidirectional arrow between them. The memoryless mode resource appears inside a GPU’s tiled memory region.](https://docs-assets.developer.apple.com/published/95106a9e6960adc249245b78fad36f76/media-3975653%402x.png)

##### Choose a Resource Storage Mode for Buffers or Textures

The storage mode you choose depends on how you plan to use Metal resources:

For information on setting storage modes in your app, see [`Setting Resource Storage Modes`](setting-resource-storage-modes.md).

##### Create a Memoryless Render Target

To create a memoryless render target, set the [`storageMode`](mtltexturedescriptor/storagemode.md) property of an [`MTLTextureDescriptor`](mtltexturedescriptor.md) to [`MTLStorageMode.memoryless`](mtlstoragemode/memoryless.md) and use this descriptor to create a new [`MTLTexture`](mtltexture.md). Then set this new texture as the [`texture`](mtlrenderpassattachmentdescriptor/texture.md) property of an [`MTLRenderPassAttachmentDescriptor`](mtlrenderpassattachmentdescriptor.md).

See [`Rendering a Scene with Deferred Lighting in Objective-C`](rendering-a-scene-with-deferred-lighting-in-objective-c.md) for an example of an app that uses a memoryless render target.

> **Note**:  You can create only textures, not buffers, using [`MTLStorageMode.memoryless`](mtlstoragemode/memoryless.md) mode. You can’t use buffers as memoryless render targets.

## See Also

- [Setting Resource Storage Modes](setting-resource-storage-modes.md)
  Set a storage mode that defines the memory location and access permissions of a resource.
- [Choosing a Resource Storage Mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
  Select an appropriate storage mode for your textures and buffers on AMD and Intel GPUs.
- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)
  Use a blit command encoder to copy buffer or texture data to a private resource.
- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)
  Manually synchronize memory for a Metal resource in apps.
- [Transferring Data Between Connected GPUs](transferring-data-between-connected-gpus.md)
  Use high-speed connections between GPUs to transfer data quickly.
- [Reducing the Memory Footprint of Metal Apps](reducing-the-memory-footprint-of-metal-apps.md)
  Learn best practices for using memory efficiently in iOS and tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/choosing-a-resource-storage-mode-for-apple-gpus)*