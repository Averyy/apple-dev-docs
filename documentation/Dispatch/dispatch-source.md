# Dispatch Source

**Framework**: Dispatch  
**Role**: API Collection

An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.

## Topics

### Creating a Dispatch Source
- [typealias dispatch_source_t](./dispatch_source_t.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [dispatch_source_create](./dispatch_source_create.md)
  Creates a new dispatch source to monitor low-level system events.
- [dispatch_source_type_t](./dispatch_source_type_t.md)
  An identifier for the type of system object being monitored by a dispatch source.
### Getting Dispatch Source Attributes
- [typealias dispatch_source_mach_recv_flags_t](./dispatch_source_mach_recv_flags_t.md)
  Mach receive-right flags.
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
- [dispatch_source_mach_send_flags_t](./dispatch_source_mach_send_flags_t.md)
  Mach send-right flags.
- [dispatch_source_memorypressure_flags_t](./dispatch_source_memorypressure_flags_t.md)
  Memory pressure events.
### Managing Event Handlers
- [dispatch_source_set_registration_handler_f](./dispatch_source_set_registration_handler_f.md)
  Sets the registration handler function for the given dispatch source.
- [dispatch_source_set_registration_handler](./dispatch_source_set_registration_handler.md)
  Sets the registration handler block for the given dispatch source.
- [dispatch_source_set_event_handler_f](./dispatch_source_set_event_handler_f.md)
  Sets the event handler function for the given dispatch source.
- [dispatch_source_set_event_handler](./dispatch_source_set_event_handler.md)
  Sets the event handler block for the given dispatch source.
- [dispatch_source_set_cancel_handler_f](./dispatch_source_set_cancel_handler_f.md)
  Sets the cancellation handler function for the given dispatch source.
- [dispatch_source_set_cancel_handler](./dispatch_source_set_cancel_handler.md)
  Sets the cancellation handler block for the given dispatch source.
### Managing Timer Parameters
- [dispatch_source_set_timer](./dispatch_source_set_timer.md)
  Sets a start time, interval, and leeway value for a timer source.
- [dispatch_source_timer_flags_t](./dispatch_source_timer_flags_t.md)
  Flags to use when configuring a timer dispatch source.
### Canceling a Dispatch Source
- [dispatch_source_cancel](./dispatch_source_cancel.md)
  Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.
- [dispatch_source_testcancel](./dispatch_source_testcancel.md)
  Tests whether the given dispatch source has been canceled.

## See Also

### System Event Monitoring
- [class DispatchSource](./dispatchsource.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [class DispatchIO](./dispatchio.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [struct DispatchData](./dispatchdata.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [struct DispatchDataIterator](./dispatchdataiterator.md)
  A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch I/O](./dispatch-i-o.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](./dispatch-data.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [protocol DispatchSourceProtocol](./dispatchsourceprotocol.md)
  Defines a common set of properties and methods that are shared with all dispatch source types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-source)*