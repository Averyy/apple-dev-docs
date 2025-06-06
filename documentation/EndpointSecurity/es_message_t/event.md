# event

**Framework**: Endpoint Security  
**Kind**: property

The event that triggered this message.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var event: es_events_t
```

#### Discussion

Use the [`event_type`](es_message_t/event_type.md) property to determine which member of this [`es_events_t`](es_events_t.md) union is available. For example, if the type is [`ES_EVENT_TYPE_NOTIFY_FORK`](es_event_type_notify_fork.md), use the [`fork`](es_events_t/fork.md) member.

## See Also

- [struct es_events_t](es_events_t.md)
  A C union of event-specific types.
- [var event_type: es_event_type_t](es_message_t/event_type.md)
  The type of the message’s event.
- [struct es_event_type_t](es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/event)*