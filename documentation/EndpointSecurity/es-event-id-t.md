# es_event_id_t

**Framework**: Endpoint Security  
**Kind**: struct

An opaque identifier for events.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_id_t
```

## Topics

### Reserved Fields
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_id_t/reserved.md)
  An opaque value.
### Initializers
- [init()](es_event_id_t/init.md)
- [init(reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_id_t/init(reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var action: es_message_t.__Unnamed_union_action](es_message_t/action.md)
  The action monitored by Endpoint Security.
- [var action_type: es_action_type_t](es_message_t/action_type.md)
  The type of action: authentication or notification.
- [struct es_action_type_t](es_action_type_t.md)
  The type of the message’s action.
- [struct es_result_t](es_result_t.md)
  The result of the Endpoint Security subsystem authorization process.
- [var version: UInt32](es_message_t/version.md)
  The version of the Endpoint Security message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_id_t)*