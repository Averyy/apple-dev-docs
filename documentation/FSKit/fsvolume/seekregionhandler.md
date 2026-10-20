# FSVolume.SeekRegionHandler

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that support seek operations

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol SeekRegionHandler : NSObjectProtocol
```

```objc
@protocol FSVolumeSeekRegionHandler <NSObject>
```

## Topics

### Performing seek
- [func seek(within: FSItem, from: off_t, region: FSVolume.SeekRegion, context: FSContext, replyHandler: (FSSeekRegionResult?, (any Error)?) -> Void)](./seekregionhandler/seek%28within,from,region,context,replyhandler%29.md)
  Find the next offset of hole or data region greater than or equal to the supplied offset
- [class FSItem](../fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [FSVolume.SeekRegion](./seekregion.md)
  Types of region for seek operations
- [class FSContext](../fscontext.md)
  A context object that provides information about the initiator of a file system operation.
- [class FSSeekRegionResult](../fsseekregionresult.md)
  A seek-region result.
### Inspecting seek properties
- [var isSeekRegionInhibited: Bool](./seekregionhandler/isseekregioninhibited.md)
  A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Implementing optional handlers
- [FSVolume.OpenCloseHandler](./openclosehandler.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteHandler](./readwritehandler.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckHandler](./accesscheckhandler.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [FSVolume.RenameHandler](./renamehandler.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.PreallocateHandler](./preallocatehandler.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrHandler](./xattrhandler.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivationHandler](./itemdeactivationhandler.md)
  Methods and properties implemented by volumes that support deactivating items.
- [FSVolume.KernelOffloadedIOHandler](./kerneloffloadediohandler.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.DataCacheHandler](./datacachehandler.md)
  Methods and properties implemented by volumes that coordinate kernel-level data caching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/seekregionhandler)*