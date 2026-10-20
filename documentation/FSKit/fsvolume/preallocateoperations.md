# FSVolume.PreallocateOperations

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that want to offer preallocation functions.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
protocol PreallocateOperations : NSObjectProtocol
```

```objc
@protocol FSVolumePreallocateOperations <NSObject>
```

#### Overview

A preallocation operation allocates space for a file without writing to it yet. A file system may use reallocation to avoid performing space allocation while in the midst of I/O; this strategy improves performance. Also, if the expected I/O pattern is many small writes, preallocating contiguous chunks may prevent fragmenting the file system. This process can improve performance later.

In a kernel-based file system, you typically preallocate space with the `VNOP_ALLOCATE` operation, called from `fcntl(F_PREALLOCATE)`.

> **Deprecated**: Use [`FSVolume.PreallocateHandler`](./preallocatehandler.md) instead.

## Topics

### Preallocating space
- [func preallocateSpace(for: FSItem, at: off_t, length: Int, flags: FSVolume.PreallocateFlags, replyHandler: (Int, (any Error)?) -> Void)](./preallocateoperations/preallocatespace%28for,at,length,flags,replyhandler%29.md)
  Preallocates disk space for the given item.
- [FSVolume.PreallocateFlags](./preallocateflags.md)
  Behavior flags for preallocation operations.
### Inspecting volume properties
- [var isPreallocateInhibited: Bool](./preallocateoperations/ispreallocateinhibited.md)
  A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated
- [FSVolume.Operations](./operations.md)
  Methods that all volumes implement to provide required capabilities.
- [FSVolume.OpenCloseOperations](./opencloseoperations.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteOperations](./readwriteoperations.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckOperations](./accesscheckoperations.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [FSVolume.RenameOperations](./renameoperations.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.XattrOperations](./xattroperations.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivation](./itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.
- [protocol FSVolumeKernelOffloadedIOOperations](../fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/preallocateoperations)*