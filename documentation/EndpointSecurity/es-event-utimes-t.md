# es_event_utimes_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates a change to a file’s access time or modification time.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_utimes_t
```

## Topics

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_file_t>](es_event_utimes_t/target.md)
  The file with time metadata to modify.
- [var atime: timespec](es_event_utimes_t/atime.md)
  The new last-accessed time.
- [var mtime: timespec](es_event_utimes_t/mtime.md)
  The new last-modified time.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_utimes_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(target: UnsafeMutablePointer<es_file_t>, atime: timespec, mtime: timespec, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_utimes_t/init(target:atime:mtime:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_deleteextattr_t](es_event_deleteextattr_t.md)
  A type for an event that indicates the deletion of an extended attribute from a file.
- [struct es_event_fsgetpath_t](es_event_fsgetpath_t.md)
  A type for an event that indicates the retrieval of a file-system path.
- [struct es_event_getattrlist_t](es_event_getattrlist_t.md)
  A type for an event that indicates the retrieval of attributes from a file.
- [struct es_event_getextattr_t](es_event_getextattr_t.md)
  A type for an event that indicates the retrieval of an extended attribute from a file.
- [struct es_event_listextattr_t](es_event_listextattr_t.md)
  A type for an event that indicates the retrieval of multiple extended attributes from a file.
- [struct es_event_readdir_t](es_event_readdir_t.md)
  A type for an event that indicates the reading of a file-system directory.
- [struct es_event_setacl_t](es_event_setacl_t.md)
  A type for an event that indicates the setting of a file’s access control list.
- [struct es_event_setattrlist_t](es_event_setattrlist_t.md)
  A type for an event that indicates the setting of a file attribute.
- [struct es_event_setextattr_t](es_event_setextattr_t.md)
  A type for an event that indicates the setting of a file’s extended attribute.
- [struct es_event_setflags_t](es_event_setflags_t.md)
  A type for an event that indicates the setting of a file’s flags.
- [struct es_event_setmode_t](es_event_setmode_t.md)
  A type for an event that indicates the setting of a file’s mode.
- [struct es_event_setowner_t](es_event_setowner_t.md)
  A type for an event that indicates the setting of a file’s owner.
- [struct es_event_stat_t](es_event_stat_t.md)
  A type for an event that indicates the retrieval of a file’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_utimes_t)*