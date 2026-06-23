# target_type

**Framework**: Endpoint Security  
**Kind**: property

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var target_type: es_bootstrap_target_type_t
```

#### Discussion

Discriminator for the `target` union of `es_event_bootstrap_look_up_t`. Selects between a running owner of the looked-up service port (PROCESS) and a lazy-launched or not-yet-running owner (JOB).


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_bootstrap_look_up_t/target_type)*