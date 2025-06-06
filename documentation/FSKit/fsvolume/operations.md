# FSVolume.Operations

**Framework**: FSKit  
**Kind**: protocol

Methods that all volumes implement to provide required capabilities.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol Operations : FSVolume.PathConfOperations
```

#### Overview

Conform to this protocol in your subclass of [`FSVolume`](fsvolume.md). To provide additional capabilities, conform to the other `FSVolume` operations protocols, like [`FSVolume.OpenCloseOperations`](fsvolume/opencloseoperations.md) and [`FSVolume.ReadWriteOperations`](fsvolume/readwriteoperations.md).

> **Note**: This protocol extends [`FSVolume.PathConfOperations`](fsvolume/pathconfoperations.md), so your volume implementation must also conform to that protocol.

This protocol extends [`FSVolume.PathConfOperations`](fsvolume/pathconfoperations.md), so your volume implementation must also conform to that protocol.

## Topics

### Handling activation and deactivation
- [func activate(options: FSTaskOptions, replyHandler: (FSItem?, (any Error)?) -> Void)](fsvolume/operations/activate(options:replyhandler:).md)
  Activates the volume using the specified options.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [func deactivate(options: FSDeactivateOptions, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/deactivate(options:replyhandler:).md)
  Tears down a previously initialized volume instance.
- [struct FSDeactivateOptions](fsdeactivateoptions.md)
  Options that affect the behavior of deactivate methods.
### Mounting and unmounting
- [func mount(options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/mount(options:replyhandler:).md)
  Mounts this volume, using the specified options.
- [func unmount(replyHandler: () -> Void)](fsvolume/operations/unmount(replyhandler:).md)
  Unmounts this volume.
### Working with items
- [func createItem(named: FSFileName, type: FSItem.ItemType, inDirectory: FSItem, attributes: FSItem.SetAttributesRequest, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolume/operations/createitem(named:type:indirectory:attributes:replyhandler:).md)
  Creates a new file or directory item.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.ItemType](fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [func lookupItem(named: FSFileName, inDirectory: FSItem, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolume/operations/lookupitem(named:indirectory:replyhandler:).md)
  Looks up an item within a directory.
- [func removeItem(FSItem, named: FSFileName, fromDirectory: FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/removeitem(_:named:fromdirectory:replyhandler:).md)
  Removes an existing item from a given directory.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, replyHandler: (FSFileName?, (any Error)?) -> Void)](fsvolume/operations/renameitem(_:indirectory:named:to:indirectory:overitem:replyhandler:).md)
  Renames an item from one path in the file system to another.
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/reclaimitem(_:replyhandler:).md)
  Reclaims an item, releasing any resources allocated for the item.
### Working with links
- [func createLink(to: FSItem, named: FSFileName, inDirectory: FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](fsvolume/operations/createlink(to:named:indirectory:replyhandler:).md)
  Creates a new hard link.
- [func createSymbolicLink(named: FSFileName, inDirectory: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, replyHandler: (FSItem?, FSFileName?, (any Error)?) -> Void)](fsvolume/operations/createsymboliclink(named:indirectory:attributes:linkcontents:replyhandler:).md)
  Creates a new symbolic link.
- [func readSymbolicLink(FSItem, replyHandler: (FSFileName?, (any Error)?) -> Void)](fsvolume/operations/readsymboliclink(_:replyhandler:).md)
  Reads a symbolic link.
### Working with attributes
- [func getAttributes(FSItem.GetAttributesRequest, of: FSItem, replyHandler: (FSItem.Attributes?, (any Error)?) -> Void)](fsvolume/operations/getattributes(_:of:replyhandler:).md)
  Fetches attributes for the given item.
- [FSItem.GetAttributesRequest](fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [func setAttributes(FSItem.SetAttributesRequest, on: FSItem, replyHandler: (FSItem.Attributes?, (any Error)?) -> Void)](fsvolume/operations/setattributes(_:on:replyhandler:).md)
  Sets the given attributes on an item.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
### Inspecting directory contents
- [func enumerateDirectory(FSItem, startingAt: FSDirectoryCookie, verifier: FSDirectoryVerifier, attributes: FSItem.GetAttributesRequest?, packer: FSDirectoryEntryPacker, replyHandler: (FSDirectoryVerifier, (any Error)?) -> Void)](fsvolume/operations/enumeratedirectory(_:startingat:verifier:attributes:packer:replyhandler:).md)
  Enumerates the contents of the given directory.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryVerifier](fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [struct FSDirectoryVerifier](fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [class FSDirectoryEntryPacker](fsdirectoryentrypacker.md)
  An object used to provide items during a directory enumeration.
### Synchronizing with a resource
- [func synchronize(flags: FSSyncFlags, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/synchronize(flags:replyhandler:).md)
  Synchronizes the volume with its underlying resource.
- [enum FSSyncFlags](fssyncflags.md)
  Behavior flags for use with synchronization calls.
### Inspecting volume properties
- [var supportedVolumeCapabilities: FSVolume.SupportedCapabilities](fsvolume/operations/supportedvolumecapabilities.md)
  A property that provides the supported capabilities of the volume.
- [FSVolume.SupportedCapabilities](fsvolume/supportedcapabilities.md)
  A type that represents capabillities supported by a volume, such as hard and symbolic links, journaling, and large file sizes.
- [var volumeStatistics: FSStatFSResult](fsvolume/operations/volumestatistics.md)
  A property that provides up-to-date statistics of the volume.
- [class FSStatFSResult](fsstatfsresult.md)
  A type used to report a volume’s statistics.

## Relationships

### Inherits From
- [FSVolume.PathConfOperations](fsvolume/pathconfoperations.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [FSVolume.PathConfOperations](fsvolume/pathconfoperations.md)
  Properties implemented by volumes that support providing the values of system limits or options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations)*