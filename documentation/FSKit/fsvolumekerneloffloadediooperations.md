# FSVolumeKernelOffloadedIOOperations

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol FSVolumeKernelOffloadedIOOperations : NSObjectProtocol
```

#### Overview

A volume that conforms to this protocol supplies file extent mappings to FSKit, which allows file transfers to take place in the kernel. This approach provides higher-performance file transfer than transferring data between the module and kernel, while still allowing the file system to run in user space.

This protocol uses  to provide the kernel the logical-to-physical mapping of a given file. An extent describes a physical offset on disk, and a length and a logical offset within the file. You don’t manage extents directly. Instead, FSKit provides you with an [`FSExtentPacker`](fsextentpacker.md) to define and pack the extents in your implementations of this protocol’s methods.

Most volumes conform to either this protocol or [`FSVolume.ReadWriteOperations`](fsvolume/readwriteoperations.md). You can conform to both if you need to provide kernel-offloaded I/O only for certain files. In that case, files with the [`inhibitKernelOffloadedIO`](fsitem/attribute/inhibitkerneloffloadedio.md) attribute set use [`FSVolume.ReadWriteOperations`](fsvolume/readwriteoperations.md), and those without it use this protocol. A volume that doesn’t conform to either protocol can’t support any I/O operation.

## Topics

### Performing mapped I/O
- [func blockmapFile(FSItem, offset: off_t, length: Int, flags: FSBlockmapFlags, operationID: FSOperationID, packer: FSExtentPacker, replyHandler: ((any Error)?) -> Void)](fsvolumekerneloffloadediooperations/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md)
  Maps a file’s disk space into extents, allowing the kernel to perform I/O with that space.
- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [func completeIO(for: FSItem, offset: off_t, length: Int, status: any Error, flags: FSCompleteIOFlags, operationID: FSOperationID, replyHandler: ((any Error)?) -> Void)](fsvolumekerneloffloadediooperations/completeio(for:offset:length:status:flags:operationid:replyhandler:).md)
  Completes an I/O operation for a given file.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
### Working with items
- [func createFile(name: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolumekerneloffloadediooperations/createfile(name:in:attributes:packer:replyhandler:).md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func lookupItem(name: FSFileName, in: FSItem, packer: FSExtentPacker, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolumekerneloffloadediooperations/lookupitem(name:in:packer:replyhandler:).md)
  Looks up an item within a directory and maps its disk space.
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, replyHandler: (Int, (any Error)?) -> Void)](fsvolumekerneloffloadediooperations/preallocatespace(for:at:length:flags:packer:replyhandler:).md)
  Preallocates and maps disk space for the given file.
- [FSVolume.PreallocateFlags](fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.
### Mapping file extents
- [class FSExtentPacker](fsextentpacker.md)
  A type that directs the kernel to map space on disk to a specific file managed by this file system.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [FSVolume.OpenCloseOperations](fsvolume/opencloseoperations.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteOperations](fsvolume/readwriteoperations.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckOperations](fsvolume/accesscheckoperations.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [FSVolume.RenameOperations](fsvolume/renameoperations.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.PreallocateOperations](fsvolume/preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrOperations](fsvolume/xattroperations.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivation](fsvolume/itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumekerneloffloadediooperations)*