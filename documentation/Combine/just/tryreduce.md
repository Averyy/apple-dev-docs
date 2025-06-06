# tryReduce(_:_:)

**Framework**: Combine  
**Kind**: method

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
func tryReduce<T>(_ initialResult: T, _ nextPartialResult: (T, Output) throws -> T) -> Result<T, any Error>.Publisher
```

## See Also

- [func collect() -> Just<[Output]>](just/collect.md)
- [func collect(Int) -> Publishers.CollectByCount<Self>](just/collect(_:).md)
  Collects up to the specified number of elements, and then emits a single array of the collection.
- [func collect<S>(Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions?) -> Publishers.CollectByTime<Self, S>](just/collect(_:options:).md)
  Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [func ignoreOutput() -> Empty<Output, Just<Output>.Failure>](just/ignoreoutput.md)
- [func reduce<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](just/reduce(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/tryreduce(_:_:))*