# FSVolume.RenameOperations

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that support renaming the volume.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
protocol RenameOperations : NSObjectProtocol
```

```objc
@protocol FSVolumeRenameOperations <NSObject>
```

#### Overview

> **Deprecated**: Use [`FSVolume.RenameHandler`](./renamehandler.md) instead.

## Topics

### Renaming the volume
- [func setVolumeName(FSFileName, replyHandler: (FSFileName?, (any Error)?) -> Void)](./renameoperations/setvolumename%28_,replyhandler%29.md)
  Sets a new name for the volume.
### Inspecting volume properties
- [var isVolumeRenameInhibited: Bool](./renameoperations/isvolumerenameinhibited.md)
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
- [FSVolume.PreallocateOperations](./preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrOperations](./xattroperations.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivation](./itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.
- [protocol FSVolumeKernelOffloadedIOOperations](../fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/renameoperations)*