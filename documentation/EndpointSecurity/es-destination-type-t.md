# es_destination_type_t

**Framework**: Endpoint Security  
**Kind**: struct

A type that indicates how a file event presents its destination to the client.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_destination_type_t
```

#### Overview

Use this type to determine how to parse file information in types like [`es_event_create_t`](es_event_create_t.md) and [`es_event_rename_t`](es_event_rename_t.md). Both of those types have a `destination` member, which is a `union` of either an existing file path or a parent directory and name of a potential file. To determine which member of the union to access, consult the event’s `destination_type` member, which is of this type.

## Topics

### Destination Types
- [var ES_DESTINATION_TYPE_EXISTING_FILE: es_destination_type_t](es_destination_type_existing_file.md)
  The destination is an existing file.
- [var ES_DESTINATION_TYPE_NEW_PATH: es_destination_type_t](es_destination_type_new_path.md)
  The destination is a path to a new location.
### Initializers
- [init(UInt32)](es_destination_type_t/init(_:).md)
- [init(rawValue: UInt32)](es_destination_type_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_destination_type_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var destination: es_event_create_t.__Unnamed_union_destination](es_event_create_t/destination.md)
  The file system destination of the created file.
- [var destination_type: es_destination_type_t](es_event_create_t/destination_type.md)
  The type of destination for the event, which can be either an existing file or information that describes a new file’s pending location.
- [var reserved2: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_create_t/reserved2.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_destination_type_t)*