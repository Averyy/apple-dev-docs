# reserved

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

An unused field reserved for future use.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)
```

```c
uint8_t reserved[64];
```

## See Also

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_process_t>?](./target.md)
  The process targeted by this event.
- [var type: es_proc_suspend_resume_type_t](./type.md)
  The type of event: suspend, resume, or socket shutdown.
- [struct es_proc_suspend_resume_type_t](../es_proc_suspend_resume_type_t.md)
  The type of a process suspension or resumption event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_proc_suspend_resume_t/reserved)*