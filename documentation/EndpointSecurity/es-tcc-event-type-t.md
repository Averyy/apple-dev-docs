# es_tcc_event_type_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_tcc_event_type_t
```

#### Overview

Represent the type of TCC modification event.

- ES_TCC_EVENT_TYPE_UNKNOWN: Unknown prior state.
- ES_TCC_EVENT_TYPE_CREATE: A new TCC authorization record was created.
- ES_TCC_EVENT_TYPE_MODIFY: An existing TCC authorization record was modified.
- ES_TCC_EVENT_TYPE_DELETE: An existing TCC authorization record was deleted.

## Topics

### Initializers
- [init(UInt32)](es_tcc_event_type_t/init(_:).md)
- [init(rawValue: UInt32)](es_tcc_event_type_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_tcc_event_type_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_tcc_event_type_t)*