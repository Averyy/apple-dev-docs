# FSVolume.XattrOperations

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that natively or partially support extended attributes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol XattrOperations : NSObjectProtocol
```

## Topics

### Reading and writing
- [func getXattr(named: FSFileName, of: FSItem, replyHandler: (Data?, (any Error)?) -> Void)](fsvolume/xattroperations/getxattr(named:of:replyhandler:).md)
  Gets the specified extended attribute of the given item.
- [func listXattrs(of: FSItem, replyHandler: ([FSFileName]?, (any Error)?) -> Void)](fsvolume/xattroperations/listxattrs(of:replyhandler:).md)
  Gets the list of extended attributes currently set on the given item.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, replyHandler: ((any Error)?) -> Void)](fsvolume/xattroperations/setxattr(named:to:on:policy:replyhandler:).md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](fsvolume/setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](fsvolume/xattroperations/supportedxattrnames(for:).md)
  Returns an array that specifies the extended attribute names the given item supports.
### Inspecting volume properties
- [var xattrOperationsInhibited: Bool](fsvolume/xattroperations/xattroperationsinhibited.md)
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
- [FSVolume.RenameOperations](fsvolume/renameoperations.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [protocol FSVolumeKernelOffloadedIOOperations](fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.PreallocateOperations](fsvolume/preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.ItemDeactivation](fsvolume/itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations)*