# FSVolume.XattrOperations

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that natively or partially support extended attributes.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
protocol XattrOperations : NSObjectProtocol
```

```objc
@protocol FSVolumeXattrOperations <NSObject>
```

## Overview

> **Deprecated**: Use [`FSVolume.XattrHandler`](./xattrhandler.md)

## Topics

### Reading and writing
- [func getXattr(named: FSFileName, of: FSItem, replyHandler: (Data?, (any Error)?) -> Void)](./xattroperations/getxattr%28named,of,replyhandler%29.md)
  Gets the specified extended attribute of the given item.
- [func listXattrs(of: FSItem, replyHandler: ([FSFileName]?, (any Error)?) -> Void)](./xattroperations/listxattrs%28of,replyhandler%29.md)
  Gets the list of extended attributes currently set on the given item.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, replyHandler: ((any Error)?) -> Void)](./xattroperations/setxattr%28named,to,on,policy,replyhandler%29.md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](./setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](./xattroperations/supportedxattrnames%28for%29.md)
  Returns an array that specifies the extended attribute names the given item supports.
### Inspecting volume properties
- [var xattrOperationsInhibited: Bool](./xattroperations/xattroperationsinhibited.md)
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
- [FSVolume.PreallocateOperations](./preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.ItemDeactivation](./itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.
- [protocol FSVolumeKernelOffloadedIOOperations](../fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations)*