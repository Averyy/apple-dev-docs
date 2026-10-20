# statfs

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The statistics of the remounted file system.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var statfs: UnsafeMutablePointer<statfs>
```

```c
struct statfs * statfs;
```

## See Also

### Inspecting Event Properties
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_remount_t/statfs)*