# FSVolume.RenameHandler

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that support renaming the volume.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol RenameHandler : NSObjectProtocol
```

#### Overview

> ❗ **Important**: This protocol replaces the [`FSVolume.RenameOperations`](fsvolume/renameoperations.md) protocol. It exposes the same functionality, while using the [`FSVolumeRenameResult`](fsvolumerenameresult.md) object, to align with all other `Handler` protocols.

## Topics

### Renaming the volume
- [func setVolumeName(FSFileName, context: FSContext, replyHandler: (FSVolumeRenameResult?, (any Error)?) -> Void)](fsvolume/renamehandler/setvolumename(_:context:replyhandler:).md)
  Sets a new name for the volume.
- [class FSVolumeRenameResult](fsvolumerenameresult.md)
  The result of a rename-volume call.
### Inspecting volume properties
- [var isVolumeRenameInhibited: Bool](fsvolume/renamehandler/isvolumerenameinhibited.md)
  A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [FSVolume.OpenCloseHandler](fsvolume/openclosehandler.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteHandler](fsvolume/readwritehandler.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckHandler](fsvolume/accesscheckhandler.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/renamehandler)*