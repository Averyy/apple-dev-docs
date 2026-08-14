# es_bootstrap_target_type_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_bootstrap_target_type_t
```

#### Overview

Discriminator for the `target` union of `es_event_bootstrap_look_up_t`. Selects between a running owner of the looked-up service port (PROCESS) and a lazy-launched or not-yet-running owner (JOB).

## Topics

### Initializers
- [init(UInt32)](es_bootstrap_target_type_t/init(_:).md)
- [init(rawValue: UInt32)](es_bootstrap_target_type_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_bootstrap_target_type_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_bootstrap_target_type_t)*