# es_action_type_t

**Framework**: Endpoint Security  
**Kind**: struct

The type of the message’s action.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_action_type_t
```

## Topics

### Action Types
- [var ES_ACTION_TYPE_AUTH: es_action_type_t](es_action_type_auth.md)
  The authentication action type.
- [var ES_ACTION_TYPE_NOTIFY: es_action_type_t](es_action_type_notify.md)
  The notification action type.
### Initializers
- [init(UInt32)](es_action_type_t/init(_:).md)
- [init(rawValue: UInt32)](es_action_type_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_action_type_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var action: es_message_t.__Unnamed_union_action](es_message_t/action.md)
  The action monitored by Endpoint Security.
- [var action_type: es_action_type_t](es_message_t/action_type.md)
  The type of action: authentication or notification.
- [struct es_event_id_t](es_event_id_t.md)
  An opaque identifier for events.
- [struct es_result_t](es_result_t.md)
  The result of the Endpoint Security subsystem authorization process.
- [var version: UInt32](es_message_t/version.md)
  The version of the Endpoint Security message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_action_type_t)*