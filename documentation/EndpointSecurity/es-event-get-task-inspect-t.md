# es_event_get_task_inspect_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the retrieval of a task’s inspect port.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_get_task_inspect_t
```

#### Overview

This event represents a process that obtains a send right to a task inspect port, through `SYS_task_inspect_for_pid` or functions like `task_identity_token_get_task_port(_:_:_:)`.

> **Note**:  For more information on ports and port rights, see the “Ports, Port Rights, Port Sets, and Port Namespaces” section of [`Mach Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/Mach/Mach.html) in the [`Kernel Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/About/About.html).

## Topics

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_process_t>](es_event_get_task_inspect_t/target.md)
  The process targeted by this event.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_get_task_inspect_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(target: UnsafeMutablePointer<es_process_t>, type: es_get_task_type_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_get_task_inspect_t/init(target:type:reserved:).md)
### Instance Properties
- [var type: es_get_task_type_t](es_event_get_task_inspect_t/type.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_get_task_t](es_event_get_task_t.md)
  A type for an event that indicates the retrieval of a task’s control port.
- [struct es_event_get_task_read_t](es_event_get_task_read_t.md)
  A type for an event that indicates the retrieval of a task’s read port.
- [struct es_event_get_task_name_t](es_event_get_task_name_t.md)
  A type for an event that indicates the retrieval of a task’s name port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_get_task_inspect_t)*