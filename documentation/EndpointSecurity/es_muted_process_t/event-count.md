# event_count

**Framework**: Endpoint Security  
**Kind**: property

The number of elements in the muted events array.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var event_count: Int
```

## See Also

- [var audit_token: audit_token_t](es_muted_process_t/audit_token.md)
  The audit token associated with a muted process.
- [var events: UnsafePointer<es_event_type_t>!](es_muted_process_t/events.md)
  An array containing the muted event types.
- [struct es_event_type_t](es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_process_t/event_count)*