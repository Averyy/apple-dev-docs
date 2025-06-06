# Transferring Data Between Connected GPUs

**Framework**: Metal

Use high-speed connections between GPUs to transfer data quickly.

#### Overview

Starting with macOS 10.15, some Mac systems directly connect GPUs to each other, allowing you to quickly transfer data between them. These connections are not only faster, but they also avoid using the memory bus between the CPU and GPUs, leaving it available for other tasks. If your app uses multiple GPUs, test to see if they’re connected, and when they are, use the transfer mechanism described here.

When GPUs are connected to each other, they’re said to be in the same . You determine whether a GPU is in a peer group by reading the device object’s [`peerGroupID`](mtldevice/peergroupid.md) property. A nonzero value indicates that the GPU is in a peer group.

GPUs in the same peer group share the same peer group ID. 

You can get the list of all devices associated with a peer group by filtering on this ID.

##### Copy Resources to the Gpu That Needs to Access Them

In Metal, resources are created by device objects, and are always associated with the device object that created them. Peer groups don’t change that association. If a resource is associated with a device object, and you want to access it on another device object, you need to copy the data to a resource associated with the second device object.

To copy data between members of a peer group, make a  on the second GPU that’s connected to the resource you want to copy. A remote view is a resource object that contains no storage of its own; it references the storage on the original GPU. You can only use remote views to copy data; using them in other Metal commands results in an error.

##### Create a Remote View of a Resource

To create a remote view of a resource, the device object you make the resource view on must share the same [`peerGroupID`](mtldevice/peergroupid.md) as the device object that created the resource. In addition, the resource must use the [`MTLStorageMode.private`](mtlstoragemode/private.md) storage mode or be backed by an [`IOSurface`](https://developer.apple.com/documentation/IOSurface/IOSurface).

To create a buffer view, call the [`makeRemoteBufferView(_:)`](mtlbuffer/makeremotebufferview(_:).md) method:

Similarly, to create a texture view, call the [`makeRemoteTextureView(_:)`](mtltexture/makeremotetextureview(_:).md) method.

##### Copy Data Between Connected Gpus

Create a [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) and encode a copy command. The source for this copy command is the remote view object:

As shown in the following illustration, there are three resource objects: the original resource that contains the data, a remote view that references the data, and a resource that receives the data.

![A figure showing two devices. The source buffer or texture is created by the first device. The second device has a remote view of the source texture and a destination texture.](https://docs-assets.developer.apple.com/published/9bd44e5a93a5da65ff277553c3c99ad1/media-3195113%402x.png)

##### Synchronize Access to Resources

Blit commands used in peer-to-peer transfers follow all of the usual synchronization rules on the GPU they’re performed on. However, they don’t automatically synchronize with any commands running on the source GPU. If you encode commands that modify the source resource, ensure that those commands are complete before executing the blit command to transfer the data to the other GPU. This is the same as what you do when transferring resources between GPUs through system memory.

To synchronize commands between different device objects, use shared events. See [`Synchronizing Events Across Multiple Devices or Processes`](synchronizing-events-across-multiple-devices-or-processes.md) and [`Implementing a Multistage Image Filter Using Heaps and Events`](implementing-a-multistage-image-filter-using-heaps-and-events.md).

## See Also

- [Setting Resource Storage Modes](setting-resource-storage-modes.md)
  Set a storage mode that defines the memory location and access permissions of a resource.
- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
  Select an appropriate storage mode for your textures and buffers on Apple GPUs.
- [Choosing a Resource Storage Mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
  Select an appropriate storage mode for your textures and buffers on AMD and Intel GPUs.
- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)
  Use a blit command encoder to copy buffer or texture data to a private resource.
- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)
  Manually synchronize memory for a Metal resource in apps.
- [Reducing the Memory Footprint of Metal Apps](reducing-the-memory-footprint-of-metal-apps.md)
  Learn best practices for using memory efficiently in iOS and tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/transferring-data-between-connected-gpus)*