# modified

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the file has modifications.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var modified: Bool
```

```c
bool modified;
```

#### Discussion

This value corresponds to `KAUTH_FILEOP_CLOSE_MODIFIED`.

## See Also

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_file_t>](./target.md)
  The file to close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_close_t/modified)*