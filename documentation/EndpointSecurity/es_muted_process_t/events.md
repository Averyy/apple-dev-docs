# events

**Framework**: Endpoint Security  
**Kind**: property

An array containing the muted event types.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var events: UnsafePointer<es_event_type_t>!
```

## See Also

- [var audit_token: audit_token_t](es_muted_process_t/audit_token.md)
  The audit token associated with a muted process.
- [struct es_event_type_t](es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.
- [var event_count: Int](es_muted_process_t/event_count.md)
  The number of elements in the muted events array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_process_t/events)*