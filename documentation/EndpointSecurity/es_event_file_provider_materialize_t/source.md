# source

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The source file.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var source: UnsafeMutablePointer<es_file_t>
```

```c
es_file_t * source;
```

## See Also

### Inspecting Event Properties
- [var instigator: UnsafeMutablePointer<es_process_t>?](./instigator.md)
  The process that instigated the event.
- [var instigator_token: audit_token_t](./instigator_token.md)
- [var target: UnsafeMutablePointer<es_file_t>](./target.md)
  The target fle.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_file_provider_materialize_t/source)*