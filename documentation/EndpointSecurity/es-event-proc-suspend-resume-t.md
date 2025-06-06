# es_event_proc_suspend_resume_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates a call to suspend, resume, or shut down sockets for a process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_proc_suspend_resume_t
```

## Topics

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_process_t>?](es_event_proc_suspend_resume_t/target.md)
  The process targeted by this event.
- [var type: es_proc_suspend_resume_type_t](es_event_proc_suspend_resume_t/type.md)
  The type of event: suspend, resume, or socket shutdown.
- [struct es_proc_suspend_resume_type_t](es_proc_suspend_resume_type_t.md)
  The type of a process suspension or resumption event.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_proc_suspend_resume_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_proc_suspend_resume_t/init.md)
- [init(target: UnsafeMutablePointer<es_process_t>?, type: es_proc_suspend_resume_type_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_proc_suspend_resume_t/init(target:type:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_trace_t](es_event_trace_t.md)
  A type for an event that indicates an attempt by one process to attach to another process.
- [struct es_event_remote_thread_create_t](es_event_remote_thread_create_t.md)
  A type for an event that indicates an attempt by one process to create a thread in another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_proc_suspend_resume_t)*