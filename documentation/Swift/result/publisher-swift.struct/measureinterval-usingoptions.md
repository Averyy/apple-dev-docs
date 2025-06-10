# measureInterval(using:options:)

**Framework**: Swift  
**Kind**: method

Measures and emits the time interval between events received from an upstream publisher.

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
func measureInterval<S>(using scheduler: S, options: S.SchedulerOptions? = nil) -> Publishers.MeasureInterval<Self, S> where S : Scheduler
```

#### Return Value

A publisher that emits elements representing the time interval between the elements it receives.

#### Discussion

Use [`measureInterval(using:options:)`](result/publisher-swift.struct/measureinterval(using:options:).md) to measure the time between events delivered from an upstream publisher.

In the example below, a 1-second [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) is used as the data source for an event publisher; the [`measureInterval(using:options:)`](result/publisher-swift.struct/measureinterval(using:options:).md) operator reports the elapsed time between the reception of events on the main run loop:

```swift
cancellable = Timer.publish(every: 1, on: .main, in: .default)
    .autoconnect()
    .measureInterval(using: RunLoop.main)
    .sink { print("\($0)", terminator: "\n") }

// Prints:
//      Stride(magnitude: 1.0013610124588013)
//      Stride(magnitude: 0.9992760419845581)
```

The output type of the returned publisher is the time interval of the provided scheduler.

This operator uses the provided scheduler’s `Scheduler/now` property to measure intervals between events.

## Parameters

- `scheduler`: A scheduler to use for tracking the timing of events.
- `options`: Options that customize the delivery of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/measureinterval(using:options:))*