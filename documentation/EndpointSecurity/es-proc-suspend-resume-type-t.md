# es_proc_suspend_resume_type_t

**Framework**: Endpoint Security  
**Kind**: struct

The type of a process suspension or resumption event.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_proc_suspend_resume_type_t
```

## Topics

### Event Types
- [var ES_PROC_SUSPEND_RESUME_TYPE_SUSPEND: es_proc_suspend_resume_type_t](es_proc_suspend_resume_type_suspend.md)
  An event type for process suspension events.
- [var ES_PROC_SUSPEND_RESUME_TYPE_RESUME: es_proc_suspend_resume_type_t](es_proc_suspend_resume_type_resume.md)
  An event type for process resumption events.
- [var ES_PROC_SUSPEND_RESUME_TYPE_SHUTDOWN_SOCKETS: es_proc_suspend_resume_type_t](es_proc_suspend_resume_type_shutdown_sockets.md)
  An event type for process socket shutdown events.
### Initializers
- [init(UInt32)](es_proc_suspend_resume_type_t/init(_:).md)
- [init(rawValue: UInt32)](es_proc_suspend_resume_type_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](es_proc_suspend_resume_type_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var target: UnsafeMutablePointer<es_process_t>?](es_event_proc_suspend_resume_t/target.md)
  The process targeted by this event.
- [var type: es_proc_suspend_resume_type_t](es_event_proc_suspend_resume_t/type.md)
  The type of event: suspend, resume, or socket shutdown.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_proc_suspend_resume_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_proc_suspend_resume_type_t)*