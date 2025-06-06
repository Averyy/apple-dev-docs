# FSVolume.ReadWriteOperations

**Framework**: FSKit  
**Kind**: protocol

Methods implemented for read and write operations that deliver data to and from the extension.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol ReadWriteOperations : NSObjectProtocol
```

#### Overview

Most volumes conform to either this protocol or [`FSVolumeKernelOffloadedIOOperations`](fsvolumekerneloffloadediooperations.md). You can conform to both if you need to provide kernel-offloaded I/O only for certain files. In that case, files with the [`inhibitKernelOffloadedIO`](fsitem/attribute/inhibitkerneloffloadedio.md) attribute set use this protocol, and those without it use [`FSVolumeKernelOffloadedIOOperations`](fsvolumekerneloffloadediooperations.md). A volume that doesn’t conform to either protocol can’t support any I/O operation.

## Topics

### Reading and writing
- [func read(from: FSItem, at: off_t, length: Int, into: FSMutableFileDataBuffer, replyHandler: (Int, (any Error)?) -> Void)](fsvolume/readwriteoperations/read(from:at:length:into:replyhandler:).md)
  Reads the contents of the given file item.
- [class FSMutableFileDataBuffer](fsmutablefiledatabuffer.md)
  A wrapper object for a data buffer.
- [func write(contents: Data, to: FSItem, at: off_t, replyHandler: (Int, (any Error)?) -> Void)](fsvolume/readwriteoperations/write(contents:to:at:replyhandler:).md)
  Writes contents to the given file item.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [FSVolume.OpenCloseOperations](fsvolume/opencloseoperations.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/readwriteoperations)*