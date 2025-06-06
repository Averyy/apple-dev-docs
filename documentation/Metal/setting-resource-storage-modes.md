# Setting Resource Storage Modes

**Framework**: Metal

Set a storage mode that defines the memory location and access permissions of a resource.

#### Overview

Storage modes are only set when creating an instance, and the system default allows for access to memory from both the CPU and GPU. Metal selects the default mode for resources depending on hardware.

- For Apple silicon GPUs the default is [`MTLStorageMode.shared`](mtlstoragemode/shared.md).
- For Intel-based Mac computers, the default is [`MTLStorageMode.managed`](mtlstoragemode/managed.md) for all [`MTLTexture`](mtltexture.md) instances and [`MTLBuffer`](mtlbuffer.md) instances attached to discrete GPUs. [`MTLBuffer`](mtlbuffer.md) instances using the integrated GPU have [`MTLStorageMode.shared`](mtlstoragemode/shared.md) as their default.

> ❗ **Important**:  Use the system default if your data is available to both the CPU and GPU. When you manually select shared or managed mode, your app may not run on some hardware.

 Use the system default if your data is available to both the CPU and GPU. When you manually select shared or managed mode, your app may not run on some hardware.

You perform the same synchronization tasks to ensure GPU and CPU memory coherency in both default modes. To check for GPU architecture and capabilities, use the [`supportsFamily(_:)`](mtldevice/supportsfamily(_:).md) method instead of the [`storageMode`](mtlresource/storagemode.md) property. See [`Detecting GPU Features and Metal Software Versions`](detecting-gpu-features-and-metal-software-versions.md) for more information.

Use [`MTLStorageMode.memoryless`](mtlstoragemode/memoryless.md), only available on Apple silicon, when you manage your own storage, or want to run a GPU task that requires temporary resources. For tasks that share memory on the GPU, use [`MTLStorageMode.private`](mtlstoragemode/private.md) storage. This article includes examples of how to set the storage mode for a buffer or texture.

For more guidance on which mode to choose, see [`Choosing a Resource Storage Mode for Apple GPUs`](choosing-a-resource-storage-mode-for-apple-gpus.md) and [`Choosing a Resource Storage Mode for Intel and AMD GPUs`](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md).

##### Set a Storage Mode for a Buffer

Create a new [`MTLBuffer`](mtlbuffer.md) with the [`makeBuffer(length:options:)`](mtldevice/makebuffer(length:options:).md) method and set its storage mode in the method’s `options` parameter.

> **Note**:  The storage mode options in [`MTLResourceOptions`](mtlresourceoptions.md) are equivalent to the storage mode values in [`MTLStorageMode`](mtlstoragemode.md). When you create a new buffer, you can combine multiple resource options but you can set only one storage mode.

 The storage mode options in [`MTLResourceOptions`](mtlresourceoptions.md) are equivalent to the storage mode values in [`MTLStorageMode`](mtlstoragemode.md). When you create a new buffer, you can combine multiple resource options but you can set only one storage mode.

##### Set a Storage Mode for a Texture

Create a new [`MTLTextureDescriptor`](mtltexturedescriptor.md) and set its storage mode in the descriptor’s [`storageMode`](mtlresource/storagemode.md) property. Then create a new [`MTLTexture`](mtltexture.md) with the [`makeTexture(descriptor:)`](mtldevice/maketexture(descriptor:).md) method.

## See Also

- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
  Select an appropriate storage mode for your textures and buffers on Apple GPUs.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/setting-resource-storage-modes)*