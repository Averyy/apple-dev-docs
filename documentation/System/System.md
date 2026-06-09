# System

**Framework**: System  
**Kind**: module

Perform low-level file operations using type-safe APIs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Topics

### Adopting System
- [Adopting Swift File Operations](adopting-file-operations.md)
  Migrate existing C code to Swift, using the file operations provided by the System module.
- [Adopting Swift File Options](adopting-file-options.md)
  Migrate existing C code to Swift, using the file-operation options provided by the System module.
- [Adopting Swift Error Constants](adopting-errno.md)
  Migrate existing C code to Swift, using the error constants provided by the System module.
### Files
- [struct FileDescriptor](filedescriptor.md)
  An abstract handle to an input or output data resource, such as a file or a socket.
- [struct FilePath](filepath.md)
  Represents a location in the file system.
- [struct FilePermissions](filepermissions.md)
  The access permissions for a file.
### Errors
- [struct Errno](errno.md)
  An error number used by system calls to communicate what kind of error occurred.
### Protocols
- [protocol MachPortRight](machportright.md)
### Structures
- [struct DeviceID](deviceid.md)
  A Swift wrapper of the C `dev_t` type.
- [struct FileFlags](fileflags.md)
  File-specific flags found in the `st_flags` property of a `stat` struct or used as input to `chflags()`.
- [struct FileMode](filemode.md)
  A strongly-typed file mode representing a C `mode_t`.
- [struct FileType](filetype.md)
  A file type matching those contained in a C `mode_t`.
- [struct GroupID](groupid.md)
  A Swift wrapper of the C `gid_t` type.
- [struct Inode](inode.md)
  A Swift wrapper of the C `ino_t` type.
- [struct Stat](stat.md)
  A Swift wrapper of the C `stat` struct.
- [struct UserID](userid.md)
  A Swift wrapper of the C `uid_t` type.
### Enumerations
- [enum CInterop](cinterop.md)
  A namespace for C and platform types
- [enum Mach](mach.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/System)*