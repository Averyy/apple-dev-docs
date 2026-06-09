# FSVolume.AccessCheckOperations

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that want to enforce access check operations.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol AccessCheckOperations : NSObjectProtocol
```

#### Overview

> **Note**:  Use [`FSVolume.AccessCheckHandler`](fsvolume/accesscheckhandler.md) instead.

## Topics

### Checking access
- [FSVolume.AccessMask](fsvolume/accessmask.md)
  A bitmask of access rights.
### Inspecting volume properties
- [var isAccessCheckInhibited: Bool](fsvolume/accesscheckoperations/isaccesscheckinhibited.md)
  A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.
### Instance Methods
- [func checkAccess(to: FSItem, requestedAccess: FSVolume.AccessMask, replyHandler: (Bool, (any Error)?) -> Void)](fsvolume/accesscheckoperations/checkaccess(to:requestedaccess:replyhandler:).md)
  Checks whether the file system allows access to the given item.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [FSVolume.Operations](fsvolume/operations.md)
  Methods that all volumes implement to provide required capabilities.
- [FSVolume.OpenCloseOperations](fsvolume/opencloseoperations.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteOperations](fsvolume/readwriteoperations.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.RenameOperations](fsvolume/renameoperations.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.PreallocateOperations](fsvolume/preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrOperations](fsvolume/xattroperations.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivation](fsvolume/itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.
- [protocol FSVolumeKernelOffloadedIOOperations](fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/accesscheckoperations)*