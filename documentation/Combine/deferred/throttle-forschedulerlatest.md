# throttle(for:scheduler:latest:)

**Framework**: Combine  
**Kind**: method

Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.

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
func throttle<S>(for interval: S.SchedulerTimeType.Stride, scheduler: S, latest: Bool) -> Publishers.Throttle<Self, S> where S : Scheduler
```

#### Return Value

A publisher that emits either the most-recent or first element received during the specified interval.

#### Discussion

Use [`throttle(for:scheduler:latest:)`](publisher/throttle(for:scheduler:latest:).md) to selectively republish elements from an upstream publisher during an interval you specify. Other elements received from the upstream in the throttling interval aren’t republished.

In the example below, a [`Timer.TimerPublisher`](https://developer.apple.com/documentation/Foundation/Timer/TimerPublisher) produces elements on one-second intervals; the [`throttle(for:scheduler:latest:)`](publisher/throttle(for:scheduler:latest:).md) operator delivers the first event, then republishes only the latest event in the following ten second intervals:

```swift
cancellable = Timer.publish(every: 3.0, on: .main, in: .default)
    .autoconnect()
    .print("\(Date().description)")
    .throttle(for: 10.0, scheduler: RunLoop.main, latest: true)
    .sink(
        receiveCompletion: { print ("Completion: \($0).") },
        receiveValue: { print("Received Timestamp \($0).") }
     )

// Prints:
 //    Publish at: 2020-03-19 18:26:54 +0000: receive value: (2020-03-19 18:26:57 +0000)
 //    Received Timestamp 2020-03-19 18:26:57 +0000.
 //    Publish at: 2020-03-19 18:26:54 +0000: receive value: (2020-03-19 18:27:00 +0000)
 //    Publish at: 2020-03-19 18:26:54 +0000: receive value: (2020-03-19 18:27:03 +0000)
 //    Publish at: 2020-03-19 18:26:54 +0000: receive value: (2020-03-19 18:27:06 +0000)
 //    Publish at: 2020-03-19 18:26:54 +0000: receive value: (2020-03-19 18:27:09 +0000)
 //    Received Timestamp 2020-03-19 18:27:09 +0000.
```

## Parameters

- `interval`: The interval at which to find and emit either the most recent or the first element, expressed in the time system of the scheduler.
- `scheduler`: The scheduler on which to publish elements.
- `latest`: A Boolean value that indicates whether to publish the most recent element. If  , the publisher emits the first element received during the interval.

## See Also

- [func measureInterval<S>(using: S, options: S.SchedulerOptions?) -> Publishers.MeasureInterval<Self, S>](deferred/measureinterval(using:options:).md)
  Measures and emits the time interval between events received from an upstream publisher.
- [func debounce<S>(for: S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Debounce<Self, S>](deferred/debounce(for:scheduler:options:).md)
  Publishes elements only after a specified time interval elapses between events.
- [func delay<S>(for: S.SchedulerTimeType.Stride, tolerance: S.SchedulerTimeType.Stride?, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Delay<Self, S>](deferred/delay(for:tolerance:scheduler:options:).md)
  Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [func timeout<S>(S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?, customError: (() -> Self.Failure)?) -> Publishers.Timeout<Self, S>](deferred/timeout(_:scheduler:options:customerror:).md)
  Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/deferred/throttle(for:scheduler:latest:))*