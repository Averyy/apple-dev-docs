# DispatchSource.TimerFlags

**Framework**: Dispatch  
**Kind**: struct

Flags to use when configuring a timer dispatch source.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct TimerFlags
```

## Topics

### Timer Flags
- [static let strict: DispatchSource.TimerFlags](dispatchsource/timerflags/strict.md)
  The system makes its best effort to observe the timer’s specified leeway value, even if the value is smaller than the default leeway.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class func makeTimerSource(flags: DispatchSource.TimerFlags, queue: DispatchQueue?) -> any DispatchSourceTimer](dispatchsource/maketimersource(flags:queue:).md)
  Creates a new dispatch source object for monitoring timer events.
- [protocol DispatchSourceTimer](dispatchsourcetimer.md)
  A dispatch source that submits the event handler block based on a timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/timerflags)*