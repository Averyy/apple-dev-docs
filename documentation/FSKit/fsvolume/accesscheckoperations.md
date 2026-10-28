# FSVolume.AccessCheckOperations

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that want to enforce access check operations.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
protocol AccessCheckOperations : NSObjectProtocol
```

```objc
@protocol FSVolumeAccessCheckOperations <NSObject>
```

## Overview

> **Deprecated**: Use [`FSVolume.AccessCheckHandler`](./accesscheckhandler.md) instead.

## Topics

### Checking access
- [func checkAccess(to: FSItem, requestedAccess: FSVolume.AccessMask, replyHandler: (Bool, (any Error)?) -> Void)](./accesscheckoperations/checkaccess%28to,requestedaccess,replyhandler%29.md)
  Checks whether the file system allows access to the given item.
- [FSVolume.AccessMask](./accessmask.md)
  A bitmask of access rights.
### Inspecting volume properties
- [var isAccessCheckInhibited: Bool](./accesscheckoperations/isaccesscheckinhibited.md)
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
- [FSVolume.RenameOperations](./renameoperations.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.PreallocateOperations](./preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrOperations](./xattroperations.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivation](./itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.
- [protocol FSVolumeKernelOffloadedIOOperations](../fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accesscheckoperations)*