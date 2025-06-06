# es_event_trace_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates an attempt by one process to attach to another process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_trace_t
```

#### Overview

Endpoint Security may generate this event multiple times for a single trace attempt. This can occur when then targeted process changes parents during the operation.

## Topics

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_process_t>](es_event_trace_t/target.md)
  The process receiving the attach.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_trace_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(target: UnsafeMutablePointer<es_process_t>, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_trace_t/init(target:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_proc_suspend_resume_t](es_event_proc_suspend_resume_t.md)
  A type for an event that indicates a call to suspend, resume, or shut down sockets for a process.
- [struct es_event_remote_thread_create_t](es_event_remote_thread_create_t.md)
  A type for an event that indicates an attempt by one process to create a thread in another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_trace_t)*