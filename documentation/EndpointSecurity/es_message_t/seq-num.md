# seq_num

**Framework**: Endpoint Security  
**Kind**: property

The sequence number of the message.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var seq_num: UInt64
```

#### Discussion

Inspect the sequence number per-client and per-event-type to detect whether the kernel had to drop events for this client. If the kernel doesn’t drop any events for this client, `seq_num` increments by 1 for every message of that event type.

To determine whether the kernel dropped events, compare the previous value of `seq_num` for this event type to the value received in the latest message. When the kernel drops no events, the difference is 1, since the current message increments the counter. You can therefore calculate the number of dropped messages as follows:

```c
numberOfDroppedEvents = thisMessage.seq_num - (prevMessage.seq_num + 1)
```

Dropped events generally indicate that the kernel generated more events than the client could handle.

This field is available if the message version is greater than `2`.

> 💡 **Tip**:  For an equivalent counter that filters only by client and not event type, see [`global_seq_num`](es_message_t/global_seq_num.md).

## See Also

- [var time: timespec](es_message_t/time.md)
  The time the event occurred, expressed as a Darwin time value.
- [var mach_time: UInt64](es_message_t/mach_time.md)
  The time the event occurred, as a Mach time value.
- [var deadline: UInt64](es_message_t/deadline.md)
  The deadline by which your app must respond to the event.
- [var global_seq_num: UInt64](es_message_t/global_seq_num.md)
  The global sequence number of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/seq_num)*