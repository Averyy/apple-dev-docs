# mprotect

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

Properties of an event that indicates a change to protection of memory-mapped pages.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var mprotect: es_event_mprotect_t { get set }
```

```c
es_event_mprotect_t mprotect;
```

## See Also

### Memory Mapping Events
- [var mmap: es_event_mmap_t](./mmap.md)
  Properties of an event that indicates the mapping of memory to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_events_t/mprotect)*