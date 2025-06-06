# action

**Framework**: Endpoint Security  
**Kind**: property

The action monitored by Endpoint Security.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var action: es_message_t.__Unnamed_union_action
```

#### Discussion

The action is a `union` of an [`es_event_id_t`](es_event_id_t.md) named `auth` and an [`es_result_t`](es_result_t.md) named `notify`. Use the [`action_type`](es_message_t/action_type.md) field to determine which kind of action this message represents.

## See Also

- [var action_type: es_action_type_t](es_message_t/action_type.md)
  The type of action: authentication or notification.
- [struct es_action_type_t](es_action_type_t.md)
  The type of the message’s action.
- [struct es_event_id_t](es_event_id_t.md)
  An opaque identifier for events.
- [struct es_result_t](es_result_t.md)
  The result of the Endpoint Security subsystem authorization process.
- [var version: UInt32](es_message_t/version.md)
  The version of the Endpoint Security message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/action)*