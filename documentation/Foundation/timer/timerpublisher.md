# Timer.TimerPublisher

**Framework**: Foundation  
**Kind**: class

A publisher that repeatedly emits the current date on a given interval.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
final class TimerPublisher
```

## Topics

### Initializers
- [init(interval: TimeInterval, tolerance: TimeInterval?, runLoop: RunLoop, mode: RunLoop.Mode, options: RunLoop.SchedulerOptions?)](timer/timerpublisher/init(interval:tolerance:runloop:mode:options:).md)
  Creates a publisher that repeatedly emits the current date on the given interval.
### Instance Properties
- [let interval: TimeInterval](timer/timerpublisher/interval.md)
- [let mode: RunLoop.Mode](timer/timerpublisher/mode.md)
- [let options: RunLoop.SchedulerOptions?](timer/timerpublisher/options.md)
- [let runLoop: RunLoop](timer/timerpublisher/runloop.md)
- [let tolerance: TimeInterval?](timer/timerpublisher/tolerance.md)

## Relationships

### Conforms To
- [ConnectablePublisher](../Combine/ConnectablePublisher.md)
- [Publisher](../Combine/Publisher.md)

## See Also

- [static func publish(every: TimeInterval, tolerance: TimeInterval?, on: RunLoop, in: RunLoop.Mode, options: RunLoop.SchedulerOptions?) -> Timer.TimerPublisher](timer/publish(every:tolerance:on:in:options:).md)
  Returns a publisher that repeatedly emits the current date on the given interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/timerpublisher)*