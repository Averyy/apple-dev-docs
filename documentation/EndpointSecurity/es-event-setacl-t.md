# es_event_setacl_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the setting of a file’s access control list.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_setacl_t
```

## Topics

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_file_t>](es_event_setacl_t/target.md)
  The file containing the access control list to set or clear.
- [var acl: es_event_setacl_t.__Unnamed_union_acl](es_event_setacl_t/acl.md)
  A union containing a settable access control list structure.
- [var set_or_clear: es_set_or_clear_t](es_event_setacl_t/set_or_clear.md)
  The access control list action represented by the event, either setting or clearing values.
- [struct es_set_or_clear_t](es_set_or_clear_t.md)
  A type that indicates whether an event represents setting or clearing a file’s access control list.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_setacl_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(target: UnsafeMutablePointer<es_file_t>, set_or_clear: es_set_or_clear_t, acl: es_event_setacl_t.__Unnamed_union_acl, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_setacl_t/init(target:set_or_clear:acl:reserved:).md)

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
- [struct es_event_utimes_t](es_event_utimes_t.md)
  A type for an event that indicates a change to a file’s access time or modification time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_setacl_t)*