# dispatch_source_get_mask

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns the mask of events monitored by the dispatch source.

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
extern uintptr_t dispatch_source_get_mask(dispatch_source_t source);
```

### Return Value

The return value should be interpreted according to the type of the dispatch source, and can be one of the following:

- [`DISPATCH_SOURCE_TYPE_MACH_SEND`](./dispatch_source_type_mach_send.md):  `Dispatch Source Mach Send Event Flags`
- [`DISPATCH_SOURCE_TYPE_PROC`](./dispatch_source_type_proc.md): `Dispatch Source Process Event Flags`
- [`DISPATCH_SOURCE_TYPE_VNODE`](./dispatch_source_type_vnode.md): `Dispatch Source Vnode Event Flags`

## Discussion

The mask is a bitmask of relevant events being monitored by the dispatch event source. Any events that are not specified in the event mask are ignored and no event handler block is submitted for them.

For details, see the flag descriptions in `Constants`.

## Parameters

- `source`: This parameter cannot be `NULL`.

## See Also

### Getting Dispatch Source Attributes
- [dispatch_source_get_data](./dispatch_source_get_data.md)
  Returns pending data for the dispatch source.
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
- [dispatch_source_memorypressure_flags_t](./dispatch_source_memorypressure_flags_t.md)
  Memory pressure events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_get_mask)*