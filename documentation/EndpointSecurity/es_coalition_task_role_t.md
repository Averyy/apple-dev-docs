# es_coalition_task_role_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

es_coalition_task_role_t

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_coalition_task_role_t
```

```c
typedef enum { ... } es_coalition_task_role_t;
```

## Overview

The role a process’s task plays within its jetsam coalition. Mirrors the COALITION_TASKROLE_* values in mach/coalition.h.

## Topics

### Initializers
- [init(UInt32)](./es_coalition_task_role_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_coalition_task_role_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_coalition_task_role_t/rawvalue.md)
### Enumeration Cases
- [ES_COALITION_TASK_ROLE_EXT](./es_coalition_task_role_ext.md)
  The task is an extension within its jetsam coalition
- [ES_COALITION_TASK_ROLE_LEADER](./es_coalition_task_role_leader.md)
  The task is the leader (e.g. the application) of its jetsam coalition
- [ES_COALITION_TASK_ROLE_UNDEF](./es_coalition_task_role_undef.md)
  The task has no specific role within its jetsam coalition
- [ES_COALITION_TASK_ROLE_XPC](./es_coalition_task_role_xpc.md)
  The task is an XPC service within its jetsam coalition

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_coalition_task_role_t)*