# collect()

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.

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
func collect() -> Publishers.Collect<Self>
```

#### Return Value

A publisher that collects all received items and returns them as an array upon completion.

#### Discussion

Use [`collect()`](./collect%28%29.md) to gather elements into an array that the operator emits after the upstream publisher finishes.

If the upstream publisher fails with an error, this publisher forwards the error to the downstream receiver instead of sending its output.

This publisher requests an unlimited number of elements from the upstream publisher and uses an unbounded amount of memory to store the received values. The publisher may exert memory pressure on the system for very large sets of elements.

The [`collect()`](./collect%28%29.md) operator only sends the collected array to its downstream receiver after a request whose demand is greater than 0 items. Otherwise, [`collect()`](./collect%28%29.md) waits until it receives a non-zero request.

In the example below, an Integer range is a publisher that emits an array of integers:

```swift
let numbers = (0...10)
cancellable = numbers.publisher
    .collect()
    .sink { print("\($0)") }

// Prints: "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
```

## See Also

### Reducing elements
- [func collect(Int) -> Publishers.CollectByCount<Self>](./collect%28_%29.md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func collect<S>(Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions?) -> Publishers.CollectByTime<Self, S>](./collect%28_,options%29.md)
  Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [Publishers.TimeGroupingStrategy](../publishers/timegroupingstrategy.md)
  A strategy for collecting received elements.
- [func ignoreOutput() -> Publishers.IgnoreOutput<Self>](./ignoreoutput%28%29.md)
  Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [func reduce<T>(T, (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>](./reduce%28_,_%29.md)
  Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [func tryReduce<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>](./tryreduce%28_,_%29.md)
  Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/collect())*