# es_event_create_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the creation of a file.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_create_t
```

#### Overview

If the file doesn’t exist — either because it’s awaiting authorization or a client denied authorization —  this type contains the parent directory and file name of the proposed file. If the file does exist, as is the case with notifications of successful file creation, this type contains the full path of the created file. Use the [`destination_type`](es_event_create_t/destination_type.md) member to determine which case this event represents, and then access the [`destination`](es_event_create_t/destination.md) `union` accordingly.

## Topics

### Inspecting Event Properties
- [var destination: es_event_create_t.__Unnamed_union_destination](es_event_create_t/destination.md)
  The file system destination of the created file.
- [var destination_type: es_destination_type_t](es_event_create_t/destination_type.md)
  The type of destination for the event, which can be either an existing file or information that describes a new file’s pending location.
- [struct es_destination_type_t](es_destination_type_t.md)
  A type that indicates how a file event presents its destination to the client.
- [var reserved2: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_create_t/reserved2.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_create_t/init.md)
### Instance Properties
- [var acl: acl_t?](es_event_create_t/acl-6m1ze.md)
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_create_t/reserved-fmi7.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct es_file_t](es_file_t.md)
  A type that represents a file related to an Endpoint Security event.
- [struct es_event_access_t](es_event_access_t.md)
  A type for an event that indicates the checking of a file’s access permission.
- [struct es_event_clone_t](es_event_clone_t.md)
  A type for an event that indicates the cloning of a file.
- [struct es_event_copyfile_t](es_event_copyfile_t.md)
  A type for an event that indicates the copying of a file by use of a system call.
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

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_create_t)*