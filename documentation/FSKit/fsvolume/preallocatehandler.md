# FSVolume.PreallocateHandler

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that want to offer preallocation functions.

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol PreallocateHandler : NSObjectProtocol
```

```objc
@protocol FSVolumePreallocateHandler <NSObject>
```

#### Overview

A preallocation operation allocates space for a file without writing to it yet. A file system may use reallocation to avoid performing space allocation while in the midst of I/O; this strategy improves performance. Also, if the expected I/O pattern is many small writes, preallocating contiguous chunks may prevent fragmenting the file system. This process can improve performance later.

In a kernel-based file system, you typically preallocate space with the `VNOP_ALLOCATE` operation, called from `fcntl(F_PREALLOCATE)`.

> ❗ **Important**: This protocol replaces the [`FSVolume.PreallocateOperations`](./preallocateoperations.md) protocol. It exposes the same functionality, while using the [`FSPreallocateResult`](../fspreallocateresult.md) object. This objects adds the ability to reply with [`FSItem.Attributes`](../fsitem/attributes.md) and free space from [`preallocateSpace(for:at:length:flags:context:replyHandler:)`](./preallocatehandler/preallocatespace%28for,at,length,flags,context,replyhandler%29.md).

## Topics

### Preallocating space
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, context: FSContext, replyHandler: (FSPreallocateResult?, (any Error)?) -> Void)](./preallocatehandler/preallocatespace%28for,at,length,flags,context,replyhandler%29.md)
  Preallocates disk space for the given item.
- [FSVolume.PreallocateFlags](./preallocateflags.md)
  Behavior flags for preallocation operations.
- [class FSPreallocateResult](../fspreallocateresult.md)
  The result of a preallocate call.
### Inspecting volume properties
- [var isPreallocateInhibited: Bool](./preallocatehandler/ispreallocateinhibited.md)
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
- [FSVolume.XattrHandler](./xattrhandler.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivationHandler](./itemdeactivationhandler.md)
  Methods and properties implemented by volumes that support deactivating items.
- [FSVolume.KernelOffloadedIOHandler](./kerneloffloadediohandler.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.DataCacheHandler](./datacachehandler.md)
  Methods and properties implemented by volumes that coordinate kernel-level data caching.
- [FSVolume.SeekRegionHandler](./seekregionhandler.md)
  Methods and properties implemented by volumes that support seek operations


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocatehandler)*