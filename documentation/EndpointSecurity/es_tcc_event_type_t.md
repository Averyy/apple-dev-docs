# es_tcc_event_type_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_tcc_event_type_t
```

```c
typedef enum { ... } es_tcc_event_type_t;
```

#### Overview

Represent the type of TCC modification event.

- ES_TCC_EVENT_TYPE_UNKNOWN: Unknown prior state.
- ES_TCC_EVENT_TYPE_CREATE: A new TCC authorization record was created.
- ES_TCC_EVENT_TYPE_MODIFY: An existing TCC authorization record was modified.
- ES_TCC_EVENT_TYPE_DELETE: An existing TCC authorization record was deleted.

## Topics

### Initializers
- [init(UInt32)](./es_tcc_event_type_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_tcc_event_type_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_tcc_event_type_t/rawvalue.md)
### Enumeration Cases
- [ES_TCC_EVENT_TYPE_CREATE](./es_tcc_event_type_create.md)
- [ES_TCC_EVENT_TYPE_DELETE](./es_tcc_event_type_delete.md)
- [ES_TCC_EVENT_TYPE_MODIFY](./es_tcc_event_type_modify.md)
- [ES_TCC_EVENT_TYPE_UNKNOWN](./es_tcc_event_type_unknown.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_tcc_event_type_t)*