# destination

**Framework**: Endpoint Security  
**Kind**: property

The file system destination of the created file.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var destination: es_event_create_t.__Unnamed_union_destination
```

#### Discussion

To parse this `union`, check the [`destination_type`](es_event_create_t/destination_type.md) to determine whether the file already exists:

- If the [`destination_type`](es_event_create_t/destination_type.md) is [`ES_DESTINATION_TYPE_EXISTING_FILE`](es_destination_type_existing_file.md), the union contains an [`es_file_t`](es_file_t.md) member called `existing_file`.
- If the [`destination_type`](es_event_create_t/destination_type.md) is [`ES_DESTINATION_TYPE_NEW_PATH`](es_destination_type_new_path.md), the union contains a `struct` called `new_path`, indicating the file’s proposed destination. The structure consists of an [`es_file_t`](es_file_t.md) called `dir` for the parent directory, an [`es_string_token_t`](es_string_token_t.md) called `filename`, and a [`mode_t`](https://developer.apple.com/documentation/kernel/mode_t) called `mode`.

## See Also

- [var destination_type: es_destination_type_t](es_event_create_t/destination_type.md)
  The type of destination for the event, which can be either an existing file or information that describes a new file’s pending location.
- [struct es_destination_type_t](es_destination_type_t.md)
  A type that indicates how a file event presents its destination to the client.
- [var reserved2: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_create_t/reserved2.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_create_t/destination)*