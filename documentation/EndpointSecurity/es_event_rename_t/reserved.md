# reserved

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

An unused field reserved for future use.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)
```

```c
uint8_t reserved[64];
```

## See Also

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](./source.md)
  The source file to rename.
- [var destination: es_event_rename_t.__Unnamed_union_destination](./destination.md)
  The destination of the rename operation.
- [var destination_type: es_destination_type_t](./destination_type.md)
  A property that indicates whether the destination is a new path or an existing file.
- [struct es_destination_type_t](../es_destination_type_t.md)
  A type that indicates how a file event presents its destination to the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_rename_t/reserved)*