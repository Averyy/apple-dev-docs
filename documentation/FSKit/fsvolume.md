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

You implement a volume for your file system type by subclassing this class, and also conforming to the [`FSVolume.Operations`](fsvolume/operations.md) and [`FSVolume.PathConfOperations`](fsvolume/pathconfoperations.md) protocols. This protocol defines the minimum set of operations supported by a volume, such as mounting, activating, creating and removing items, and more.

Your volume can provide additional functionality by conforming to other volume operations protocols. These protocols add support for operations like open and close, read and write, extended attribute (Xattr) manipulation, and more.

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
### Implementing required operations
- [FSVolume.Operations](fsvolume/operations.md)
  Methods that all volumes implement to provide required capabilities.
- [FSVolume.PathConfOperations](fsvolume/pathconfoperations.md)
  Properties implemented by volumes that support providing the values of system limits or options.
### Implementing optional operations
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
- [FSVolume.ItemDeactivation](fsvolume/itemdeactivation.md)
  Methods and properties implemented by volumes that support deactivating items.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume)*