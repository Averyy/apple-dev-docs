# deadline

**Framework**: Endpoint Security  
**Kind**: property

The deadline by which your app must respond to the event.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var deadline: UInt64
```

#### Discussion

If you fail to respond to an event before this deadline, Endpoint Security may terminate the client process, or restart the process if it’s a system extension. If your client repeatedly misses deadlines, Endpoint Security may refuse new connections from [`es_new_client(_:_:)`](es_new_client(_:_:).md) altogether.

## See Also

- [var time: timespec](es_message_t/time.md)
  The time the event occurred, expressed as a Darwin time value.
- [var mach_time: UInt64](es_message_t/mach_time.md)
  The time the event occurred, as a Mach time value.
- [var seq_num: UInt64](es_message_t/seq_num.md)
  The sequence number of the message.
- [var global_seq_num: UInt64](es_message_t/global_seq_num.md)
  The global sequence number of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/deadline)*