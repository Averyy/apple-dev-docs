# Publishers.TimeGroupingStrategy

**Framework**: Combine  
**Kind**: enum

A strategy for collecting received elements.

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
enum TimeGroupingStrategy<Context> where Context : Scheduler
```

## Topics

### Time groupings
- [case byTime(Context, Context.SchedulerTimeType.Stride)](publishers/timegroupingstrategy/bytime(_:_:).md)
  A grouping that collects and periodically publishes items.
- [case byTimeOrCount(Context, Context.SchedulerTimeType.Stride, Int)](publishers/timegroupingstrategy/bytimeorcount(_:_:_:).md)
  A grouping that collects and publishes items periodically or when a buffer reaches a maximum size.

## See Also

- [func collect() -> Publishers.Collect<Self>](publisher/collect.md)
  Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [func collect(Int) -> Publishers.CollectByCount<Self>](publisher/collect(_:).md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func collect<S>(Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions?) -> Publishers.CollectByTime<Self, S>](publisher/collect(_:options:).md)
  Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [func ignoreOutput() -> Publishers.IgnoreOutput<Self>](publisher/ignoreoutput.md)
  Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [func reduce<T>(T, (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>](publisher/reduce(_:_:).md)
  Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [func tryReduce<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>](publisher/tryreduce(_:_:).md)
  Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/timegroupingstrategy)*