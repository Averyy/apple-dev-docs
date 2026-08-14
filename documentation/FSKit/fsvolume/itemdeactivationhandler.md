# FSVolume.ItemDeactivationHandler

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that support deactivating items.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol ItemDeactivationHandler : NSObjectProtocol
```

#### Overview

> ❗ **Important**: This protocol replaces the [`FSVolume.ItemDeactivation`](fsvolume/itemdeactivation.md) protocol. It exposes the same functionality, while using the [`FSDeactivateItemResult`](fsdeactivateitemresult.md) object. This object adds the ability to reply with free space from [`deactivateItem(_:context:replyHandler:)`](fsvolume/itemdeactivationhandler/deactivateitem(_:context:replyhandler:).md).

## Topics

### Deactivating an item
- [func deactivateItem(FSItem, context: FSContext, replyHandler: (FSDeactivateItemResult?, (any Error)?) -> Void)](fsvolume/itemdeactivationhandler/deactivateitem(_:context:replyhandler:).md)
  Notifies the file system that the kernel is no longer making immediate use of the given item.
- [class FSDeactivateItemResult](fsdeactivateitemresult.md)
  The result of a deactivate-item call.
### Inspecting volume properties
- [var itemDeactivationPolicy: FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivationhandler/itemdeactivationpolicy.md)
  A property that tells FSKit to which types of items the deactivation applies, if any.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [FSVolume.OpenCloseHandler](fsvolume/openclosehandler.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteHandler](fsvolume/readwritehandler.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckHandler](fsvolume/accesscheckhandler.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [FSVolume.RenameHandler](fsvolume/renamehandler.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.PreallocateHandler](fsvolume/preallocatehandler.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrHandler](fsvolume/xattrhandler.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.KernelOffloadedIOHandler](fsvolume/kerneloffloadediohandler.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.DataCacheHandler](fsvolume/datacachehandler.md)
  Methods and properties implemented by volumes that coordinate kernel-level data caching.
- [FSVolume.SeekRegionHandler](fsvolume/seekregionhandler.md)
  Methods and properties implemented by volumes that support seek operations


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivationhandler)*