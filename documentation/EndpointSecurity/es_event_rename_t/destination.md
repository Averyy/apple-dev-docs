# destination

**Framework**: Endpoint Security  
**Kind**: property

The destination of the rename operation.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var destination: es_event_rename_t.__Unnamed_union_destination
```

#### Discussion

To parse this `union`, check the [`destination_type`](es_event_rename_t/destination_type.md) to determine whether the rename event’s destination file already exists:

- If the [`destination_type`](es_event_rename_t/destination_type.md) is [`ES_DESTINATION_TYPE_EXISTING_FILE`](es_destination_type_existing_file.md), the union contains an [`es_file_t`](es_file_t.md) member called `existing_file`.
- If the [`destination_type`](es_event_rename_t/destination_type.md) is [`ES_DESTINATION_TYPE_NEW_PATH`](es_destination_type_new_path.md), the union contains a `struct` called `new_path`, indicating the file’s proposed destination. The structure consists of an [`es_file_t`](es_file_t.md) called `dir` for the parent directory, and an [`es_string_token_t`](es_string_token_t.md) called `filename`.

## See Also

- [var source: UnsafeMutablePointer<es_file_t>](es_event_rename_t/source.md)
  The source file to rename.
- [var destination_type: es_destination_type_t](es_event_rename_t/destination_type.md)
  A property that indicates whether the destination is a new path or an existing file.
- [struct es_destination_type_t](es_destination_type_t.md)
  A type that indicates how a file event presents its destination to the client.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_rename_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_rename_t/destination)*