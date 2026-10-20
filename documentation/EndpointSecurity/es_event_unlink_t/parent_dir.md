# parent_dir

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The directory that contains the file to unlink.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var parent_dir: UnsafeMutablePointer<es_file_t>
```

```c
es_file_t * parent_dir;
```

## See Also

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_file_t>](./target.md)
  The file to unlink.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_unlink_t/parent_dir)*