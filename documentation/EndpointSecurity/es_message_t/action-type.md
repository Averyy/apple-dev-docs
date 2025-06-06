# action_type

**Framework**: Endpoint Security  
**Kind**: property

The type of action: authentication or notification.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var action_type: es_action_type_t
```

#### Discussion

Use this value to determine how to access the [`action`](es_message_t/action.md) field, which is a `union` of different authentication and notification types.

## See Also

- [var action: es_message_t.__Unnamed_union_action](es_message_t/action.md)
  The action monitored by Endpoint Security.
- [struct es_action_type_t](es_action_type_t.md)
  The type of the message’s action.
- [struct es_event_id_t](es_event_id_t.md)
  An opaque identifier for events.
- [struct es_result_t](es_result_t.md)
  The result of the Endpoint Security subsystem authorization process.
- [var version: UInt32](es_message_t/version.md)
  The version of the Endpoint Security message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/action_type)*