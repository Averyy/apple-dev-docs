# target_name

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The name of the newly cloned file.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var target_name: es_string_token_t
```

```c
es_string_token_t target_name;
```

## See Also

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](./source.md)
  The file to clone.
- [var target_dir: UnsafeMutablePointer<es_file_t>](./target_dir.md)
  The directory that contains the cloned file.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_clone_t/target_name)*