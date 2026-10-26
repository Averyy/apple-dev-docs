# dispatch_source_timer_flags_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

Flags to use when configuring a timer dispatch source.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef unsigned long dispatch_source_timer_flags_t;
```

## Topics

### Timer Flags
- [var DISPATCH_TIMER_STRICT: Int32](./dispatch_timer_strict.md)
  The system makes its best effort to observe the timer’s specified leeway value, even if the value is smaller than the default leeway.

## See Also

### Managing Timer Parameters
- [dispatch_source_set_timer](./dispatch_source_set_timer.md)
  Sets a start time, interval, and leeway value for a timer source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_timer_flags_t)*