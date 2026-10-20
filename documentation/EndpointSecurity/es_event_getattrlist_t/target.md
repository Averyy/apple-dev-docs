# target

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The file for which to retrieve attributes.

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
- [var attrlist: attrlist](./attrlist.md)
  The attributes to retrieve, such as volume, directory, file, and fork attributes.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_getattrlist_t/target)*