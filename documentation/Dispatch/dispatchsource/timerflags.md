# DispatchSource.TimerFlags

**Framework**: Dispatch  
**Kind**: struct  
**Role**: Structure

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

```swift
struct TimerFlags
```

## Topics

### Timer Flags
- [static let strict: DispatchSource.TimerFlags](./timerflags/strict.md)
  The system makes its best effort to observe the timer’s specified leeway value, even if the value is smaller than the default leeway.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a Timer Source
- [class func makeTimerSource(flags: DispatchSource.TimerFlags, queue: DispatchQueue?) -> any DispatchSourceTimer](./maketimersource%28flags,queue%29.md)
  Creates a new dispatch source object for monitoring timer events.
- [protocol DispatchSourceTimer](../dispatchsourcetimer.md)
  A dispatch source that submits the event handler block based on a timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/timerflags)*