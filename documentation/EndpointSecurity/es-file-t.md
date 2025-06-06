# es_file_t

**Framework**: Endpoint Security  
**Kind**: struct

A type that represents a file related to an Endpoint Security event.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_file_t
```

## Topics

### Inspecting File Properties
- [var path: es_string_token_t](es_file_t/path.md)
  The file’s path.
- [var path_truncated: Bool](es_file_t/path_truncated.md)
  A Boolean value that indicates whether Endpoint Security truncated the path string.
- [var stat: stat](es_file_t/stat.md)
  The file’s metadata, such as file size, user and group identifiers, and access and modification dates.
### Initializers
- [init()](es_file_t/init.md)
- [init(path: es_string_token_t, path_truncated: Bool, stat: stat)](es_file_t/init(path:path_truncated:stat:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_file_t)*