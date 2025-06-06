# source

**Framework**: Endpoint Security  
**Kind**: property

The source file to rename.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var source: UnsafeMutablePointer<es_file_t>
```

## See Also

- [var destination: es_event_rename_t.__Unnamed_union_destination](es_event_rename_t/destination.md)
  The destination of the rename operation.
- [var destination_type: es_destination_type_t](es_event_rename_t/destination_type.md)
  A property that indicates whether the destination is a new path or an existing file.
- [struct es_destination_type_t](es_destination_type_t.md)
  A type that indicates how a file event presents its destination to the client.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_rename_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_rename_t/source)*