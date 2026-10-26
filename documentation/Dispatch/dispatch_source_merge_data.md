# dispatch_source_merge_data

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Merges data into a dispatch source and submits its event handler block to its target queue.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_source_merge_data(dispatch_source_t source, uintptr_t value);
```

#### Discussion

Your application can use this function to indicate that an event has occurred on one of the application-defined dispatch event sources of type [`DISPATCH_SOURCE_TYPE_DATA_ADD`](./dispatch_source_type_data_add.md) or [`DISPATCH_SOURCE_TYPE_DATA_OR`](./dispatch_source_type_data_or.md).

## Parameters

- `source`: This parameter cannot be `NULL`.
- `value`: The value to coalesce with the pending data using a logical OR or an ADD as specified by the dispatch source type. A value of zero has no effect and does not result in the submission of the event handler block.

## See Also

### Getting Dispatch Source Attributes
- [dispatch_source_get_data](./dispatch_source_get_data.md)
  Returns pending data for the dispatch source.
- [dispatch_source_get_mask](./dispatch_source_get_mask.md)
  Returns the mask of events monitored by the dispatch source.
- [dispatch_source_get_handle](./dispatch_source_get_handle.md)
  Returns the underlying system handle associated with the specified dispatch source.
- [dispatch_source_proc_flags_t](./dispatch_source_proc_flags_t.md)
  Events related to a process.
- [dispatch_source_vnode_flags_t](./dispatch_source_vnode_flags_t.md)
  Events involving a change to a file system object.
- [typealias dispatch_source_mach_recv_flags_t](./dispatch_source_mach_recv_flags_t.md)
  Mach receive-right flags.
- [dispatch_source_mach_send_flags_t](./dispatch_source_mach_send_flags_t.md)
  Mach send-right flags.
- [dispatch_source_memorypressure_flags_t](./dispatch_source_memorypressure_flags_t.md)
  Memory pressure events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_merge_data)*