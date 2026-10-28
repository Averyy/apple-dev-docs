# deadline

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The deadline by which your app must respond to the event.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var deadline: UInt64
```

```c
uint64_t deadline;
```

## Discussion

If you fail to respond to an event before this deadline, Endpoint Security may terminate the client process, or restart the process if it’s a system extension. If your client repeatedly misses deadlines, Endpoint Security may refuse new connections from [`es_new_client(_:_:)`](../es_new_client%28_,_%29.md) altogether.

## See Also

### Inspecting Timing Properties
- [var time: timespec](./time.md)
  The time the event occurred, expressed as a Darwin time value.
- [var mach_time: UInt64](./mach_time.md)
  The time the event occurred, as a Mach time value.
- [var seq_num: UInt64](./seq_num.md)
  The sequence number of the message.
- [var global_seq_num: UInt64](./global_seq_num.md)
  The global sequence number of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/deadline)*