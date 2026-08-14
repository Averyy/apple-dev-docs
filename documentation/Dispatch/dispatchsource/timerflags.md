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
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [class func makeTimerSource(flags: DispatchSource.TimerFlags, queue: DispatchQueue?) -> any DispatchSourceTimer](dispatchsource/maketimersource(flags:queue:).md)
  Creates a new dispatch source object for monitoring timer events.
- [protocol DispatchSourceTimer](dispatchsourcetimer.md)
  A dispatch source that submits the event handler block based on a timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/timerflags)*