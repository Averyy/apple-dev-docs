# source_dir

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The source directory to look up.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var source_dir: UnsafeMutablePointer<es_file_t>
```

```c
es_file_t * source_dir;
```

## See Also

### Inspecting Event Properties
- [var relative_target: es_string_token_t](./relative_target.md)
  The filename to look up.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_lookup_t/source_dir)*