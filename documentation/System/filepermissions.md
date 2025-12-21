# FilePermissions

**Framework**: System  
**Kind**: struct

The access permissions for a file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
struct FilePermissions
```

#### Overview

The following example creates an instance of the `FilePermissions` structure from a raw octal literal and compares it to a file permission created using named options:

```swift
let perms = FilePermissions(rawValue: 0o644)
perms == [.ownerReadWrite, .groupRead, .otherRead] // true
```

## Topics

### Owner Permissions
- [static var ownerRead: FilePermissions](filepermissions/ownerread.md)
  Indicates that the owner has read-only permission.
- [static var ownerWrite: FilePermissions](filepermissions/ownerwrite.md)
  Indicates that the owner has write-only permission.
- [static var ownerExecute: FilePermissions](filepermissions/ownerexecute.md)
  Indicates that the owner has execute-only permission.
- [static var ownerReadWrite: FilePermissions](filepermissions/ownerreadwrite.md)
  Indicates that the owner has read-write permission.
- [static var ownerReadExecute: FilePermissions](filepermissions/ownerreadexecute.md)
  Indicates that the owner has read-execute permission.
- [static var ownerWriteExecute: FilePermissions](filepermissions/ownerwriteexecute.md)
  Indicates that the owner has write-execute permission.
- [static var ownerReadWriteExecute: FilePermissions](filepermissions/ownerreadwriteexecute.md)
  Indicates that the owner has read, write, and execute permission.
### Group Permissions
- [static var groupRead: FilePermissions](filepermissions/groupread.md)
  Indicates that the group has read-only permission.
- [static var groupWrite: FilePermissions](filepermissions/groupwrite.md)
  Indicates that the group has write-only permission.
- [static var groupExecute: FilePermissions](filepermissions/groupexecute.md)
  Indicates that the group has execute-only permission.
- [static var groupReadWrite: FilePermissions](filepermissions/groupreadwrite.md)
  Indicates that the group has read-write permission.
- [static var groupReadExecute: FilePermissions](filepermissions/groupreadexecute.md)
  Indicates that the group has read-execute permission.
- [static var groupWriteExecute: FilePermissions](filepermissions/groupwriteexecute.md)
  Indicates that the group has write-execute permission.
- [static var groupReadWriteExecute: FilePermissions](filepermissions/groupreadwriteexecute.md)
  Indicates that the group has read, write, and execute permission.
### Other Permissions
- [static var otherRead: FilePermissions](filepermissions/otherread.md)
  Indicates that other users have read-only permission.
- [static var otherWrite: FilePermissions](filepermissions/otherwrite.md)
  Indicates that other users have write-only permission.
- [static var otherExecute: FilePermissions](filepermissions/otherexecute.md)
  Indicates that other users have execute-only permission.
- [static var otherReadWrite: FilePermissions](filepermissions/otherreadwrite.md)
  Indicates that other users have read-write permission.
- [static var otherReadExecute: FilePermissions](filepermissions/otherreadexecute.md)
  Indicates that other users have read-execute permission.
- [static var otherWriteExecute: FilePermissions](filepermissions/otherwriteexecute.md)
  Indicates that other users have write-execute permission.
- [static var otherReadWriteExecute: FilePermissions](filepermissions/otherreadwriteexecute.md)
  Indicates that other users have read, write, and execute permission.
### Special Permissions
- [static var setUserID: FilePermissions](filepermissions/setuserid.md)
  Indicates that the file is executed as the owner.
- [static var setGroupID: FilePermissions](filepermissions/setgroupid.md)
  Indicates that the file is executed as the group.
- [static var saveText: FilePermissions](filepermissions/savetext.md)
  Indicates that executable’s text segment should be kept in swap space even after it exits.
### Interacting with C APIs
- [init(rawValue: CModeT)](filepermissions/init(rawvalue:).md)
  Create a strongly-typed file permission from a raw C value.
- [let rawValue: CModeT](filepermissions/rawvalue.md)
  The raw C file permissions.
- [typealias CModeT](cmodet.md)
  The C `mode_t` type.
### Debugging
- [var description: String](filepermissions/description.md)
  A textual representation of the file permissions.
- [var debugDescription: String](filepermissions/debugdescription.md)
  A textual representation of the file permissions, suitable for debugging.
### Default Implementations
- [CustomDebugStringConvertible Implementations](filepermissions/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](filepermissions/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct FileDescriptor](filedescriptor.md)
  An abstract handle to an input or output data resource, such as a file or a socket.
- [struct FilePath](filepath.md)
  Represents a location in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepermissions)*