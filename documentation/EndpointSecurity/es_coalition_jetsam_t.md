# es_coalition_jetsam_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_coalition_jetsam_t
```

```c
typedef struct { ... } es_coalition_jetsam_t;
```

## Overview

The jetsam-coalition membership of a process.

```
   the lifetime of the boot.
```

## Topics

### Initializers
- [init()](./es_coalition_jetsam_t/init%28%29.md)
- [init(id: UInt64, role: es_coalition_task_role_t)](./es_coalition_jetsam_t/init%28id,role%29.md)
### Instance Properties
- [var id: UInt64](./es_coalition_jetsam_t/id.md)
- [var role: es_coalition_task_role_t](./es_coalition_jetsam_t/role.md)
  es_coalition_task_role_t

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_coalition_jetsam_t)*