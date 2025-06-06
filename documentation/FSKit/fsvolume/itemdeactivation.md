# FSVolume.ItemDeactivation

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that support deactivating items.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol ItemDeactivation : NSObjectProtocol
```

## Topics

### Deactivating an item
- [func deactivateItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/itemdeactivation/deactivateitem(_:replyhandler:).md)
  Notifies the file system that the kernel is no longer making immediate use of the given item.
### Setting deactivation policy
- [var itemDeactivationPolicy: FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivation/itemdeactivationpolicy.md)
  A property that tells FSKit to which types of items the deactivation applies, if any.
- [FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivationoptions.md)
  Options to specify the item deactivation policy.

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
- [FSVolume.RenameOperations](fsvolume/renameoperations.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [protocol FSVolumeKernelOffloadedIOOperations](fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.PreallocateOperations](fsvolume/preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrOperations](fsvolume/xattroperations.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivation)*