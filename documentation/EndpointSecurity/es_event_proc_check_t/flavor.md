# flavor

**Framework**: Endpoint Security  
**Kind**: property

A representation of the information sought by a process based on the type member of [`es_event_proc_check_t`](es_event_proc_check_t.md).

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var flavor: Int32
```

## See Also

- [var target: UnsafeMutablePointer<es_process_t>?](es_event_proc_check_t/target.md)
  The process targeted by this event.
- [var type: es_proc_check_type_t](es_event_proc_check_t/type.md)
  The type of call number used to check the access on the target process.
- [struct es_proc_check_type_t](es_proc_check_type_t.md)
  The type of call used when a process checks on the access of the target process.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_proc_check_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_proc_check_t/flavor)*