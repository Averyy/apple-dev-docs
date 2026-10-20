# audit_token

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The audit token associated with a muted process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var audit_token: audit_token_t
```

```c
audit_token_t audit_token;
```

## See Also

### Accessing Muted Processes
- [var events: UnsafePointer<es_event_type_t>!](./events.md)
  An array containing the muted event types.
- [struct es_event_type_t](../es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.
- [var event_count: Int](./event_count.md)
  The number of elements in the muted events array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_process_t/audit_token)*