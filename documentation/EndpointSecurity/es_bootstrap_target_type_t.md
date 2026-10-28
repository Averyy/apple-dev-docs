# es_bootstrap_target_type_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_bootstrap_target_type_t
```

```c
typedef enum { ... } es_bootstrap_target_type_t;
```

## Overview

Discriminator for the `target` union of `es_event_bootstrap_look_up_t`. Selects between a running owner of the looked-up service port (PROCESS) and a lazy-launched or not-yet-running owner (JOB).

## Topics

### Initializers
- [init(UInt32)](./es_bootstrap_target_type_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_bootstrap_target_type_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_bootstrap_target_type_t/rawvalue.md)
### Enumeration Cases
- [ES_BOOTSTRAP_TARGET_TYPE_JOB](./es_bootstrap_target_type_job.md)
- [ES_BOOTSTRAP_TARGET_TYPE_PROCESS](./es_bootstrap_target_type_process.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_bootstrap_target_type_t)*