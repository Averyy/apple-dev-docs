# es_event_fork_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the forking of a process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_fork_t
```

## Topics

### Inspecting Event Properties
- [var child: UnsafeMutablePointer<es_process_t>](es_event_fork_t/child.md)
  The forked child process.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_fork_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(child: UnsafeMutablePointer<es_process_t>, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_fork_t/init(child:reserved:).md)

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
- [struct es_event_proc_check_t](es_event_proc_check_t.md)
  A type that indicates the call used and the data returned when a process checks on the access of the target process.
- [struct es_event_signal_t](es_event_signal_t.md)
  A type for an event that indicates the sending of a signal to a process.
- [struct es_event_exit_t](es_event_exit_t.md)
  A type for an event that indicates a process exiting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_fork_t)*