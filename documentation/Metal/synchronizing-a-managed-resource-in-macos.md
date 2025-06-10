# Synchronizing a Managed Resource in macOS

**Framework**: Metal

Manually synchronize memory for a Metal resource in apps.

#### Overview

For Mac computers with Intel or external GPUs, Metal offers  Managed resources are [`MTLResource`](mtlresource.md) instances, such as an [`MTLTexture`](mtltexture.md) or [`MTLBuffer`](mtlbuffer.md), which use memory that your app can copy between the CPU and GPU. Managed resources use a [`storageMode`](mtlresource/storagemode.md) of [`MTLStorageMode.managed`](mtlstoragemode/managed.md).

You need to manually synchronize managed resources, copying changed memory between the CPU and GPU. This is different from Apple family GPUs, which use [`MTLStorageMode.shared`](mtlstoragemode/shared.md) for resources that the CPU and GPU can both access. Synchronize after your code finishes memory writes. After data synchronizes, you can safely read it in both your app and GPU functions.

As a best practice, try to keep your data synchronization points to a minimum. Even synchronization calls which don’t copy data can result in a small performance hit.

> **Note**:  Managed resources are the default memory storage type for Intel and external GPU devices in Metal. For more information about macOS resource storage modes and how to select them, see [`Choosing a Resource Storage Mode for Intel and AMD GPUs`](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md).

##### Synchronize a Managed Buffer

First, create an [`MTLBuffer`](mtlbuffer.md) with the option [`MTLStorageMode.managed`](mtlstoragemode/managed.md), which tells Metal to reserve managed memory space for the resource:

Next, modify the buffer’s data on the CPU:

After completing a CPU modification, call the [`didModifyRange:`](mtlbuffer/didmodifyrange:.md) method. This method updates a specific range of data and keeps the buffer synchronized. Before calling this method, the modified buffer’s data on the GPU is in an undefined state.

After encoding a GPU modification, encode a [`synchronize(resource:)`](mtlblitcommandencoder/synchronize(resource:).md) command. This command updates the entire buffer and keeps it synchronized. Before executing this command, the modified buffer’s data on the CPU is in an undefined state.

##### Synchronize a Managed Texture

First, create an [`MTLTexture`](mtltexture.md) in managed memory from an [`MTLTextureDescriptor`](mtltexturedescriptor.md) with its storage mode set to [`MTLStorageMode.managed`](mtlstoragemode/managed.md):

To perform a CPU modification and simultaneously notify Metal about the change, call the [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:).md) method. This method updates a specific region of data and keeps the texture synchronized. To update a specific texture slice, call the [`replace(region:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:)`](mtltexture/replace(region:mipmaplevel:slice:withbytes:bytesperrow:bytesperimage:).md) method instead. Before calling one of these methods, the modified texture’s data on the GPU is in an undefined state.

After encoding a GPU modification, encode a [`synchronize(resource:)`](mtlblitcommandencoder/synchronize(resource:).md) command. This command updates the entire texture and keeps it synchronized. To update a specific texture slice or mipmap level, encode the [`synchronize(texture:slice:level:)`](mtlblitcommandencoder/synchronize(texture:slice:level:).md) command instead. Before executing this command, the modified texture’s data on the CPU is in an undefined state.

## See Also

- [Setting Resource Storage Modes](setting-resource-storage-modes.md)
  Set a storage mode that defines the memory location and access permissions of a resource.
- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
  Select an appropriate storage mode for your textures and buffers on Apple GPUs.
- [Choosing a Resource Storage Mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
  Select an appropriate storage mode for your textures and buffers on AMD and Intel GPUs.
- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)
  Use a blit command encoder to copy buffer or texture data to a private resource.
- [Transferring Data Between Connected GPUs](transferring-data-between-connected-gpus.md)
  Use high-speed connections between GPUs to transfer data quickly.
- [Reducing the Memory Footprint of Metal Apps](reducing-the-memory-footprint-of-metal-apps.md)
  Learn best practices for using memory efficiently in iOS and tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/synchronizing-a-managed-resource-in-macos)*