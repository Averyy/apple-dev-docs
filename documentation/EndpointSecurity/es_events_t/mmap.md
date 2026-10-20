# mmap

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

Properties of an event that indicates the mapping of memory to a file.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var mmap: es_event_mmap_t { get set }
```

```c
es_event_mmap_t mmap;
```

## See Also

### Memory Mapping Events
- [var mprotect: es_event_mprotect_t](./mprotect.md)
  Properties of an event that indicates a change to protection of memory-mapped pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_events_t/mmap)*