# time

**Framework**: Endpoint Security  
**Kind**: property

The time the event occurred, expressed as a Darwin time value.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var time: timespec
```

## See Also

- [var mach_time: UInt64](es_message_t/mach_time.md)
  The time the event occurred, as a Mach time value.
- [var deadline: UInt64](es_message_t/deadline.md)
  The deadline by which your app must respond to the event.
- [var seq_num: UInt64](es_message_t/seq_num.md)
  The sequence number of the message.
- [var global_seq_num: UInt64](es_message_t/global_seq_num.md)
  The global sequence number of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/time)*