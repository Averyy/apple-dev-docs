# destination_type

**Framework**: Endpoint Security  
**Kind**: property

A property that indicates whether the destination is a new path or an existing file.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var destination_type: es_destination_type_t
```

#### Discussion

Use this property to determine how to access the [`destination`](es_event_rename_t/destination.md) field.

## See Also

- [var source: UnsafeMutablePointer<es_file_t>](es_event_rename_t/source.md)
  The source file to rename.
- [var destination: es_event_rename_t.__Unnamed_union_destination](es_event_rename_t/destination.md)
  The destination of the rename operation.
- [struct es_destination_type_t](es_destination_type_t.md)
  A type that indicates how a file event presents its destination to the client.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_rename_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_rename_t/destination_type)*