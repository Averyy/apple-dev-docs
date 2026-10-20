# target

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The file containing the access control list to set or clear.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var target: UnsafeMutablePointer<es_file_t>
```

```c
es_file_t * target;
```

## See Also

### Inspecting Event Properties
- [var acl: es_event_setacl_t.__Unnamed_union_acl](./acl.md)
  A union containing a settable access control list structure.
- [var set_or_clear: es_set_or_clear_t](./set_or_clear.md)
  The access control list action represented by the event, either setting or clearing values.
- [struct es_set_or_clear_t](../es_set_or_clear_t.md)
  A type that indicates whether an event represents setting or clearing a file’s access control list.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_setacl_t/target)*