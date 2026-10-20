# reserved2

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

An unused field reserved for future use.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var reserved2: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)
```

```c
uint8_t reserved2[16];
```

## See Also

### Inspecting Event Properties
- [var destination: es_event_create_t.__Unnamed_union_destination](./destination.md)
  The file system destination of the created file.
- [var destination_type: es_destination_type_t](./destination_type.md)
  The type of destination for the event, which can be either an existing file or information that describes a new file’s pending location.
- [struct es_destination_type_t](../es_destination_type_t.md)
  A type that indicates how a file event presents its destination to the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_create_t/reserved2)*