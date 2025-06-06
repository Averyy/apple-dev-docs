# es_event_copyfile_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the copying of a file by use of a system call.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_copyfile_t
```

#### Overview

Be aware that the `copyfile` system call isn’t the same thing as the `copyfile(3)` function in the standard library. Its semantics depend on the specific filesystem in use.

## Topics

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](es_event_copyfile_t/source.md)
  The file to clone.
- [var target_file: UnsafeMutablePointer<es_file_t>?](es_event_copyfile_t/target_file.md)
  The file, if any, that exists at the target location.
- [var target_dir: UnsafeMutablePointer<es_file_t>](es_event_copyfile_t/target_dir.md)
  The directory that contains the copied file.
- [var target_name: es_string_token_t](es_event_copyfile_t/target_name.md)
  The name of the newly copied file.
- [var mode: mode_t](es_event_copyfile_t/mode.md)
  The mode argument of the system call.
- [var flags: Int32](es_event_copyfile_t/flags.md)
  The flags argument of the system call.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_copyfile_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(source: UnsafeMutablePointer<es_file_t>, target_file: UnsafeMutablePointer<es_file_t>?, target_dir: UnsafeMutablePointer<es_file_t>, target_name: es_string_token_t, mode: mode_t, flags: Int32, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_copyfile_t/init(source:target_file:target_dir:target_name:mode:flags:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_file_t](es_file_t.md)
  A type that represents a file related to an Endpoint Security event.
- [struct es_event_access_t](es_event_access_t.md)
  A type for an event that indicates the checking of a file’s access permission.
- [struct es_event_clone_t](es_event_clone_t.md)
  A type for an event that indicates the cloning of a file.
- [struct es_event_create_t](es_event_create_t.md)
  A type for an event that indicates the creation of a file.
- [struct es_event_dup_t](es_event_dup_t.md)
  A type for an event that indicates the duplication of a file descriptor.
- [struct es_event_fcntl_t](es_event_fcntl_t.md)
  A type for an event that indicates the manipulation of a file descriptor.
- [struct es_event_open_t](es_event_open_t.md)
  A type for an event that indicates the opening of a file.
- [struct es_event_close_t](es_event_close_t.md)
  A type for an event that indicates the closing of a file.
- [struct es_event_rename_t](es_event_rename_t.md)
  A type for an event that indicates the renaming of a file.
- [struct es_event_truncate_t](es_event_truncate_t.md)
  A type for an event that indicates the truncation of a file.
- [struct es_event_exchangedata_t](es_event_exchangedata_t.md)
  A type for an event that indicates the exchange of data between two files.
- [struct es_event_write_t](es_event_write_t.md)
  A type for an event that indicates the writing of data to a file.
- [struct es_event_lookup_t](es_event_lookup_t.md)
  A type for an event that indicates the lookup of a file’s path.
- [struct es_event_searchfs_t](es_event_searchfs_t.md)
  A type for an event that indicates searching a volume or mounted file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_copyfile_t)*