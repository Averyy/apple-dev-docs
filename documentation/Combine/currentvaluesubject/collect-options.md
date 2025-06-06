# collect(_:options:)

**Framework**: Combine  
**Kind**: method

Collects elements by a given time-grouping strategy, and emits a single array of the collection.

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
func collect<S>(_ strategy: Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions? = nil) -> Publishers.CollectByTime<Self, S> where S : Scheduler
```

#### Return Value

A publisher that collects elements by a given strategy, and emits a single array of the collection.

#### Discussion

Use [`collect(_:options:)`](publisher/collect(_:options:).md) to emit arrays of elements on a schedule specified by a [`Scheduler`](scheduler.md) and `Stride` that you provide. At the end of each scheduled interval, the publisher sends an array that contains the items it collected. If the upstream publisher finishes before filling the buffer, the publisher sends an array that contains items it received. This may be fewer than the number of elements specified in the requested `Stride`.

If the upstream publisher fails with an error, this publisher forwards the error to the downstream receiver instead of sending its output.

The example above collects timestamps generated on a one-second [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) in groups (`Stride`) of five.

```swift
let sub = Timer.publish(every: 1, on: .main, in: .default)
    .autoconnect()
    .collect(.byTime(RunLoop.main, .seconds(5)))
    .sink { print("\($0)", terminator: "\n\n") }

// Prints: "[2020-01-24 00:54:46 +0000, 2020-01-24 00:54:47 +0000,
//          2020-01-24 00:54:48 +0000, 2020-01-24 00:54:49 +0000,
//          2020-01-24 00:54:50 +0000]"
```

> **Note**: When this publisher receives a request for `.max(n)` elements, it requests `.max(count * n)` from the upstream publisher.

When this publisher receives a request for `.max(n)` elements, it requests `.max(count * n)` from the upstream publisher.

## Parameters

- `strategy`: The timing group strategy used by the operator to collect and publish elements.
- `options`: Scheduler options to use for the strategy.

## See Also

- [func collect() -> Publishers.Collect<Self>](currentvaluesubject/collect.md)
  Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [func collect(Int) -> Publishers.CollectByCount<Self>](currentvaluesubject/collect(_:).md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func ignoreOutput() -> Publishers.IgnoreOutput<Self>](currentvaluesubject/ignoreoutput.md)
  Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [func reduce<T>(T, (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>](currentvaluesubject/reduce(_:_:).md)
  Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [func tryReduce<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>](currentvaluesubject/tryreduce(_:_:).md)
  Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/currentvaluesubject/collect(_:options:))*