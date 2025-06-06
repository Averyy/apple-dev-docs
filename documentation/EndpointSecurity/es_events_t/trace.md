# trace

**Framework**: Endpoint Security  
**Kind**: property

Properties of an event that indicates an attempt by one process to attach to another.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var trace: es_event_trace_t { get set }
```

## See Also

- [var proc_suspend_resume: es_event_proc_suspend_resume_t](es_events_t/proc_suspend_resume.md)
  Properties of an event that indicates a call to suspend, resume, or shut down sockets for a process.
- [var remote_thread_create: es_event_remote_thread_create_t](es_events_t/remote_thread_create.md)
  Properties of an event that indicates an attempt by one process to spawn a thread in another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_events_t/trace)*