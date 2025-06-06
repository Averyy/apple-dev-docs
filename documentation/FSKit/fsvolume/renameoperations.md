# FSVolume.RenameOperations

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that support renaming the volume.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol RenameOperations : NSObjectProtocol
```

## Topics

### Renaming the volume
- [func setVolumeName(FSFileName, replyHandler: (FSFileName?, (any Error)?) -> Void)](fsvolume/renameoperations/setvolumename(_:replyhandler:).md)
  Sets a new name for the volume.
### Inspecting volume properties
- [var isVolumeRenameInhibited: Bool](fsvolume/renameoperations/isvolumerenameinhibited.md)
  A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [FSVolume.OpenCloseOperations](fsvolume/opencloseoperations.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteOperations](fsvolume/readwriteoperations.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckOperations](fsvolume/accesscheckoperations.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [protocol FSVolumeKernelOffloadedIOOperations](fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.PreallocateOperations](fsvolume/preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrOperations](fsvolume/xattroperations.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivation](fsvolume/itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/renameoperations)*