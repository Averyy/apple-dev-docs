# type

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The type of event: suspend, resume, or socket shutdown.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var type: es_proc_suspend_resume_type_t
```

```c
es_proc_suspend_resume_type_t type;
```

## See Also

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_process_t>?](./target.md)
  The process targeted by this event.
- [struct es_proc_suspend_resume_type_t](../es_proc_suspend_resume_type_t.md)
  The type of a process suspension or resumption event.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_proc_suspend_resume_t/type)*