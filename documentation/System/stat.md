# Stat

**Framework**: System  
**Kind**: struct  
**Role**: Structure

A Swift wrapper of the C `stat` struct.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@frozen
struct Stat
```

#### Overview

> **Note**: Only available on Unix-like platforms.

## Topics

### Structures
- [struct Flags](./stat/flags-swift.struct.md)
  Flags representing those passed to `fstatat()`.
### Initializers
- [init(FilePath, flags: Stat.Flags, retryOnInterrupt: Bool) throws(Errno)](./stat/init%28_,flags,retryoninterrupt%29-349q0.md)
  Creates a `Stat` struct from a `FilePath` and `Flags`.
- [init(UnsafePointer<CChar>, flags: Stat.Flags, retryOnInterrupt: Bool) throws(Errno)](./stat/init%28_,flags,retryoninterrupt%29-9o008.md)
  Creates a `Stat` struct from an `UnsafePointer<CChar>` path and `Flags`.
- [init(UnsafePointer<CChar>, followTargetSymlink: Bool, retryOnInterrupt: Bool) throws(Errno)](./stat/init%28_,followtargetsymlink,retryoninterrupt%29-2szq8.md)
  Creates a `Stat` struct from an `UnsafePointer<CChar>` path.
- [init(FilePath, followTargetSymlink: Bool, retryOnInterrupt: Bool) throws(Errno)](./stat/init%28_,followtargetsymlink,retryoninterrupt%29-4apli.md)
  Creates a `Stat` struct from a `FilePath`.
- [init(UnsafePointer<CChar>, relativeTo: FileDescriptor, flags: Stat.Flags, retryOnInterrupt: Bool) throws(Errno)](./stat/init%28_,relativeto,flags,retryoninterrupt%29-5rm1x.md)
  Creates a `Stat` struct from an `UnsafePointer<CChar>` path and `Flags`, including a `FileDescriptor` to resolve a relative path.
- [init(FilePath, relativeTo: FileDescriptor, flags: Stat.Flags, retryOnInterrupt: Bool) throws(Errno)](./stat/init%28_,relativeto,flags,retryoninterrupt%29-q6e4.md)
  Creates a `Stat` struct from a `FilePath` and `Flags`, including a `FileDescriptor` to resolve a relative path.
- [init(FileDescriptor, retryOnInterrupt: Bool) throws(Errno)](./stat/init%28_,retryoninterrupt%29.md)
  Creates a `Stat` struct from a `FileDescriptor`.
- [init(rawValue: CInterop.Stat)](./stat/init%28rawvalue%29.md)
  Creates a Swift `Stat` from the raw C struct.
### Instance Properties
- [var blocksAllocated: Int64](./stat/blocksallocated.md)
  Number of 512-byte blocks allocated
- [var deviceID: DeviceID](./stat/deviceid.md)
  ID of device containing file
- [var flags: FileFlags](./stat/flags-swift.property.md)
  File flags
- [var generationNumber: UInt64](./stat/generationnumber.md)
  File generation number
- [var groupID: GroupID](./stat/groupid.md)
  Group ID of owner
- [var inode: Inode](./stat/inode.md)
  Inode number
- [var linkCount: Int](./stat/linkcount.md)
  Number of hard links
- [var mode: FileMode](./stat/mode.md)
  File mode
- [var permissions: FilePermissions](./stat/permissions.md)
  File permissions for the given mode
- [var preferredIOBlockSize: Int](./stat/preferredioblocksize.md)
  Block size for file system I/O, in bytes
- [var rawValue: CInterop.Stat](./stat/rawvalue.md)
  The raw C `stat` struct.
- [var size: Int64](./stat/size.md)
  Total size, in bytes
- [var sizeAllocated: Int64](./stat/sizeallocated.md)
  Total size allocated, in bytes
- [var specialDeviceID: DeviceID](./stat/specialdeviceid.md)
  Device ID (if special file)
- [var st_atim: timespec](./stat/st_atim.md)
  Time of last access, given as a C `timespec` since the Epoch.
- [var st_birthtim: timespec](./stat/st_birthtim.md)
  Time of file creation, given as a C `timespec` since the Epoch.
- [var st_ctim: timespec](./stat/st_ctim.md)
  Time of last status (inode) change, given as a C `timespec` since the Epoch.
- [var st_mtim: timespec](./stat/st_mtim.md)
  Time of last modification, given as a C `timespec` since the Epoch.
- [var type: FileType](./stat/type.md)
  File type for the given mode
- [var userID: UserID](./stat/userid.md)
  User ID of owner
### Default Implementations
- [Equatable Implementations](./stat/equatable-implementations.md)
- [Hashable Implementations](./stat/hashable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat)*