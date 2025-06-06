# es_event_proc_check_t

**Framework**: Endpoint Security  
**Kind**: struct

A type that indicates the call used and the data returned when a process checks on the access of the target process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_proc_check_t
```

## Topics

### Inspecting Event Properties
- [var flavor: Int32](es_event_proc_check_t/flavor.md)
  A representation of the information sought by a process based on the type member of [`es_event_proc_check_t`](es_event_proc_check_t.md).
- [var target: UnsafeMutablePointer<es_process_t>?](es_event_proc_check_t/target.md)
  The process targeted by this event.
- [var type: es_proc_check_type_t](es_event_proc_check_t/type.md)
  The type of call number used to check the access on the target process.
- [struct es_proc_check_type_t](es_proc_check_type_t.md)
  The type of call used when a process checks on the access of the target process.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_proc_check_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_proc_check_t/init.md)
- [init(target: UnsafeMutablePointer<es_process_t>?, type: es_proc_check_type_t, flavor: Int32, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_proc_check_t/init(target:type:flavor:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_chdir_t](es_event_chdir_t.md)
  A type for an event that indicates a change to a process’s working directory.
- [struct es_event_chroot_t](es_event_chroot_t.md)
  A type for an event that indicates a change to a process’s root directory.
- [struct es_event_exec_t](es_event_exec_t.md)
  A type for an event that indicates the execution of a process.
- [struct es_event_fork_t](es_event_fork_t.md)
  A type for an event that indicates the forking of a process.
- [struct es_event_signal_t](es_event_signal_t.md)
  A type for an event that indicates the sending of a signal to a process.
- [struct es_event_exit_t](es_event_exit_t.md)
  A type for an event that indicates a process exiting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_proc_check_t)*