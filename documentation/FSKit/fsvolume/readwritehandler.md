# FSVolume.ReadWriteHandler

**Framework**: FSKit  
**Kind**: protocol

Methods implemented for read and write operations that deliver data to and from the extension.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol ReadWriteHandler : NSObjectProtocol
```

#### Overview

Most volumes conform to either this protocol or [`FSVolume.KernelOffloadedIOHandler`](fsvolume/kerneloffloadediohandler.md). You can conform to both if you need to provide kernel-offloaded I/O only for certain files. In that case, files with the [`inhibitKernelOffloadedIO`](fsitem/attribute/inhibitkerneloffloadedio.md) attribute set use this protocol, and those without it use [`FSVolume.KernelOffloadedIOHandler`](fsvolume/kerneloffloadediohandler.md). A volume that doesn’t conform to either protocol can’t support any I/O operation.

> ❗ **Important**: This protocol replaces the [`FSVolume.ReadWriteOperations`](fsvolume/readwriteoperations.md) protocol. It exposes the same functionality, while using [`FSVolumeHandlerResult`](fsvolumehandlerresult.md) objects. These objects add the ability to reply with [`FSItem.Attributes`](fsitem/attributes.md) and free space from the relevant methods.

## Topics

### Reading and writing
- [func read(from: FSItem, at: off_t, length: Int, into: FSMutableFileDataBuffer, replyHandler: (FSReadFileResult?, (any Error)?) -> Void)](fsvolume/readwritehandler/read(from:at:length:into:replyhandler:).md)
  Reads the contents of the given file item.
- [class FSMutableFileDataBuffer](fsmutablefiledatabuffer.md)
  A wrapper object for a data buffer.
- [class FSReadFileResult](fsreadfileresult.md)
  The result of a read-file call.
- [func write(contents: Data, to: FSItem, at: off_t, replyHandler: (FSWriteFileResult?, (any Error)?) -> Void)](fsvolume/readwritehandler/write(contents:to:at:replyhandler:).md)
  Writes contents to the given file item.
- [class FSWriteFileResult](fswritefileresult.md)
  The result of a read-file call.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [FSVolume.OpenCloseHandler](fsvolume/openclosehandler.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.AccessCheckHandler](fsvolume/accesscheckhandler.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [FSVolume.RenameHandler](fsvolume/renamehandler.md)
  Methods and properties implemented by volumes that support renaming the volume.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/readwritehandler)*