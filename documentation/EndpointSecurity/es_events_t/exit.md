# exit

**Framework**: Endpoint Security  
**Kind**: property

Properties of an event that indicates a process exiting.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var exit: es_event_exit_t { get set }
```

## See Also

- [var chdir: es_event_chdir_t](es_events_t/chdir.md)
  Properties of an event that indicates a change to a process’s working directory.
- [var chroot: es_event_chroot_t](es_events_t/chroot.md)
  Properties of an event that indicates a change to a process’s root directory.
- [var exec: es_event_exec_t](es_events_t/exec.md)
  Properties of an event that indicates the execution of a process.
- [var fork: es_event_fork_t](es_events_t/fork.md)
  Properties of an event that indicates the forking of a process.
- [var proc_check: es_event_proc_check_t](es_events_t/proc_check.md)
  Properties of an event that indicate the retrieval of process information.
- [var signal: es_event_signal_t](es_events_t/signal.md)
  Properties of an event that indicates the sending of a signal to a process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_events_t/exit)*