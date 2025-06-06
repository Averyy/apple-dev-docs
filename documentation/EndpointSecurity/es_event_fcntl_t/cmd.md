# cmd

**Framework**: Endpoint Security  
**Kind**: property

The file descriptor modification command.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var cmd: Int32
```

#### Discussion

This value corresponds to the `cmd` argument given to `fcntl(2)`.

## See Also

- [var target: UnsafeMutablePointer<es_file_t>](es_event_fcntl_t/target.md)
  The target file to modify.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_fcntl_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_fcntl_t/cmd)*