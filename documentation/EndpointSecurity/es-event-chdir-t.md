# es_event_chdir_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates a change to a process’s working directory.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_chdir_t
```

## Topics

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_file_t>](es_event_chdir_t/target.md)
  The new current working directory.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_chdir_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(target: UnsafeMutablePointer<es_file_t>, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_chdir_t/init(target:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

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
- [struct es_event_exit_t](es_event_exit_t.md)
  A type for an event that indicates a process exiting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_chdir_t)*