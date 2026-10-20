# FSVolume.Operations

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods that all volumes implement to provide required capabilities.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
protocol Operations : FSVolume.CommonOperations, FSVolume.PathConfOperations
```

```objc
@protocol FSVolumeOperations <NSObject, FSVolumeCommonOperations, FSVolumePathConfOperations>
```

#### Overview

Conform to this protocol in your subclass of [`FSVolume`](../fsvolume.md). To provide additional capabilities, conform to the other `FSVolume` operations protocols, such as [`FSVolume.OpenCloseOperations`](./opencloseoperations.md) and [`FSVolume.ReadWriteOperations`](./readwriteoperations.md).

> **Note**: This protocol extends [`FSVolume.PathConfOperations`](./pathconfoperations.md), so your volume implementation must also conform to that protocol.

> **Deprecated**: Use [`FSVolume.Handler`](./handler.md) instead.

## Topics

### Handling activation and deactivation
- [func activate(options: FSTaskOptions, replyHandler: (FSItem?, (any Error)?) -> Void)](./operations/activate%28options,replyhandler%29.md)
  Activates the volume using the specified options.
- [class FSItem](../fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [func deactivate(options: FSDeactivateOptions, replyHandler: ((any Error)?) -> Void)](./operations/deactivate%28options,replyhandler%29.md)
  Tears down a previously initialized volume instance.
- [struct FSDeactivateOptions](../fsdeactivateoptions.md)
  Options that affect the behavior of deactivate methods.
### Working with items
- [func createItem(named: FSFileName, type: FSItem.ItemType, inDirectory: FSItem, attributes: FSItem.SetAttributesRequest, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./operations/createitem%28named,type,indirectory,attributes,replyhandler%29.md)
  Creates a new file or directory item.
- [class FSFileName](../fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.ItemType](../fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.SetAttributesRequest](../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func lookupItem(named: FSFileName, inDirectory: FSItem, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./operations/lookupitem%28named,indirectory,replyhandler%29.md)
  Looks up an item within a directory.
- [func removeItem(FSItem, named: FSFileName, fromDirectory: FSItem, replyHandler: ((any Error)?) -> Void)](./operations/removeitem%28_,named,fromdirectory,replyhandler%29.md)
  Removes an existing item from a given directory.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, replyHandler: (FSFileName?, (any Error)?) -> Void)](./operations/renameitem%28_,indirectory,named,to,indirectory,overitem,replyhandler%29.md)
  Renames an item from one path in the file system to another.
### Working with links
- [func createLink(to: FSItem, named: FSFileName, inDirectory: FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](./operations/createlink%28to,named,indirectory,replyhandler%29.md)
  Creates a new hard link.
- [func createSymbolicLink(named: FSFileName, inDirectory: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](./operations/createsymboliclink%28named,indirectory,attributes,linkcontents,replyhandler%29.md)
  Creates a new symbolic link.
- [func readSymbolicLink(FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](./operations/readsymboliclink%28_,replyhandler%29.md)
  Reads a symbolic link.
### Working with attributes
- [func getAttributes(FSItem.GetAttributesRequest, of: FSItem, replyHandler: (FSItem.Attributes?, (any Error)?) -> Void)](./operations/getattributes%28_,of,replyhandler%29.md)
  Fetches attributes for the given item.
- [FSItem.GetAttributesRequest](../fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [func setAttributes(FSItem.SetAttributesRequest, on: FSItem, replyHandler: (FSItem.Attributes?, (any Error)?) -> Void)](./operations/setattributes%28_,on,replyhandler%29.md)
  Sets the given attributes on an item.
- [FSItem.SetAttributesRequest](../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
### Inspecting directory contents
- [func enumerateDirectory(FSItem, startingAt: FSDirectoryCookie, verifier: FSDirectoryVerifier, attributes: FSItem.GetAttributesRequest?, packer: FSDirectoryEntryPacker, replyHandler: (FSDirectoryVerifier, (any Error)?) -> Void)](./operations/enumeratedirectory%28_,startingat,verifier,attributes,packer,replyhandler%29.md)
  Enumerates the contents of the given directory.
- [struct FSDirectoryCookie](../fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryCookie](../fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryVerifier](../fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [struct FSDirectoryVerifier](../fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [class FSDirectoryEntryPacker](../fsdirectoryentrypacker.md)
  An object used to provide items during a directory enumeration.
### Synchronizing with a resource
- [enum FSSyncFlags](../fssyncflags.md)
  Behavior flags for use with synchronization calls.
### Inspecting required volume properties
- [FSVolume.SupportedCapabilities](./supportedcapabilities.md)
  A type that represents capabilities supported by a volume, such as hard and symbolic links, journaling, and large file sizes.
- [class FSStatFSResult](../fsstatfsresult.md)
  A type used to report a volume’s statistics.
### Inspecting optional volume properties
- [FSVolume.MountOptions](./mountoptions.md)
  Mount options to be requested from FSKit using the `requestedMountOptions` property.

## Relationships

### Inherits From
- [FSVolume.CommonOperations](./commonoperations.md)
- [FSVolume.PathConfOperations](./pathconfoperations.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated
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
- [FSVolume.ItemDeactivation](./itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.
- [protocol FSVolumeKernelOffloadedIOOperations](../fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations)*