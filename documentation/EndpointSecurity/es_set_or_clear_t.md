# es_set_or_clear_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

A type that indicates whether an event represents setting or clearing a file’s access control list.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_set_or_clear_t
```

```c
typedef enum { ... } es_set_or_clear_t;
```

## Topics

### Event Types
- [var ES_CLEAR: es_set_or_clear_t](./es_clear.md)
  A case that indicates the event represents a clearing of the access control list.
- [var ES_SET: es_set_or_clear_t](./es_set.md)
  A case that indicates the event represents a setting of access control list values.
### Initializers
- [init(UInt32)](./es_set_or_clear_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_set_or_clear_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_set_or_clear_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_file_t>](./es_event_setacl_t/target.md)
  The file containing the access control list to set or clear.
- [var acl: es_event_setacl_t.__Unnamed_union_acl](./es_event_setacl_t/acl.md)
  A union containing a settable access control list structure.
- [var set_or_clear: es_set_or_clear_t](./es_event_setacl_t/set_or_clear.md)
  The access control list action represented by the event, either setting or clearing values.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./es_event_setacl_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_set_or_clear_t)*