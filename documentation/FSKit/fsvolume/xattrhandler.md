# FSVolume.XattrHandler

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that natively or partially support extended attributes.

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol XattrHandler : NSObjectProtocol
```

```objc
@protocol FSVolumeXattrHandler <NSObject>
```

## Overview

> ❗ **Important**: This protocol replaces the [`FSVolume.XattrOperations`](./xattroperations.md) protocol. It exposes the same functionality, while using [`FSVolumeHandlerResult`](../fsvolumehandlerresult.md) objects. These objects add the ability to reply with [`FSItem.Attributes`](../fsitem/attributes.md) and free space from the relevant methods.

## Topics

### Reading and writing
- [func getXattr(named: FSFileName, of: FSItem, context: FSContext, replyHandler: (FSGetXattrResult?, (any Error)?) -> Void)](./xattrhandler/getxattr%28named,of,context,replyhandler%29.md)
  Gets the specified extended attribute of the given item.
- [class FSGetXattrResult](../fsgetxattrresult.md)
  The result of a get-extended-attributes call.
- [func listXattrs(of: FSItem, context: FSContext, replyHandler: (FSListXattrsResult?, (any Error)?) -> Void)](./xattrhandler/listxattrs%28of,context,replyhandler%29.md)
  Gets the list of extended attributes currently set on the given item.
- [class FSListXattrsResult](../fslistxattrsresult.md)
  The result of a list-extended-attributes call.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, context: FSContext, replyHandler: (FSSetXattrResult?, (any Error)?) -> Void)](./xattrhandler/setxattr%28named,to,on,policy,context,replyhandler%29.md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](./setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [class FSSetXattrResult](../fssetxattrresult.md)
  The result of a set-extended-attributes call.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](./xattrhandler/supportedxattrnames%28for%29.md)
  Returns an array that specifies the extended attribute names the given item supports.
### Inspecting volume properties
- [var xattrOperationsInhibited: Bool](./xattrhandler/xattroperationsinhibited.md)
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
- [FSVolume.ItemDeactivationHandler](./itemdeactivationhandler.md)
  Methods and properties implemented by volumes that support deactivating items.
- [FSVolume.KernelOffloadedIOHandler](./kerneloffloadediohandler.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.DataCacheHandler](./datacachehandler.md)
  Methods and properties implemented by volumes that coordinate kernel-level data caching.
- [FSVolume.SeekRegionHandler](./seekregionhandler.md)
  Methods and properties implemented by volumes that support seek operations


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattrhandler)*