# WakeAtTime

**Framework**: DriverKit  
**Kind**: method

Schedules a callback from the timer.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t WakeAtTime(uint64_t options, uint64_t deadline, uint64_t leeway);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

#### Discussion

Use this method to schedule the execution time for your timer. Call this method from a block running on the same dispatch queue you passed to the [`Create`](iotimerdispatchsource/create.md) method. If a previously scheduled timer has not yet fired, calling this method replaces the old time with the new value.

## Parameters

- `options`: The timebase to use when interpreting the   and   parameters. For a list of possible values, see  .
- `deadline`: The time at which to execute your action. The meaning of this parameter depends on the timebase you specified in the   parameter.
- `leeway`: The maximum amount of time beyond the scheduled   that the system may wait before executing your action. Leeway values improve the system’s power usage by letting the system schedule timers at a more advantageous time. The system guarantees the execution of the timer’s action before the combined   and   values expire.

## See Also

- [Clock Types](3242783-clock_types.md)
  Clock types to use when configuring a timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource/wakeattime)*