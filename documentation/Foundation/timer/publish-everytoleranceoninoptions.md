# publish(every:tolerance:on:in:options:)

**Framework**: Foundation  
**Kind**: method

Returns a publisher that repeatedly emits the current date on the given interval.

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
static func publish(every interval: TimeInterval, tolerance: TimeInterval? = nil, on runLoop: RunLoop, in mode: RunLoop.Mode, options: RunLoop.SchedulerOptions? = nil) -> Timer.TimerPublisher
```

#### Return Value

A publisher that repeatedly emits the current date on the given interval.

#### Discussion

The return type, [`Timer.TimerPublisher`](timer/timerpublisher.md), conforms to [`ConnectablePublisher`](https://developer.apple.com/documentation/Combine/ConnectablePublisher), which means you must explicitly connect to the [`Timer`](timer.md) publisher to begin publishing events. You can do this with a call to [`connect()`](https://developer.apple.com/documentation/Combine/ConnectablePublisher/connect()), or by using [`autoconnect()`](https://developer.apple.com/documentation/Combine/ConnectablePublisher/autoconnect()) to automatically connect when a subscriber attaches, as shown here:

```swift
cancellable = Timer.publish(every: 1, on: .main, in: .common)
    .autoconnect()
    .sink() {
        print ("timer fired: \($0)")
}

```

## Parameters

- `interval`: The time interval on which to publish events. For example, a value of   publishes an event approximately every half-second.
- `tolerance`: The allowed timing variance when emitting events. Defaults to  , which allows any variance.
- `runLoop`: The run loop on which the timer runs.
- `mode`: The run loop mode in which to run the timer.
- `options`: Scheduler options passed to the timer. Defaults to  .

## Topics

### Creating a Timer Publisher
- [init(interval: TimeInterval, tolerance: TimeInterval?, runLoop: RunLoop, mode: RunLoop.Mode, options: RunLoop.SchedulerOptions?)](timer/timerpublisher/init(interval:tolerance:runloop:mode:options:).md)
  Creates a publisher that repeatedly emits the current date on the given interval.

## See Also

- [Timer.TimerPublisher](timer/timerpublisher.md)
  A publisher that repeatedly emits the current date on a given interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/publish(every:tolerance:on:in:options:))*