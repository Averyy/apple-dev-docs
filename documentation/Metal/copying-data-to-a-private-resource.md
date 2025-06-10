# Copying Data to a Private Resource

**Framework**: Metal

Use a blit command encoder to copy buffer or texture data to a private resource.

#### Overview

Resources with an [`MTLStorageMode.private`](mtlstoragemode/private.md) storage mode are accessible only to the GPU. Private resources perform better than shared resources, and you don’t have to explicitly synchronize them the way you do for managed resources.

However, because private resources aren’t accessible to the CPU, you can’t populate them with it. To write data from the CPU to a private resource, you must first write the data to a shared or managed resource. You can then copy the data from that resource to the private resource.

For more information about resource storage modes, see [`Setting Resource Storage Modes`](setting-resource-storage-modes.md).

##### Copying Data From a Shared Buffer to a Private Buffer

First, create a shared buffer and populate its contents using the [`makeBuffer(bytes:length:options:)`](mtldevice/makebuffer(bytes:length:options:).md) method.

Next, create a private buffer that’s large enough to store your buffer data using the [`makeBuffer(length:options:)`](mtldevice/makebuffer(length:options:).md) method.

Finally, encode and commit a [`copy(from:sourceOffset:to:destinationOffset:size:)`](mtlblitcommandencoder/copy(from:sourceoffset:to:destinationoffset:size:).md) command. Set the shared buffer as the `sourceBuffer` parameter. Set the private buffer as the `destinationBuffer` parameter.

> **Note**:  In macOS, Metal doesn’t reformat buffer contents or layout to improve GPU access. There’s no difference in GPU performance between managed or private buffers, so there’s no performance benefit in copying data from a managed buffer to a private buffer.

##### Copying Data From a Shared Buffer to a Private Texture

Use this implementation to copy texture data from the CPU to a private texture in one operation, without having to synchronize a managed texture.

First, create a shared buffer and populate its contents with your texture data.

Next, create a private texture with a suitable configuration for the texture data.

Finally, encode and commit a [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)`](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md) command. Set the shared buffer as the `sourceBuffer` parameter. Set the private texture as the `destinationTexture` parameter.

##### Copying Data From a Shared or Managed Texture to a Private Texture

First, create a shared texture or for Mac apps, a managed texture. For more information about creating buffers and textures with specific storage modes, see [`Setting Resource Storage Modes`](setting-resource-storage-modes.md).

Then populate the contents of the source texture using the [`replace(region:mipmapLevel:withBytes:bytesPerRow:)`](mtltexture/replace(region:mipmaplevel:withbytes:bytesperrow:).md) method.

Next, create a private texture with a suitable configuration for your texture data. If appropriate, reuse the texture descriptor that you configured for the shared or managed texture.

Finally, encode and commit a [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationslice:destinationlevel:destinationorigin:).md) command. Set the shared or managed texture as the `sourceTexture` parameter. Set the private texture as the `destinationTexture` parameter.

Copying data from a managed texture to a private texture involves two copy operations. For the first operation, Metal synchronizes the managed texture and copies the texture data from CPU-accessible memory to GPU-accessible memory. For the second operation, Metal copies the texture data from the managed texture to the private texture.

##### Copying Data From a Private Texture to a Shared Buffer

Use this implementation to copy texture data from the GPU to a shared buffer, without having to synchronize a managed texture.

First, create a private texture.

Next, create a shared buffer that’s large enough to store your texture data.

Next, encode a compute, render, or blit pass to populate the contents of your private texture.

Finally, encode and commit a [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:).md) command. Set the private texture as the `sourceTexture` parameter. Set the shared buffer as the `destinationBuffer` parameter.

## See Also

- [Setting Resource Storage Modes](setting-resource-storage-modes.md)
  Set a storage mode that defines the memory location and access permissions of a resource.
- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
  Select an appropriate storage mode for your textures and buffers on Apple GPUs.
- [Choosing a Resource Storage Mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
  Select an appropriate storage mode for your textures and buffers on AMD and Intel GPUs.
- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)
  Manually synchronize memory for a Metal resource in apps.
- [Transferring Data Between Connected GPUs](transferring-data-between-connected-gpus.md)
  Use high-speed connections between GPUs to transfer data quickly.
- [Reducing the Memory Footprint of Metal Apps](reducing-the-memory-footprint-of-metal-apps.md)
  Learn best practices for using memory efficiently in iOS and tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/copying-data-to-a-private-resource)*