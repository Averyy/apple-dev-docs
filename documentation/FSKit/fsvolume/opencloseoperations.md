# FSVolume.OpenCloseOperations

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that want to receive open and close calls for each item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol OpenCloseOperations : NSObjectProtocol
```

#### Overview

When a file system volume conforms to this protocol, the kernel layer issues an open call to indicate desired access, and a close call to indicate what access to retain. A file is fully closed when the kernel layer issues a close call with no retained open nodes. When a file system receives the close call, it removes all access to the item. When all memory mappings to the item release, the kernel layer issues a final close.

If a file system volume doesn’t conform to this protocol, the kernel layer can skip making such calls to the volume.

## Topics

### Opening and closing
- [func openItem(FSItem, modes: FSVolume.OpenModes, replyHandler: ((any Error)?) -> Void)](fsvolume/opencloseoperations/openitem(_:modes:replyhandler:).md)
  Opens a file for access.
- [func closeItem(FSItem, modes: FSVolume.OpenModes, replyHandler: ((any Error)?) -> Void)](fsvolume/opencloseoperations/closeitem(_:modes:replyhandler:).md)
  Closes a file from further access.
- [FSVolume.OpenModes](fsvolume/openmodes.md)
  Defined modes for opening a file.
### Inspecting volume properties
- [var isOpenCloseInhibited: Bool](fsvolume/opencloseoperations/isopencloseinhibited.md)
  A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [FSVolume.ReadWriteOperations](fsvolume/readwriteoperations.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckOperations](fsvolume/accesscheckoperations.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [FSVolume.RenameOperations](fsvolume/renameoperations.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [protocol FSVolumeKernelOffloadedIOOperations](fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.PreallocateOperations](fsvolume/preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrOperations](fsvolume/xattroperations.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivation](fsvolume/itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/opencloseoperations)*