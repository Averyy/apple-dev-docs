# es_event_readlink_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

A type for an event that indicates the reading of a symbolic link.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_event_readlink_t
```

```c
typedef struct { ... } es_event_readlink_t;
```

## Topics

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](./es_event_readlink_t/source.md)
  The source file pointed to by the link.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./es_event_readlink_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(source: UnsafeMutablePointer<es_file_t>, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](./es_event_readlink_t/init%28source,reserved%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Link Event Types
- [struct es_event_link_t](./es_event_link_t.md)
  A type for an event that indicates the creation of a hard link.
- [struct es_event_unlink_t](./es_event_unlink_t.md)
  A type for an event that indicates the deletion of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_readlink_t)*