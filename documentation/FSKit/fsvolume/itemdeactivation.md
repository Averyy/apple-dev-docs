# FSVolume.ItemDeactivation

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that support deactivating items.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
protocol ItemDeactivation : NSObjectProtocol
```

```objc
@protocol FSVolumeItemDeactivation <NSObject>
```

## Topics

### Deactivating an item
- [func deactivateItem(FSItem, replyHandler: ((any Error)?) -> Void)](./itemdeactivation/deactivateitem%28_,replyhandler%29.md)
  Notifies the file system that the kernel is no longer making immediate use of the given item.
### Setting deactivation policy
- [var itemDeactivationPolicy: FSVolume.ItemDeactivationOptions](./itemdeactivation/itemdeactivationpolicy.md)
  A property that tells FSKit to which types of items the deactivation applies, if any.
- [FSVolume.ItemDeactivationOptions](./itemdeactivationoptions.md)
  Options to specify the item deactivation policy.

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
- [FSVolume.RenameOperations](./renameoperations.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.PreallocateOperations](./preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrOperations](./xattroperations.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [protocol FSVolumeKernelOffloadedIOOperations](../fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivation)*