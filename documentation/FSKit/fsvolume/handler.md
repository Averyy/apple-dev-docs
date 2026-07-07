# FSVolume.Handler

**Framework**: FSKit  
**Kind**: protocol

Methods that all volumes implement to provide required capabilities.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol Handler : FSVolume.PathConfOperations
```

#### Overview

Conform to this protocol in your subclass of [`FSVolume`](fsvolume.md). To provide additional capabilities, conform to the other `FSVolume` handler protocols, such as [`FSVolume.OpenCloseHandler`](fsvolume/openclosehandler.md) and [`FSVolume.ReadWriteHandler`](fsvolume/readwritehandler.md).

> **Note**: This protocol extends [`FSVolume.PathConfOperations`](fsvolume/pathconfoperations.md), so your volume implementation must also conform to that protocol.

> ❗ **Important**: This protocol replaces the [`FSVolume.Operations`](fsvolume/operations.md) protocol. It exposes the same functionality, while using [`FSVolumeHandlerResult`](fsvolumehandlerresult.md) objects. These objects add the ability to reply with [`FSItem.Attributes`](fsitem/attributes.md) and free space from the relevant methods.

## Topics

### Handling activation and deactivation
- [func activate(options: FSTaskOptions, replyHandler: (FSActivateResult?, (any Error)?) -> Void)](fsvolume/handler/activate(options:replyhandler:).md)
  Activates the volume using the specified options.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSActivateResult](fsactivateresult.md)
  The result of an activate call.
- [func deactivate(options: FSDeactivateOptions, replyHandler: ((any Error)?) -> Void)](fsvolume/handler/deactivate(options:replyhandler:).md)
  Tears down a previously initialized volume instance.
- [struct FSDeactivateOptions](fsdeactivateoptions.md)
  Options that affect the behavior of deactivate methods.
### Mounting and unmounting
- [func mount(options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](fsvolume/handler/mount(options:replyhandler:).md)
  Mounts this volume, using the specified options.
- [func unmount(replyHandler: () -> Void)](fsvolume/handler/unmount(replyhandler:).md)
  Unmounts this volume.
### Working with items
- [func createItem(named: FSFileName, type: FSItem.ItemType, in: FSItem, attributes: FSItem.SetAttributesRequest, context: FSContext, replyHandler: (FSCreateItemResult?, (any Error)?) -> Void)](fsvolume/handler/createitem(named:type:in:attributes:context:replyhandler:).md)
  Creates a new file or directory item.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.ItemType](fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSCreateItemResult](fscreateitemresult.md)
  The result of a create-item call.
- [func lookupItem(named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSLookupItemResult?, (any Error)?) -> Void)](fsvolume/handler/lookupitem(named:in:context:replyhandler:).md)
  Looks up an item within a directory.
- [class FSLookupItemResult](fslookupitemresult.md)
  The result of an item lookup call.
- [func removeItem(FSItem, named: FSFileName, from: FSItem, context: FSContext, replyHandler: (FSRemoveItemResult?, (any Error)?) -> Void)](fsvolume/handler/removeitem(_:named:from:context:replyhandler:).md)
  Removes an existing item from a given directory.
- [class FSRemoveItemResult](fsremoveitemresult.md)
  The result of a remove-item call.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, context: FSContext, replyHandler: (FSRenameItemResult?, (any Error)?) -> Void)](fsvolume/handler/renameitem(_:indirectory:named:to:indirectory:overitem:context:replyhandler:).md)
  Renames an item from one path in the file system to another.
- [class FSRenameItemResult](fsrenameitemresult.md)
  The result of a rename-item call.
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](fsvolume/handler/reclaimitem(_:replyhandler:).md)
  Reclaims an item, releasing any resources allocated for the item.
### Working with links
- [func createLink(to: FSItem, named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSCreateLinkResult?, (any Error)?) -> Void)](fsvolume/handler/createlink(to:named:in:context:replyhandler:).md)
  Creates a new hard link.
- [class FSCreateLinkResult](fscreatelinkresult.md)
  The result of a create-link call.
- [func createSymbolicLink(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, context: FSContext, replyHandler: (FSCreateSymlinkResult?, (any Error)?) -> Void)](fsvolume/handler/createsymboliclink(named:in:attributes:linkcontents:context:replyhandler:).md)
  Creates a new symbolic link.
- [class FSCreateSymlinkResult](fscreatesymlinkresult.md)
  The result of a create-symlink call.
- [func readSymbolicLink(FSItem, context: FSContext, replyHandler: (FSReadSymlinkResult?, (any Error)?) -> Void)](fsvolume/handler/readsymboliclink(_:context:replyhandler:).md)
  Reads a symbolic link.
- [class FSReadSymlinkResult](fsreadsymlinkresult.md)
  The result of a read-symlink call.
### Working with attributes
- [func getAttributes(FSItem.GetAttributesRequest, of: FSItem, context: FSContext, replyHandler: (FSGetAttributesResult?, (any Error)?) -> Void)](fsvolume/handler/getattributes(_:of:context:replyhandler:).md)
  Fetches attributes for the given item.
- [FSItem.GetAttributesRequest](fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [class FSGetAttributesResult](fsgetattributesresult.md)
  The result of a get-attributes call.
- [func setAttributes(FSItem.SetAttributesRequest, on: FSItem, context: FSContext, replyHandler: (FSSetAttributesResult?, (any Error)?) -> Void)](fsvolume/handler/setattributes(_:on:context:replyhandler:).md)
  Sets the given attributes on an item.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSSetAttributesResult](fssetattributesresult.md)
  The restlt of a set-attributes call.
### Inspecting directory contents
- [func enumerateDirectory(FSItem, startingAt: FSDirectoryCookie, verifier: FSDirectoryVerifier, attributes: FSItem.GetAttributesRequest?, packer: FSDirectoryEntryPacker, context: FSContext, replyHandler: (FSEnumerateDirectoryResult?, (any Error)?) -> Void)](fsvolume/handler/enumeratedirectory(_:startingat:verifier:attributes:packer:context:replyhandler:).md)
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
- [class FSEnumerateDirectoryResult](fsenumeratedirectoryresult.md)
  The result of an enumerate-directory call.
### Performing synchronization
- [func synchronize(flags: FSSyncFlags, replyHandler: ((any Error)?) -> Void)](fsvolume/handler/synchronize(flags:replyhandler:).md)
  Synchronizes the volume with its underlying resource.
- [enum FSSyncFlags](fssyncflags.md)
  Behavior flags for use with synchronization calls.
### Inspecting required volume properties
- [var supportedVolumeCapabilities: FSVolume.SupportedCapabilities](fsvolume/handler/supportedvolumecapabilities.md)
- [FSVolume.SupportedCapabilities](fsvolume/supportedcapabilities.md)
  A type that represents capabilities supported by a volume, such as hard and symbolic links, journaling, and large file sizes.
- [var volumeStatistics: FSStatFSResult](fsvolume/handler/volumestatistics.md)
  A property that provides up-to-date statistics of the volume.
- [class FSStatFSResult](fsstatfsresult.md)
  A type used to report a volume’s statistics.
### Inspecting optional volume properties
- [var requestedMountOptions: FSVolume.MountOptions](fsvolume/handler/requestedmountoptions.md)
  A property that allows the file system to request for specific mount options from FSKit.
- [FSVolume.MountOptions](fsvolume/mountoptions.md)
  Mount options to be requested from FSKit using the `requestedMountOptions` property.
- [var enableOpenUnlinkEmulation: Bool](fsvolume/handler/enableopenunlinkemulation.md)
  A property that allows the file system to use open-unlink emulation.
### Supporting types
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.

## Relationships

### Inherits From
- [FSVolume.PathConfOperations](fsvolume/pathconfoperations.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class FSVolumeHandlerResult](fsvolumehandlerresult.md)
  An abstract base class for all result objects in FSKit handler-style protocols.
- [FSVolume.PathConfOperations](fsvolume/pathconfoperations.md)
  Properties implemented by volumes that support providing the values of system limits or options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler)*