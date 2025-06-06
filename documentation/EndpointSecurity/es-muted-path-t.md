# es_muted_path_t

**Framework**: Endpoint Security  
**Kind**: struct

A structure that describes a path’s muted events.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_muted_path_t
```

## Topics

### Accessing Muted Path Properties
- [var type: es_mute_path_type_t](es_muted_path_t/type.md)
  The path type: prefix or literal.
- [struct es_mute_path_type_t](es_mute_path_type_t.md)
  The type of a path argument, such as a prefix or a path literal.
- [var events: UnsafePointer<es_event_type_t>!](es_muted_path_t/events.md)
  An array containing the muted event types.
- [struct es_event_type_t](es_event_type_t.md)
  A type used to identify a message’s event type and subscribe to events of that type.
- [var event_count: Int](es_muted_path_t/event_count.md)
  The number of elements in the muted events array.
- [var path: es_string_token_t](es_muted_path_t/path.md)
  The muted path.
- [struct es_string_token_t](es_string_token_t.md)
  A pointer to a null-terminated string, and the length in bytes of that string.
### Initializers
- [init()](es_muted_path_t/init.md)
- [init(type: es_mute_path_type_t, event_count: Int, events: UnsafePointer<es_event_type_t>!, path: es_string_token_t)](es_muted_path_t/init(type:event_count:events:path:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [var paths: UnsafePointer<es_muted_path_t>!](es_muted_paths_t/paths.md)
  An array containing the muted paths.
- [var count: Int](es_muted_paths_t/count.md)
  The number of elements in the paths array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_path_t)*