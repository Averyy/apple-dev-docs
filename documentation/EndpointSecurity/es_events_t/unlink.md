# unlink

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

Properties of an event that indicates the deletion of a file.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var unlink: es_event_unlink_t { get set }
```

```c
es_event_unlink_t unlink;
```

## See Also

### Symbolic Link Events
- [var link: es_event_link_t](./link.md)
  Properties of an event that indicates the creation of a hard link.
- [var readlink: es_event_readlink_t](./readlink.md)
  Properties of an event that indicates the reading of a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_events_t/unlink)*