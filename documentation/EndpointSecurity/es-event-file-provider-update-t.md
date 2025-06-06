# es_event_file_provider_update_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates an update to a file provider.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_file_provider_update_t
```

## Topics

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](es_event_file_provider_update_t/source.md)
  The source file of the event.
- [var target_path: es_string_token_t](es_event_file_provider_update_t/target_path.md)
  The target path to update.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_file_provider_update_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(source: UnsafeMutablePointer<es_file_t>, target_path: es_string_token_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_file_provider_update_t/init(source:target_path:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_file_provider_materialize_t](es_event_file_provider_materialize_t.md)
  A type for an event that indicates the materialization of a file provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_file_provider_update_t)*