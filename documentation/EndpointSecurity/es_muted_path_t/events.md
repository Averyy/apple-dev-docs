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

- [var type: es_mute_path_type_t](es_muted_path_t/type.md)
  The path type: prefix or literal.
- [struct es_mute_path_type_t](es_mute_path_type_t.md)
  The type of a path argument, such as a prefix or a path literal.
- [struct es_event_type_t](es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.
- [var event_count: Int](es_muted_path_t/event_count.md)
  The number of elements in the muted events array.
- [var path: es_string_token_t](es_muted_path_t/path.md)
  The muted path.
- [struct es_string_token_t](es_string_token_t.md)
  A pointer to a null-terminated string, and the length in bytes of that string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_path_t/events)*