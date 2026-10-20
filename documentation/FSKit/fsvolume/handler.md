# FSVolume.Handler

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods that all volumes implement to provide required capabilities.

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol Handler : FSVolume.CommonOperations, FSVolume.PathConfOperations
```

```objc
@protocol FSVolumeHandler <NSObject, FSVolumeCommonOperations, FSVolumePathConfOperations>
```

#### Overview

Conform to this protocol in your subclass of [`FSVolume`](../fsvolume.md). To provide additional capabilities, conform to the other `FSVolume` handler protocols, such as [`FSVolume.OpenCloseHandler`](./openclosehandler.md) and [`FSVolume.ReadWriteHandler`](./readwritehandler.md).

> **Note**: This protocol extends [`FSVolume.PathConfOperations`](./pathconfoperations.md), so your volume implementation must also conform to that protocol.

> ❗ **Important**: This protocol replaces the [`FSVolume.Operations`](./operations.md) protocol. It exposes the same functionality, while using [`FSVolumeHandlerResult`](../fsvolumehandlerresult.md) objects. These objects add the ability to reply with [`FSItem.Attributes`](../fsitem/attributes.md) and free space from the relevant methods.

## Topics

### Handling activation and deactivation
- [class FSItem](../fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSActivateResult](../fsactivateresult.md)
  The result of an activate call.
- [struct FSDeactivateOptions](../fsdeactivateoptions.md)
  Options that affect the behavior of deactivate methods.
### Mounting and unmounting
- [func mount(options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](./handler/mount%28options,replyhandler%29.md)
- [func unmount(replyHandler: () -> Void)](./handler/unmount%28replyhandler%29.md)
### Working with items
- [func createItem(named: FSFileName, type: FSItem.ItemType, in: FSItem, attributes: FSItem.SetAttributesRequest, context: FSContext, replyHandler: (FSCreateItemResult?, (any Error)?) -> Void)](./handler/createitem%28named,type,in,attributes,context,replyhandler%29.md)
  Creates a new file or directory item.
- [class FSFileName](../fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.ItemType](../fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.SetAttributesRequest](../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSCreateItemResult](../fscreateitemresult.md)
  The result of a create-item call.
- [func lookupItem(named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSLookupItemResult?, (any Error)?) -> Void)](./handler/lookupitem%28named,in,context,replyhandler%29.md)
  Looks up an item within a directory.
- [class FSLookupItemResult](../fslookupitemresult.md)
  The result of an item lookup call.
- [func removeItem(FSItem, named: FSFileName, from: FSItem, context: FSContext, replyHandler: (FSRemoveItemResult?, (any Error)?) -> Void)](./handler/removeitem%28_,named,from,context,replyhandler%29.md)
  Removes an existing item from a given directory.
- [class FSRemoveItemResult](../fsremoveitemresult.md)
  The result of a remove-item call.
- [func renameItem(FSItem, inDirectory: FSItem, named: FSFileName, to: FSFileName, inDirectory: FSItem, overItem: FSItem?, context: FSContext, replyHandler: (FSRenameItemResult?, (any Error)?) -> Void)](./handler/renameitem%28_,indirectory,named,to,indirectory,overitem,context,replyhandler%29.md)
  Renames an item from one path in the file system to another.
- [class FSRenameItemResult](../fsrenameitemresult.md)
  The result of a rename-item call.
- [func reclaimItem(FSItem, replyHandler: ((any Error)?) -> Void)](./handler/reclaimitem%28_,replyhandler%29.md)
### Working with links
- [func createLink(to: FSItem, named: FSFileName, in: FSItem, context: FSContext, replyHandler: (FSCreateLinkResult?, (any Error)?) -> Void)](./handler/createlink%28to,named,in,context,replyhandler%29.md)
  Creates a new hard link.
- [class FSCreateLinkResult](../fscreatelinkresult.md)
  The result of a create-link call.
- [func createSymbolicLink(named: FSFileName, in: FSItem, attributes: FSItem.SetAttributesRequest, linkContents: FSFileName, context: FSContext, replyHandler: (FSCreateSymlinkResult?, (any Error)?) -> Void)](./handler/createsymboliclink%28named,in,attributes,linkcontents,context,replyhandler%29.md)
  Creates a new symbolic link.
- [class FSCreateSymlinkResult](../fscreatesymlinkresult.md)
  The result of a create-symlink call.
- [func readSymbolicLink(FSItem, context: FSContext, replyHandler: (FSReadSymlinkResult?, (any Error)?) -> Void)](./handler/readsymboliclink%28_,context,replyhandler%29.md)
  Reads a symbolic link.
- [class FSReadSymlinkResult](../fsreadsymlinkresult.md)
  The result of a read-symlink call.
### Working with attributes
- [func getAttributes(FSItem.GetAttributesRequest, of: FSItem, context: FSContext, replyHandler: (FSGetAttributesResult?, (any Error)?) -> Void)](./handler/getattributes%28_,of,context,replyhandler%29.md)
  Fetches attributes for the given item.
- [FSItem.GetAttributesRequest](../fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [class FSGetAttributesResult](../fsgetattributesresult.md)
  The result of a get-attributes call.
- [func setAttributes(FSItem.SetAttributesRequest, on: FSItem, context: FSContext, replyHandler: (FSSetAttributesResult?, (any Error)?) -> Void)](./handler/setattributes%28_,on,context,replyhandler%29.md)
  Sets the given attributes on an item.
- [FSItem.SetAttributesRequest](../fsitem/setattributesrequest.md)
  A request to set attributes on an item.
- [class FSSetAttributesResult](../fssetattributesresult.md)
  The restlt of a set-attributes call.
### Inspecting directory contents
- [func enumerateDirectory(FSItem, startingAt: FSDirectoryCookie, verifier: FSDirectoryVerifier, attributes: FSItem.GetAttributesRequest?, packer: FSDirectoryEntryPacker, context: FSContext, replyHandler: (FSEnumerateDirectoryResult?, (any Error)?) -> Void)](./handler/enumeratedirectory%28_,startingat,verifier,attributes,packer,context,replyhandler%29.md)
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
- [class FSEnumerateDirectoryResult](../fsenumeratedirectoryresult.md)
  The result of an enumerate-directory call.
### Performing synchronization
- [func synchronize(flags: FSSyncFlags, replyHandler: ((any Error)?) -> Void)](./handler/synchronize%28flags,replyhandler%29.md)
- [enum FSSyncFlags](../fssyncflags.md)
  Behavior flags for use with synchronization calls.
### Inspecting required volume properties
- [var supportedVolumeCapabilities: FSVolume.SupportedCapabilities](./handler/supportedvolumecapabilities.md)
- [FSVolume.SupportedCapabilities](./supportedcapabilities.md)
  A type that represents capabilities supported by a volume, such as hard and symbolic links, journaling, and large file sizes.
- [var volumeStatistics: FSStatFSResult](./handler/volumestatistics.md)
  A property that provides up-to-date statistics of the volume.
- [class FSStatFSResult](../fsstatfsresult.md)
  A type used to report a volume’s statistics.
### Inspecting optional volume properties
- [FSVolume.MountOptions](./mountoptions.md)
  Mount options to be requested from FSKit using the `requestedMountOptions` property.
### Supporting types
- [class FSContext](../fscontext.md)
  A context object that provides information about the initiator of a file system operation.
### Instance Methods
- [func activateVolume(options: FSTaskOptions, replyHandler: (FSActivateResult?, (any Error)?) -> Void)](./handler/activatevolume%28options,replyhandler%29.md)
  Activates the volume using the specified options.
- [func deactivateVolume(options: FSDeactivateOptions, replyHandler: ((any Error)?) -> Void)](./handler/deactivatevolume%28options,replyhandler%29.md)
  Tears down a previously initialized volume instance.

## Relationships

### Inherits From
- [FSVolume.CommonOperations](./commonoperations.md)
- [FSVolume.PathConfOperations](./pathconfoperations.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Implementing required handlers
- [class FSVolumeHandlerResult](../fsvolumehandlerresult.md)
  An abstract base class for all result objects in FSKit handler-style protocols.
- [FSVolume.PathConfOperations](./pathconfoperations.md)
  Properties implemented by volumes that support providing the values of system limits or options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler)*