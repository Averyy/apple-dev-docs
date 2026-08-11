# FSVolume

**Framework**: FSKit  
**Kind**: class

A directory structure for files and folders.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSVolume
```

#### Overview

A file system, depending on its type, provides one or more volumes to clients. The [`FSUnaryFileSystem`](fsunaryfilesystem.md) by definition provides only one volume, while an [`FSFileSystem`](fsfilesystem.md) supports multiple volumes.

You implement a volume for your file system type by subclassing this class, and also conforming to the [`FSVolume.Handler`](fsvolume/handler.md) and [`FSVolume.PathConfOperations`](fsvolume/pathconfoperations.md) protocols. This protocol defines the minimum set of operations supported by a volume, such as mounting, activating, creating and removing items, and more.

Your volume can provide additional functionality by conforming to other volume handler protocols. These protocols add support for operations like open and close, read and write, extended attribute (Xattr) manipulation, and more.

## Topics

### Creating a volume
- [init(volumeID: FSVolume.Identifier, volumeName: FSFileName)](fsvolume/init(volumeid:volumename:).md)
  Creates a volume with the given identifier and name.
- [FSVolume.Identifier](fsvolume/identifier.md)
  A type that identifies a volume.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
### Accessing volume properties
- [var volumeID: FSVolume.Identifier](fsvolume/volumeid.md)
  An identifier that uniquely identifies the volume.
- [var name: FSFileName](fsvolume/name.md)
  The name of the volume.
### Implementing required handlers
- [FSVolume.Handler](fsvolume/handler.md)
  Methods that all volumes implement to provide required capabilities.
- [class FSVolumeHandlerResult](fsvolumehandlerresult.md)
  An abstract base class for all result objects in FSKit handler-style protocols.
- [FSVolume.PathConfOperations](fsvolume/pathconfoperations.md)
  Properties implemented by volumes that support providing the values of system limits or options.
### Implementing optional handlers
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
- [FSVolume.ItemDeactivationHandler](fsvolume/itemdeactivationhandler.md)
  Methods and properties implemented by volumes that support deactivating items.
- [FSVolume.KernelOffloadedIOHandler](fsvolume/kerneloffloadediohandler.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.DataCacheHandler](fsvolume/datacachehandler.md)
  Methods and properties implemented by volumes that coordinate kernel-level data caching.
- [FSVolume.SeekRegionHandler](fsvolume/seekregionhandler.md)
  Methods and properties implemented by volumes that support seek operations
### Managing caching behavior
- [func setCacheState(for: FSItem, cacheMode: FSVolume.DataCacheMode, coherencyType: FSVolume.KernelCacheCoherencyType, action: FSVolume.KernelCacheCoherencyAction) -> (any Error)?](fsvolume/setcachestate(for:cachemode:coherencytype:action:).md)
  Sends a synchronous cache state update request from the module to the kernel.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [FSVolume.DataCacheMode](fsvolume/datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [FSVolume.KernelCacheCoherencyType](fsvolume/kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.
- [FSVolume.KernelCacheCoherencyAction](fsvolume/kernelcachecoherencyaction.md)
  A type that defines actions for cache state changes.
### Deprecated
- [FSVolume.Operations](fsvolume/operations.md)
  Methods that all volumes implement to provide required capabilities.
- [FSVolume.OpenCloseOperations](fsvolume/opencloseoperations.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteOperations](fsvolume/readwriteoperations.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckOperations](fsvolume/accesscheckoperations.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [FSVolume.RenameOperations](fsvolume/renameoperations.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.PreallocateOperations](fsvolume/preallocateoperations.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrOperations](fsvolume/xattroperations.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivation](fsvolume/itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.
- [protocol FSVolumeKernelOffloadedIOOperations](fsvolumekerneloffloadediooperations.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
### Protocols
- [FSVolume.CommonOperations](fsvolume/commonoperations.md)
  Methods common to `FSVolumeHandler` and `FSVolumeOperations`

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume)*