# FSVolume.AccessCheckHandler

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that want to enforce access check operations.

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol AccessCheckHandler : NSObjectProtocol
```

```objc
@protocol FSVolumeAccessCheckHandler <NSObject>
```

## Overview

> ❗ **Important**: This protocol replaces the [`FSVolume.AccessCheckOperations`](./accesscheckoperations.md) protocol. It exposes the same functionality, while using the [`FSCheckAccessResult`](../fscheckaccessresult.md) object, to align with all other `Handler` protocols.

## Topics

### Checking access
- [func checkAccess(to: FSItem, requestedAccess: FSVolume.AccessMask, context: FSContext, replyHandler: (FSCheckAccessResult?, (any Error)?) -> Void)](./accesscheckhandler/checkaccess%28to,requestedaccess,context,replyhandler%29.md)
  Checks whether the file system allows access to the given item.
- [FSVolume.AccessMask](./accessmask.md)
  A bitmask of access rights.
- [class FSCheckAccessResult](../fscheckaccessresult.md)
  The result of a check-access call.
### Inspecting volume properties
- [var isAccessCheckInhibited: Bool](./accesscheckhandler/isaccesscheckinhibited.md)
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
- [FSVolume.SeekRegionHandler](./seekregionhandler.md)
  Methods and properties implemented by volumes that support seek operations


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accesscheckhandler)*