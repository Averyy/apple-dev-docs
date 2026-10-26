# dispatch_source_memorypressure_flags_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

Memory pressure events.

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
typedef unsigned long dispatch_source_memorypressure_flags_t;
```

## Topics

### Memory Pressure Event Flags
- [var DISPATCH_MEMORYPRESSURE_WARN: Int32](./dispatch_memorypressure_warn.md)
  The system memory pressure condition is at the warning stage.
- [var DISPATCH_MEMORYPRESSURE_NORMAL: Int32](./dispatch_memorypressure_normal.md)
  The system memory pressure condition has returned to normal.
- [var DISPATCH_MEMORYPRESSURE_CRITICAL: Int32](./dispatch_memorypressure_critical.md)
  The system memory pressure condition is at the critical stage.

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
- [dispatch_source_proc_flags_t](./dispatch_source_proc_flags_t.md)
  Events related to a process.
- [dispatch_source_vnode_flags_t](./dispatch_source_vnode_flags_t.md)
  Events involving a change to a file system object.
- [typealias dispatch_source_mach_recv_flags_t](./dispatch_source_mach_recv_flags_t.md)
  Mach receive-right flags.
- [dispatch_source_mach_send_flags_t](./dispatch_source_mach_send_flags_t.md)
  Mach send-right flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_memorypressure_flags_t)*