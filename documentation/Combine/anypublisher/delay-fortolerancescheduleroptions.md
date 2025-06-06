# delay(for:tolerance:scheduler:options:)

**Framework**: Combine  
**Kind**: method

Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.

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
func delay<S>(for interval: S.SchedulerTimeType.Stride, tolerance: S.SchedulerTimeType.Stride? = nil, scheduler: S, options: S.SchedulerOptions? = nil) -> Publishers.Delay<Self, S> where S : Scheduler
```

#### Return Value

A publisher that delays delivery of elements and completion to the downstream receiver.

#### Discussion

Use [`delay(for:tolerance:scheduler:options:)`](publisher/delay(for:tolerance:scheduler:options:).md) when you need to delay the delivery of elements to a downstream by a specified amount of time.

In this example, a [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) publishes an event every second. The [`delay(for:tolerance:scheduler:options:)`](publisher/delay(for:tolerance:scheduler:options:).md) operator holds the delivery of the initial element for 3 seconds (±0.5 seconds), after which each element is delivered to the downstream on the main run loop after the specified delay:

```swift
let df = DateFormatter()
df.dateStyle = .none
df.timeStyle = .long
cancellable = Timer.publish(every: 1.0, on: .main, in: .default)
    .autoconnect()
    .handleEvents(receiveOutput: { date in
        print ("Sending Timestamp \'\(df.string(from: date))\' to delay()")
    })
    .delay(for: .seconds(3), scheduler: RunLoop.main, options: .none)
    .sink(
        receiveCompletion: { print ("completion: \($0)", terminator: "\n") },
        receiveValue: { value in
            let now = Date()
            print ("At \(df.string(from: now)) received  Timestamp \'\(df.string(from: value))\' sent: \(String(format: "%.2f", now.timeIntervalSince(value))) secs ago", terminator: "\n")
        }
    )

// Prints:
//    Sending Timestamp '5:02:33 PM PDT' to delay()
//    Sending Timestamp '5:02:34 PM PDT' to delay()
//    Sending Timestamp '5:02:35 PM PDT' to delay()
//    Sending Timestamp '5:02:36 PM PDT' to delay()
//    At 5:02:36 PM PDT received  Timestamp '5:02:33 PM PDT' sent: 3.00 secs ago
//    Sending Timestamp '5:02:37 PM PDT' to delay()
//    At 5:02:37 PM PDT received  Timestamp '5:02:34 PM PDT' sent: 3.00 secs ago
//    Sending Timestamp '5:02:38 PM PDT' to delay()
//    At 5:02:38 PM PDT received  Timestamp '5:02:35 PM PDT' sent: 3.00 secs ago
```

The delay affects the delivery of elements and completion, but not of the original subscription.

## Parameters

- `interval`: The amount of time to delay.
- `tolerance`: The allowed tolerance in delivering delayed events. The   publisher may deliver elements this much sooner or later than the interval specifies.
- `scheduler`: The scheduler to deliver the delayed events.
- `options`: Options relevant to the scheduler’s behavior.

## See Also

- [func measureInterval<S>(using: S, options: S.SchedulerOptions?) -> Publishers.MeasureInterval<Self, S>](anypublisher/measureinterval(using:options:).md)
  Measures and emits the time interval between events received from an upstream publisher.
- [func debounce<S>(for: S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?) -> Publishers.Debounce<Self, S>](anypublisher/debounce(for:scheduler:options:).md)
  Publishes elements only after a specified time interval elapses between events.
- [func throttle<S>(for: S.SchedulerTimeType.Stride, scheduler: S, latest: Bool) -> Publishers.Throttle<Self, S>](anypublisher/throttle(for:scheduler:latest:).md)
  Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [func timeout<S>(S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions?, customError: (() -> Self.Failure)?) -> Publishers.Timeout<Self, S>](anypublisher/timeout(_:scheduler:options:customerror:).md)
  Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/anypublisher/delay(for:tolerance:scheduler:options:))*