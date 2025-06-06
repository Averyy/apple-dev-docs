# es_event_rename_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the renaming of a file.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_rename_t
```

## Topics

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](es_event_rename_t/source.md)
  The source file to rename.
- [var destination: es_event_rename_t.__Unnamed_union_destination](es_event_rename_t/destination.md)
  The destination of the rename operation.
- [var destination_type: es_destination_type_t](es_event_rename_t/destination_type.md)
  A property that indicates whether the destination is a new path or an existing file.
- [struct es_destination_type_t](es_destination_type_t.md)
  A type that indicates how a file event presents its destination to the client.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_rename_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(source: UnsafeMutablePointer<es_file_t>, destination_type: es_destination_type_t, destination: es_event_rename_t.__Unnamed_union_destination, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_rename_t/init(source:destination_type:destination:reserved:).md)

## See Also

- [struct es_file_t](es_file_t.md)
  A type that represents a file related to an Endpoint Security event.
- [struct es_event_access_t](es_event_access_t.md)
  A type for an event that indicates the checking of a file’s access permission.
- [struct es_event_clone_t](es_event_clone_t.md)
  A type for an event that indicates the cloning of a file.
- [struct es_event_copyfile_t](es_event_copyfile_t.md)
  A type for an event that indicates the copying of a file by use of a system call.
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

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_rename_t)*