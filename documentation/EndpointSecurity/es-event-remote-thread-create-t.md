# es_event_remote_thread_create_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates an attempt by one process to create a thread in another process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_remote_thread_create_t
```

## Topics

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_process_t>](es_event_remote_thread_create_t/target.md)
  The process targeted to spawn a new thread.
- [var thread_state: UnsafeMutablePointer<es_thread_state_t>?](es_event_remote_thread_create_t/thread_state.md)
  The new thread’s state.
- [struct es_thread_state_t](es_thread_state_t.md)
  A description of a thread’s machine-specfiic state.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_remote_thread_create_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(target: UnsafeMutablePointer<es_process_t>, thread_state: UnsafeMutablePointer<es_thread_state_t>?, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_remote_thread_create_t/init(target:thread_state:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_proc_suspend_resume_t](es_event_proc_suspend_resume_t.md)
  A type for an event that indicates a call to suspend, resume, or shut down sockets for a process.
- [struct es_event_trace_t](es_event_trace_t.md)
  A type for an event that indicates an attempt by one process to attach to another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_remote_thread_create_t)*