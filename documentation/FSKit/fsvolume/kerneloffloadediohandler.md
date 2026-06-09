# FSVolume.KernelOffloadedIOHandler

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol KernelOffloadedIOHandler : NSObjectProtocol
```

#### Overview

A volume that conforms to this protocol supplies file extent mappings to FSKit, which allows file data transfers to take place in the kernel. This approach provides higher-performance data transfer than transferring all file data between the module and kernel, while still allowing the file system to run in user space.

This protocol uses *extents* to provide the kernel the logical-to-physical mapping of a given file. An extent describes a physical offset on disk, and a length and a logical offset within the file. You don’t manage extents directly. Instead, FSKit provides you with an [`FSExtentPacker`](fsextentpacker.md) to define and pack the extents in your implementations of this protocol’s methods.

Most volumes conform to either this protocol or [`FSVolume.ReadWriteHandler`](fsvolume/readwritehandler.md). You can conform to both if you need to provide kernel-offloaded I/O only for certain files. In that case, files with the [`inhibitKernelOffloadedIO`](fsitem/attribute/inhibitkerneloffloadedio.md) attribute set use [`FSVolume.ReadWriteHandler`](fsvolume/readwritehandler.md), and those without it use this protocol. A volume that doesn’t conform to either protocol can’t support any file I/O operation.

> ❗ **Important**: This protocol replaces the [`FSVolumeKernelOffloadedIOOperations`](fsvolumekerneloffloadediooperations.md) protocol. It exposes the same functionality, while using [`FSVolumeHandlerResult`](fsvolumehandlerresult.md) objects. These objects add the ability to reply with [`FSItem.Attributes`](fsitem/attributes.md) and free space from the relevant methods.

## Topics

### Performing mapped I/O
- [func blockmapFile(FSItem, offset: off_t, length: Int, flags: FSBlockmapFlags, operationID: FSOperationID, packer: FSExtentPacker, replyHandler: (FSBlockmapResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md)
  Maps a file’s disk space into extents, allowing the kernel to perform I/O with that space.
- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [class FSBlockmapResult](fsblockmapresult.md)
  The result of a blockmap call.
- [func completeIO(for: FSItem, offset: off_t, length: Int, status: any Error, flags: FSCompleteIOFlags, operationID: FSOperationID, replyHandler: (FSCompleteIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/completeio(for:offset:length:status:flags:operationid:replyhandler:).md)
  Completes an I/O operation for a given file.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSCompleteIOResult](fscompleteioresult.md)
  The result of a complete-I/O call.
### Working with items
- [func createFile(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, packer: FSExtentPacker, context: FSContext, replyHandler: (FSCreateFileKOIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/createfile(named:in:attributes:packer:context:replyhandler:).md)
  Creates a new file item and map its disk space.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSCreateFileKOIOResult](fscreatefilekoioresult.md)
  The result of a kernel-offloaded create-file call.
- [func lookupItem(named: FSFileName, in: FSItem, packer: FSExtentPacker, context: FSContext, replyHandler: (FSLookupItemKOIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/lookupitem(named:in:packer:context:replyhandler:).md)
  Looks up an item within a directory and maps its disk space.
- [class FSLookupItemKOIOResult](fslookupitemkoioresult.md)
  The result of a kernel-offloaded lookup-item call.
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, packer: FSExtentPacker, context: FSContext, replyHandler: (FSPreallocateKOIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/preallocatespace(for:at:length:flags:packer:context:replyhandler:).md)
  Preallocates and maps disk space for the given file.
- [FSVolume.PreallocateFlags](fsvolume/preallocateflags.md)
  Behavior flags for preallocation operations.
- [class FSPreallocateKOIOResult](fspreallocatekoioresult.md)
  The result of a kernel-offloaded preallocate call.
### Mapping file extents
- [class FSExtentPacker](fsextentpacker.md)
  A type that directs the kernel to map space on disk to a specific file managed by this file system.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [FSVolume.OpenCloseHandler](fsvolume/openclosehandler.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteHandler](fsvolume/readwritehandler.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckHandler](fsvolume/accesscheckhandler.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [FSVolume.RenameHandler](fsvolume/renamehandler.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.PreallocateHandler](fsvolume/preallocatehandler.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrHandler](fsvolume/xattrhandler.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivationHandler](fsvolume/itemdeactivationhandler.md)
  Methods and properties implemented by volumes that support deactivating items.
- [FSVolume.DataCacheHandler](fsvolume/datacachehandler.md)
  Methods and properties implemented by volumes that coordinate kernel-level data caching.
- [FSVolume.SeekRegionHandler](fsvolume/seekregionhandler.md)
  Methods and properties implemented by volumes that support seek operations


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kerneloffloadediohandler)*