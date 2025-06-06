# event_type

**Framework**: Endpoint Security  
**Kind**: property

The type of the message’s event.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var event_type: es_event_type_t
```

#### Discussion

Use this value to determine how to access the [`event`](es_message_t/event.md) field, which is a union of all the possible event types.

## See Also

- [var event: es_events_t](es_message_t/event.md)
  The event that triggered this message.
- [struct es_events_t](es_events_t.md)
  A C union of event-specific types.
- [struct es_event_type_t](es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/event_type)*