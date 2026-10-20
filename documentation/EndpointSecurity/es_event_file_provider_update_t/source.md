# source

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The source file of the event.

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
- [var target_path: es_string_token_t](./target_path.md)
  The target path to update.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_file_provider_update_t/source)*