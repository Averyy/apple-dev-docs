# attrlist

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The attributes to retrieve, such as volume, directory, file, and fork attributes.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var attrlist: attrlist
```

```c
struct attrlist attrlist;
```

## See Also

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_file_t>](./target.md)
  The file for which to retrieve attributes.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.
- [attrlist](../../kernel/attrlist.md)
  A list of attributes associated with a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_getattrlist_t/attrlist)*