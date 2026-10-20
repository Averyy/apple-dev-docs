# destination_type

**Framework**: Endpoint Security  
**Kind**: property

The type of destination for the event, which can be either an existing file or information that describes a new file’s pending location.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var destination_type: es_destination_type_t
```

#### Discussion

Use the value of this member to parse the [`destination`](es_event_create_t/destination.md) union.

## See Also

- [var destination: es_event_create_t.__Unnamed_union_destination](es_event_create_t/destination.md)
  The file system destination of the created file.
- [struct es_destination_type_t](es_destination_type_t.md)
  A type that indicates how a file event presents its destination to the client.
- [var reserved2: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_create_t/reserved2.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_create_t/destination_type)*