# es_muted_process_t

**Framework**: Endpoint Security  
**Kind**: struct

A structure that describes a process’s muted events.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_muted_process_t
```

## Topics

### Accessing Muted Processes
- [var audit_token: audit_token_t](es_muted_process_t/audit_token.md)
  The audit token associated with a muted process.
- [var events: UnsafePointer<es_event_type_t>!](es_muted_process_t/events.md)
  An array containing the muted event types.
- [struct es_event_type_t](es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.
- [var event_count: Int](es_muted_process_t/event_count.md)
  The number of elements in the muted events array.
### Initializers
- [init()](es_muted_process_t/init.md)
- [init(audit_token: audit_token_t, event_count: Int, events: UnsafePointer<es_event_type_t>!)](es_muted_process_t/init(audit_token:event_count:events:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [var processes: UnsafePointer<es_muted_process_t>!](es_muted_processes_t/processes.md)
  An array containing the muted processes.
- [var count: Int](es_muted_processes_t/count.md)
  The number of elements in the processes array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_process_t)*