# target

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The file with ownership metadata to set.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var target: UnsafeMutablePointer<es_file_t>
```

```c
es_file_t * target;
```

## See Also

### Inspecting Event Properties
- [var uid: uid_t](./uid.md)
  The user identifier to set.
- [var gid: gid_t](./gid.md)
  The group identifier to set.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_setowner_t/target)*