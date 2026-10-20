# iokit_open

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

Properties of an event that indicates the opening of an IOKit device.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var iokit_open: es_event_iokit_open_t { get set }
```

```c
es_event_iokit_open_t iokit_open;
```

## See Also

### Kernel Events
- [var kextload: es_event_kextload_t](./kextload.md)
  Properties of an event that indicates the loading of a Kernel Extension (KEXT).
- [var kextunload: es_event_kextunload_t](./kextunload.md)
  Properties of an event that indicates the unloading of a Kernel Extension (KEXT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_events_t/iokit_open)*