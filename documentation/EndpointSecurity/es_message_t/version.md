# version

**Framework**: Endpoint Security  
**Kind**: property

The version of the Endpoint Security message.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var version: UInt32
```

#### Discussion

Clients wishing to be backward-compatible with future changes to Endpoint Security should inspect the version to ensure they don’t try to access fields that aren’t available.

## See Also

- [var action: es_message_t.__Unnamed_union_action](es_message_t/action.md)
  The action monitored by Endpoint Security.
- [var action_type: es_action_type_t](es_message_t/action_type.md)
  The type of action: authentication or notification.
- [struct es_action_type_t](es_action_type_t.md)
  The type of the message’s action.
- [struct es_event_id_t](es_event_id_t.md)
  An opaque identifier for events.
- [struct es_result_t](es_result_t.md)
  The result of the Endpoint Security subsystem authorization process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/version)*