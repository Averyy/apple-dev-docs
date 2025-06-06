# es_event_exit_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates a process exiting.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_exit_t
```

## Topics

### Inspecting Event Properties
- [var stat: Int32](es_event_exit_t/stat.md)
  The exit status of the process.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_exit_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_exit_t/init.md)
- [init(stat: Int32, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_exit_t/init(stat:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct es_event_chdir_t](es_event_chdir_t.md)
  A type for an event that indicates a change to a process’s working directory.
- [struct es_event_chroot_t](es_event_chroot_t.md)
  A type for an event that indicates a change to a process’s root directory.
- [struct es_event_exec_t](es_event_exec_t.md)
  A type for an event that indicates the execution of a process.
- [struct es_event_fork_t](es_event_fork_t.md)
  A type for an event that indicates the forking of a process.
- [struct es_event_proc_check_t](es_event_proc_check_t.md)
  A type that indicates the call used and the data returned when a process checks on the access of the target process.
- [struct es_event_signal_t](es_event_signal_t.md)
  A type for an event that indicates the sending of a signal to a process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_exit_t)*