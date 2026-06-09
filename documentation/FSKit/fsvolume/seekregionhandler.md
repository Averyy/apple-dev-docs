# FSVolume.SeekRegionHandler

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that support seek operations

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol SeekRegionHandler : NSObjectProtocol
```

## Topics

### Performing seek
- [func seek(within: FSItem, from: off_t, region: FSVolume.SeekRegion, context: FSContext, replyHandler: (FSSeekRegionResult?, (any Error)?) -> Void)](fsvolume/seekregionhandler/seek(within:from:region:context:replyhandler:).md)
  Find the next offset of hole or data region greater than or equal to the supplied offset
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [FSVolume.SeekRegion](fsvolume/seekregion.md)
  Types of region for seek operations
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.
- [class FSSeekRegionResult](fsseekregionresult.md)
  A seek-region result.
### Inspecting seek properties
- [var isSeekRegionInhibited: Bool](fsvolume/seekregionhandler/isseekregioninhibited.md)
  A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

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
- [FSVolume.KernelOffloadedIOHandler](fsvolume/kerneloffloadediohandler.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.DataCacheHandler](fsvolume/datacachehandler.md)
  Methods and properties implemented by volumes that coordinate kernel-level data caching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/seekregionhandler)*