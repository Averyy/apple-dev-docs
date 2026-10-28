# update_type

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var update_type: es_tcc_event_type_t
```

```c
es_tcc_event_type_t update_type;
```

## Discussion

Represent the type of TCC modification event.

- ES_TCC_EVENT_TYPE_UNKNOWN: Unknown prior state.
- ES_TCC_EVENT_TYPE_CREATE: A new TCC authorization record was created.
- ES_TCC_EVENT_TYPE_MODIFY: An existing TCC authorization record was modified.
- ES_TCC_EVENT_TYPE_DELETE: An existing TCC authorization record was deleted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_tcc_modify_t/update_type)*