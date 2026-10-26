# DISPATCH_SOURCE_TYPE_DATA_OR

**Framework**: Dispatch  
**Kind**: macro  
**Role**: Macro

A type of dispatch source for monitoring custom events involving the coalescing of data with an OR operator.

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
#define DISPATCH_SOURCE_TYPE_DATA_OR
```

#### Discussion

A dispatch source that coalesces data obtained via calls to [`dispatch_source_merge_data`](./dispatch_source_merge_data.md). A bitwise OR is used to coalesce the data. The handle is unused (pass zero for now). The mask is unused (pass zero for now).

## See Also

### Dispatch Source Types
- [DISPATCH_SOURCE_TYPE_TIMER](./dispatch_source_type_timer.md)
  A type of dispatch source for monitoring a timer.
- [DISPATCH_SOURCE_TYPE_READ](./dispatch_source_type_read.md)
  A type of dispatch source for monitoring read operations on a file descriptor.
- [DISPATCH_SOURCE_TYPE_WRITE](./dispatch_source_type_write.md)
  A type of dispatch source for monitoring write operations on a file descriptor.
- [DISPATCH_SOURCE_TYPE_VNODE](./dispatch_source_type_vnode.md)
  A type of dispatch source for monitoring changes to a file system object.
- [DISPATCH_SOURCE_TYPE_SIGNAL](./dispatch_source_type_signal.md)
  A type of dispatch source for monitoring signals.
- [DISPATCH_SOURCE_TYPE_PROC](./dispatch_source_type_proc.md)
  A type of dispatch source for monitoring a process.
- [DISPATCH_SOURCE_TYPE_MEMORYPRESSURE](./dispatch_source_type_memorypressure.md)
  A type of dispatch source for monitoring memory pressure events.
- [DISPATCH_SOURCE_TYPE_MACH_SEND](./dispatch_source_type_mach_send.md)
  A type of dispatch source for monitoring a mach send port.
- [DISPATCH_SOURCE_TYPE_MACH_RECV](./dispatch_source_type_mach_recv.md)
  A type of dispatch source for monitoring a mach receive port.
- [DISPATCH_SOURCE_TYPE_DATA_ADD](./dispatch_source_type_data_add.md)
  A type of dispatch source for monitoring custom events involving the coalescing of data with an AND operator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_type_data_or)*