# FSVolume.RenameHandler

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that support renaming the volume.

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol RenameHandler : NSObjectProtocol
```

```objc
@protocol FSVolumeRenameHandler <NSObject>
```

#### Overview

> ❗ **Important**: This protocol replaces the [`FSVolume.RenameOperations`](./renameoperations.md) protocol. It exposes the same functionality, while using the [`FSVolumeRenameResult`](../fsvolumerenameresult.md) object, to align with all other `Handler` protocols.

## Topics

### Renaming the volume
- [func setVolumeName(FSFileName, context: FSContext, replyHandler: (FSVolumeRenameResult?, (any Error)?) -> Void)](./renamehandler/setvolumename%28_,context,replyhandler%29.md)
  Sets a new name for the volume.
- [class FSVolumeRenameResult](../fsvolumerenameresult.md)
  The result of a rename-volume call.
### Inspecting volume properties
- [var isVolumeRenameInhibited: Bool](./renamehandler/isvolumerenameinhibited.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/renamehandler)*