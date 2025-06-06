# FSKit

**Framework**: Fskit  
**Kind**: module

Implement a file system that runs in user space.

**Availability**:
- macOS 15.4+

#### Overview

With FSKit, you can extend macOS by enabling access to new types of file systems. You do this by developing an FSKit module (`FSModule`), which you deliver as an app extension that runs in user space, and is compatible with Mac App Store distribution. FSKit connects your module to the system’s existing frameworks and tools, like [`Disk Arbitration`](https://developer.apple.com/documentation/DiskArbitration), NetFS, and the `mount(8)` command.

##### Fskit Modules

An FSKit module consists of two main parts:

- A set of  that you define in the module’s `Info.plist` file. These attributes provide metadata like Boolean keys that indicate feature support and dictionaries that describe command-line interface access.
- The code that implements the file system functionality. Your app extension conforms to one of two protocols, depending on its design flow, as described below.

The FSKit framework defines three key file storage concepts that `FSModule` supports:

##### Design Flows

FSKit provides two design flows, with different trade-offs of functionality and complexity:

- [`FSFileSystem`](fsfilesystem.md) is a conventional, full-featured file system that can employ multiple resources and deliver multiple volumes.
- [`FSUnaryFileSystem`](fsunaryfilesystem.md) is a simpler file system where containers use only one resource and provide only one volume. Most file systems shipping in macOS fit this pattern, including `HFS`, `msdosfs`, `ExFAT`, `ntfs`, and others.

> **Note**: The current version of FSKit supports only `FSUnaryFileSystem`.

When you choose a design flow, write an app extension that conforms to either `FileSystemExtension` or [`UnaryFileSystemExtension`](unaryfilesystemextension.md), based on your chosen flow. These protocols declare a `fileSystem` delegate object that your extension creates and returns. This delegate object subclasses either `FSFileSystem` or `FSUnaryFileSystem` as appropriate, and conforms to either the `FSFileSystemOperations` or [`FSUnaryFileSystemOperations`](fsunaryfilesystemoperations.md) protocol. These protocols define a `loadResource` method, which FSKit uses to make a resource available to the module.

## Topics

### App extensions
- [protocol UnaryFileSystemExtension](unaryfilesystemextension.md)
  A protocol for implementing a minimal file system as an app extension.
### File systems
- [class FSUnaryFileSystem](fsunaryfilesystem.md)
  An abstract base class for implementing a minimal file system.
- [protocol FSFileSystemBase](fsfilesystembase.md)
  A protocol containing functionality supplied by FSKit to file system implementations.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
### Containers
- [class FSContainerIdentifier](fscontaineridentifier.md)
  A type that identifies a container.
- [class FSContainerStatus](fscontainerstatus.md)
  A type that represents a container’s status.
### Resources
- [class FSResource](fsresource.md)
  An abstract resource a file system uses to provide data for a volume.
- [class FSBlockDeviceResource](fsblockdeviceresource.md)
  A resource that represents a block storage disk partition.
### Volumes
- [class FSVolume](fsvolume.md)
  A directory structure for files and folders.
### Items
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
### Maintenance and management
- [protocol FSManageableResourceMaintenanceOperations](fsmanageableresourcemaintenanceoperations.md)
  Maintenance operations for a file system’s resources.
### Operations
- [struct FSOperationID](fsoperationid.md)
  A unique identifier for an operation.
### Tasks
- [class FSTask](fstask.md)
  A class that enables a file system module to pass log messages and completion notifications to clients.
- [class FSTaskOptions](fstaskoptions.md)
  A class that passes command options to a task, optionally providing security-scoped URLs.
### Errors and logging
- [func fs_errorForCocoaError(Int32) -> any Error](fs_errorforcocoaerror(_:).md)
  Creates an error object for the given Cocoa error code.
- [func fs_errorForMachError(Int32) -> any Error](fs_errorformacherror(_:).md)
  Creates an error object for the given Mach error code.
- [func fs_errorForPOSIXError(Int32) -> any Error](fs_errorforposixerror(_:).md)
  Creates an error object for the given POSIX error code.
- [struct FSError](fserror.md)
  An error encountered when performing an FSKit operation.
- [FSError.Code](fserror/code.md)
  A code that indicates a specific FSKit error.
- [let FSKitErrorDomain: String](fskiterrordomain.md)
  An error domain for FSKit errors.
### FSKit interactions
- [class FSClient](fsclient.md)
  An interface for apps and daemons to interact with FSKit.
### Supporting types
- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSEntityIdentifier](fsentityidentifier.md)
  A base type that identifies containers and volumes.
- [class FSExtentPacker](fsextentpacker.md)
  A type that directs the kernel to map space on disk to a specific file managed by this file system.
- [enum FSExtentType](fsextenttype.md)
  An enumeration of types of extents.
- [enum FSMatchResult](fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.
- [class FSProbeResult](fsproberesult.md)
  An object that represents the results of a specific probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FSKit)*