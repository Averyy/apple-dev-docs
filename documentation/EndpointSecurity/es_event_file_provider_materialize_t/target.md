# target

**Framework**: Endpoint Security  
**Kind**: property

The target fle.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var target: UnsafeMutablePointer<es_file_t>
```

## See Also

- [var instigator: UnsafeMutablePointer<es_process_t>?](es_event_file_provider_materialize_t/instigator.md)
  The process that instigated the event.
- [var instigator_token: audit_token_t](es_event_file_provider_materialize_t/instigator_token.md)
- [var source: UnsafeMutablePointer<es_file_t>](es_event_file_provider_materialize_t/source.md)
  The source file.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_file_provider_materialize_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_file_provider_materialize_t/target)*