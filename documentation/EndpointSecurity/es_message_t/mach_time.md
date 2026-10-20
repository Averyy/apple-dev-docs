# mach_time

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The time the event occurred, as a Mach time value.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var mach_time: UInt64
```

```c
uint64_t mach_time;
```

## See Also

### Inspecting Timing Properties
- [var time: timespec](./time.md)
  The time the event occurred, expressed as a Darwin time value.
- [var deadline: UInt64](./deadline.md)
  The deadline by which your app must respond to the event.
- [var seq_num: UInt64](./seq_num.md)
  The sequence number of the message.
- [var global_seq_num: UInt64](./global_seq_num.md)
  The global sequence number of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/mach_time)*