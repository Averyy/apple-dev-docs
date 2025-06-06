# acl

**Framework**: Endpoint Security  
**Kind**: property

A union containing a settable access control list structure.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var acl: es_event_setacl_t.__Unnamed_union_acl
```

#### Discussion

The `acl` union is valid only when the [`set_or_clear`](es_event_setacl_t/set_or_clear.md) value is [`ES_SET`](es_set.md). In this case, the union contains an `acl_t` called `set` containing the access control list values.

## See Also

- [var target: UnsafeMutablePointer<es_file_t>](es_event_setacl_t/target.md)
  The file containing the access control list to set or clear.
- [var set_or_clear: es_set_or_clear_t](es_event_setacl_t/set_or_clear.md)
  The access control list action represented by the event, either setting or clearing values.
- [struct es_set_or_clear_t](es_set_or_clear_t.md)
  A type that indicates whether an event represents setting or clearing a file’s access control list.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_setacl_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_setacl_t/acl)*