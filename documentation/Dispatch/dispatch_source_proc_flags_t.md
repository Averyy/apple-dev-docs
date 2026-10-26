# dispatch_source_proc_flags_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

Events related to a process.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef unsigned long dispatch_source_proc_flags_t;
```

## Topics

### Process Event Flags
- [var DISPATCH_PROC_EXEC: Int32](./dispatch_proc_exec.md)
  The process became another executable image.
- [var DISPATCH_PROC_EXIT: UInt32](./dispatch_proc_exit.md)
  The process has exited (perhaps cleanly, perhaps not).
- [var DISPATCH_PROC_FORK: Int32](./dispatch_proc_fork.md)
  The process created one or more child processes.
- [var DISPATCH_PROC_SIGNAL: Int32](./dispatch_proc_signal.md)
  The process received a UNIX signal.

## See Also

### Getting Dispatch Source Attributes
- [dispatch_source_get_data](./dispatch_source_get_data.md)
  Returns pending data for the dispatch source.
- [dispatch_source_get_mask](./dispatch_source_get_mask.md)
  Returns the mask of events monitored by the dispatch source.
- [dispatch_source_get_handle](./dispatch_source_get_handle.md)
  Returns the underlying system handle associated with the specified dispatch source.
- [dispatch_source_merge_data](./dispatch_source_merge_data.md)
  Merges data into a dispatch source and submits its event handler block to its target queue.
- [dispatch_source_vnode_flags_t](./dispatch_source_vnode_flags_t.md)
  Events involving a change to a file system object.
- [typealias dispatch_source_mach_recv_flags_t](./dispatch_source_mach_recv_flags_t.md)
  Mach receive-right flags.
- [dispatch_source_mach_send_flags_t](./dispatch_source_mach_send_flags_t.md)
  Mach send-right flags.
- [dispatch_source_memorypressure_flags_t](./dispatch_source_memorypressure_flags_t.md)
  Memory pressure events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_proc_flags_t)*