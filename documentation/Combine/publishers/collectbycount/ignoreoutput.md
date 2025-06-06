# ignoreOutput()

**Framework**: Combine  
**Kind**: method

Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).

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
func ignoreOutput() -> Publishers.IgnoreOutput<Self>
```

#### Return Value

A publisher that ignores all upstream elements.

#### Discussion

Use the [`ignoreOutput()`](publisher/ignoreoutput().md) operator to determine if a publisher is able to complete successfully or would fail.

In the example below, the array publisher (`numbers`) delivers the first five of its elements successfully, as indicated by the [`ignoreOutput()`](publisher/ignoreoutput().md) operator. The operator consumes, but doesn’t republish the elements downstream. However, the sixth element, `0`, causes the error throwing closure to catch a `NoZeroValuesAllowedError` that terminates the stream.

```swift
struct NoZeroValuesAllowedError: Error {}
let numbers = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9]
cancellable = numbers.publisher
    .tryFilter({ anInt in
        guard anInt != 0 else { throw NoZeroValuesAllowedError() }
        return anInt < 20
    })
    .ignoreOutput()
    .sink(receiveCompletion: {print("completion: \($0)")},
          receiveValue: {print("value \($0)")})

// Prints: "completion: failure(NoZeroValuesAllowedError())"
```

The output type of this publisher is [`Never`](https://developer.apple.com/documentation/Swift/Never).

## See Also

- [func collect() -> Publishers.Collect<Self>](publishers/collectbycount/collect.md)
  Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [func collect(Int) -> Publishers.CollectByCount<Self>](publishers/collectbycount/collect(_:).md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func collect<S>(Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions?) -> Publishers.CollectByTime<Self, S>](publishers/collectbycount/collect(_:options:).md)
  Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [func reduce<T>(T, (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>](publishers/collectbycount/reduce(_:_:).md)
  Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [func tryReduce<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>](publishers/collectbycount/tryreduce(_:_:).md)
  Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/collectbycount/ignoreoutput())*