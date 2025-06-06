# es_event_file_provider_materialize_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the materialization of a file provider.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_file_provider_materialize_t
```

## Topics

### Inspecting Event Properties
- [var instigator: UnsafeMutablePointer<es_process_t>?](es_event_file_provider_materialize_t/instigator.md)
  The process that instigated the event.
- [var instigator_token: audit_token_t](es_event_file_provider_materialize_t/instigator_token.md)
- [var source: UnsafeMutablePointer<es_file_t>](es_event_file_provider_materialize_t/source.md)
  The source file.
- [var target: UnsafeMutablePointer<es_file_t>](es_event_file_provider_materialize_t/target.md)
  The target fle.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_file_provider_materialize_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(instigator: UnsafeMutablePointer<es_process_t>?, source: UnsafeMutablePointer<es_file_t>, target: UnsafeMutablePointer<es_file_t>, instigator_token: audit_token_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_file_provider_materialize_t/init(instigator:source:target:instigator_token:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_file_provider_update_t](es_event_file_provider_update_t.md)
  A type for an event that indicates an update to a file provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_file_provider_materialize_t)*