# Timer.TimerPublisher

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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
- [init(interval: TimeInterval, tolerance: TimeInterval?, runLoop: RunLoop, mode: RunLoop.Mode, options: RunLoop.SchedulerOptions?)](./timerpublisher/init%28interval,tolerance,runloop,mode,options%29.md)
  Creates a publisher that repeatedly emits the current date on the given interval.
### Instance Properties
- [let interval: TimeInterval](./timerpublisher/interval.md)
- [let mode: RunLoop.Mode](./timerpublisher/mode.md)
- [let options: RunLoop.SchedulerOptions?](./timerpublisher/options.md)
- [let runLoop: RunLoop](./timerpublisher/runloop.md)
- [let tolerance: TimeInterval?](./timerpublisher/tolerance.md)

## Relationships

### Conforms To
- [ConnectablePublisher](../../Combine/connectablepublisher.md)
- [Publisher](../../Combine/publisher.md)

## See Also

### Firing Messages as a Combine Publisher
- [static func publish(every: TimeInterval, tolerance: TimeInterval?, on: RunLoop, in: RunLoop.Mode, options: RunLoop.SchedulerOptions?) -> Timer.TimerPublisher](./publish%28every,tolerance,on,in,options%29.md)
  Returns a publisher that repeatedly emits the current date on the given interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/timerpublisher)*