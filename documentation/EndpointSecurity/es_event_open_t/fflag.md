# fflag

**Framework**: Endpoint Security  
**Kind**: property

The file-opening mask as applied by the kernel.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var fflag: Int32
```

#### Discussion

This mask differs from the `oflag` values used in `open(2)`. When responding to this event, use `FFLAG` values such as `FREAD` and `FWRITE` instead, rather than `O_RDONLY`, `O_RDWR` and the like.

## See Also

- [var file: UnsafeMutablePointer<es_file_t>](es_event_open_t/file.md)
  The file to open.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_open_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_open_t/fflag)*