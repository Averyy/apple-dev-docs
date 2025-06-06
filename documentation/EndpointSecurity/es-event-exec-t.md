# es_event_exec_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the execution of a process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_exec_t
```

#### Overview

To get the process’ arguments, file descriptors, and environment variables from this type, use the following functions:

- Arguments — [`es_exec_arg(_:_:)`](es_exec_arg(_:_:).md) and [`es_exec_arg_count(_:)`](es_exec_arg_count(_:).md).
- Environment variables — [`es_exec_env(_:_:)`](es_exec_env(_:_:).md), and [`es_exec_env_count(_:)`](es_exec_env_count(_:).md).
- File descriptors — [`es_exec_fd(_:_:)`](es_exec_fd(_:_:).md), [`es_exec_fd_count(_:)`](es_exec_fd_count(_:).md).

## Topics

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_process_t>](es_event_exec_t/target.md)
  The process to execute.
- [struct es_process_t](es_process_t.md)
  A type that describes a process, as delivered by an Endpoint Security message.
### Instance Properties
- [var cwd: UnsafeMutablePointer<es_file_t>](es_event_exec_t/cwd-7pogi.md)
- [var dyld_exec_path: es_string_token_t](es_event_exec_t/dyld_exec_path.md)
- [var image_cpusubtype: cpu_subtype_t](es_event_exec_t/image_cpusubtype-4h1ft.md)
- [var image_cputype: cpu_type_t](es_event_exec_t/image_cputype-9u2jr.md)
- [var last_fd: Int32](es_event_exec_t/last_fd-g0rc.md)
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_exec_t/reserved-25qdu.md)
- [var script: UnsafeMutablePointer<es_file_t>?](es_event_exec_t/script-19tlj.md)

## See Also

- [struct es_event_chdir_t](es_event_chdir_t.md)
  A type for an event that indicates a change to a process’s working directory.
- [struct es_event_chroot_t](es_event_chroot_t.md)
  A type for an event that indicates a change to a process’s root directory.
- [struct es_event_fork_t](es_event_fork_t.md)
  A type for an event that indicates the forking of a process.
- [struct es_event_proc_check_t](es_event_proc_check_t.md)
  A type that indicates the call used and the data returned when a process checks on the access of the target process.
- [struct es_event_signal_t](es_event_signal_t.md)
  A type for an event that indicates the sending of a signal to a process.
- [struct es_event_exit_t](es_event_exit_t.md)
  A type for an event that indicates a process exiting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_exec_t)*