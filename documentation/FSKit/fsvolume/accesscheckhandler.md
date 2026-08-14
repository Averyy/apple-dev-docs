# FSVolume.AccessCheckHandler

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that want to enforce access check operations.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol AccessCheckHandler : NSObjectProtocol
```

#### Overview

> ❗ **Important**: This protocol replaces the [`FSVolume.AccessCheckOperations`](fsvolume/accesscheckoperations.md) protocol. It exposes the same functionality, while using the [`FSCheckAccessResult`](fscheckaccessresult.md) object, to align with all other `Handler` protocols.

## Topics

### Checking access
- [func checkAccess(to: FSItem, requestedAccess: FSVolume.AccessMask, context: FSContext, replyHandler: (FSCheckAccessResult?, (any Error)?) -> Void)](fsvolume/accesscheckhandler/checkaccess(to:requestedaccess:context:replyhandler:).md)
  Checks whether the file system allows access to the given item.
- [FSVolume.AccessMask](fsvolume/accessmask.md)
  A bitmask of access rights.
- [class FSCheckAccessResult](fscheckaccessresult.md)
  The result of a check-access call.
### Inspecting volume properties
- [var isAccessCheckInhibited: Bool](fsvolume/accesscheckhandler/isaccesscheckinhibited.md)
  A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [FSVolume.OpenCloseHandler](fsvolume/openclosehandler.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteHandler](fsvolume/readwritehandler.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
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
- [FSVolume.SeekRegionHandler](fsvolume/seekregionhandler.md)
  Methods and properties implemented by volumes that support seek operations


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accesscheckhandler)*