# es_event_cs_invalidated_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the invalidation of a process’ code signing status.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_cs_invalidated_t
```

#### Overview

Endpoint Security generates this event as a result of removing the `CS_VALID` bit from a process’s CS flags. This occurs in the following situations:

- An invalid page for a process with an otherwise-valid code signature pages in.
- A call to `csops(CS_OPS_MARKINVALID)` explicitly invalidates the process.

Endpoint Security doesn’t generate this event if `CS_HARD` is set, since `CS_HARD` by design prevents the process from becoming invalid.

## Topics

### Inspecting Event Properties
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_cs_invalidated_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_cs_invalidated_t/init.md)
- [init(reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_cs_invalidated_t/init(reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_cs_invalidated_t)*