# dispatch_source_get_handle

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns the underlying system handle associated with the specified dispatch source.

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
extern uintptr_t dispatch_source_get_handle(dispatch_source_t source);
```

### Return Value

The return value should be interpreted according to the type of the dispatch source, and can be one of the following:

- [`DISPATCH_SOURCE_TYPE_MACH_SEND`](./dispatch_source_type_mach_send.md):  mach port (`mach_port_t`)
- [`DISPATCH_SOURCE_TYPE_MACH_RECV`](./dispatch_source_type_mach_recv.md):  mach port (`mach_port_t`)
- [`DISPATCH_SOURCE_TYPE_PROC`](./dispatch_source_type_proc.md): process identifier (`pid_t`)
- [`DISPATCH_SOURCE_TYPE_READ`](./dispatch_source_type_read.md): file descriptor (`int`)
- [`DISPATCH_SOURCE_TYPE_SIGNAL`](./dispatch_source_type_signal.md): signal number (`int`)
- [`DISPATCH_SOURCE_TYPE_VNODE`](./dispatch_source_type_vnode.md): file descriptor (`int`)
- `Dispatch Source Memory Pressure Event Flags`: file descriptor (`int`)

## Discussion

The handle returned is a reference to the underlying system object being monitored by the dispatch source.

## Parameters

- `source`: This parameter cannot be NULL.

## See Also

### Getting Dispatch Source Attributes
- [dispatch_source_get_data](./dispatch_source_get_data.md)
  Returns pending data for the dispatch source.
- [dispatch_source_get_mask](./dispatch_source_get_mask.md)
  Returns the mask of events monitored by the dispatch source.
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
- [dispatch_source_memorypressure_flags_t](./dispatch_source_memorypressure_flags_t.md)
  Memory pressure events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_get_handle)*