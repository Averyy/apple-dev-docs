# DispatchTimeoutResult

**Framework**: Dispatch  
**Kind**: enum  
**Role**: Enumeration

A result value indicating whether a dispatch operation finished before a specified time.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
@frozen
enum DispatchTimeoutResult
```

## Topics

### Enumeration Cases
- [DispatchTimeoutResult.success](./dispatchtimeoutresult/success.md)
  Indicates that a dispatch operation successfully finished before the specified time elapsed.
- [DispatchTimeoutResult.timedOut](./dispatchtimeoutresult/timedout.md)
  Indicates that a dispatch operation failed to finish before the specified time elapsed.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Time Constructs
- [struct DispatchTime](./dispatchtime.md)
  A point in time relative to the default clock, with nanosecond precision.
- [struct DispatchWallTime](./dispatchwalltime.md)
  An absolute point in time according to the wall clock, with microsecond precision.
- [enum DispatchTimeInterval](./dispatchtimeinterval.md)
  A number of seconds, millisconds, microseconds, or nanoseconds.
- [typealias dispatch_time_t](./dispatch_time_t.md)
  An abstract representation of time.
- [var DISPATCH_WALLTIME_NOW: UInt](./dispatch_walltime_now.md)
  The current time.
- [Wall Time Constants](./api-2963138-wall-time-constants.md)
  Constants for wall time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchtimeoutresult)*