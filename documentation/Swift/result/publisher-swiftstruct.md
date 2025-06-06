# Result.Publisher

**Framework**: Swift  
**Kind**: struct

The type of a Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.

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
struct Publisher
```

#### Overview

If the result is `Swift/Result/success`, then the publisher waits until it receives a request for at least one value, then sends the output to all subscribers and finishes normally. If the result is `/Swift/Result/failure`, then the publisher sends the failure immediately upon subscription. This latter behavior is a contrast with [`Just`](https://developer.apple.com/documentation/Combine/Just), which always publishes a single value.

## Topics

### Declaring Publisher Topology
- [Result.Publisher.Output](result/publisher-swift.struct/output.md)
  The kind of values published by this publisher.
### Creating a Result Publisher
- [init(Result<Result<Success, Failure>.Publisher.Output, Failure>)](result/publisher-swift.struct/init(_:)-516t.md)
  Creates a publisher that delivers the specified result.
- [init(Failure)](result/publisher-swift.struct/init(_:)-69fv4.md)
  Creates a publisher that immediately terminates upon subscription with the given failure.
- [init(Result<Success, Failure>.Publisher.Output)](result/publisher-swift.struct/init(_:)-7t2tt.md)
  Creates a publisher that sends the specified output to all subscribers and finishes normally.
### Inspecting Publisher Properties
- [let result: Result<Result<Success, Failure>.Publisher.Output, Failure>](result/publisher-swift.struct/result.md)
  The result to deliver to each subscriber.
### Working with Subscribers
- [func receive<S>(subscriber: S)](result/publisher-swift.struct/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
### Instance Methods
- [func allSatisfy((Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Bool, Failure>.Publisher](result/publisher-swift.struct/allsatisfy(_:).md)
- [func collect() -> Result<[Result<Success, Failure>.Publisher.Output], Failure>.Publisher](result/publisher-swift.struct/collect.md)
- [func contains(Result<Success, Failure>.Publisher.Output) -> Result<Bool, Failure>.Publisher](result/publisher-swift.struct/contains(_:).md)
- [func contains(where: (Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Bool, Failure>.Publisher](result/publisher-swift.struct/contains(where:).md)
- [func count() -> Result<Int, Failure>.Publisher](result/publisher-swift.struct/count.md)
- [func first() -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](result/publisher-swift.struct/first.md)
- [func ignoreOutput() -> Empty<Result<Success, Failure>.Publisher.Output, Failure>](result/publisher-swift.struct/ignoreoutput.md)
- [func last() -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](result/publisher-swift.struct/last.md)
- [func map<T>((Result<Success, Failure>.Publisher.Output) -> T) -> Result<T, Failure>.Publisher](result/publisher-swift.struct/map(_:).md)
- [func mapError<E>((Failure) -> E) -> Result<Result<Success, Failure>.Publisher.Output, E>.Publisher](result/publisher-swift.struct/maperror(_:).md)
- [func max() -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](result/publisher-swift.struct/max.md)
- [func max(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](result/publisher-swift.struct/max(by:).md)
- [func min() -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](result/publisher-swift.struct/min.md)
- [func min(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](result/publisher-swift.struct/min(by:).md)
- [func reduce<T>(T, (T, Result<Success, Failure>.Publisher.Output) -> T) -> Result<T, Failure>.Publisher](result/publisher-swift.struct/reduce(_:_:).md)
- [func removeDuplicates() -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](result/publisher-swift.struct/removeduplicates.md)
- [func removeDuplicates(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](result/publisher-swift.struct/removeduplicates(by:).md)
- [func replaceEmpty(with: Result<Success, Failure>.Publisher.Output) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](result/publisher-swift.struct/replaceempty(with:).md)
- [func replaceError(with: Result<Success, Failure>.Publisher.Output) -> Result<Result<Success, Failure>.Publisher.Output, Never>.Publisher](result/publisher-swift.struct/replaceerror(with:).md)
- [func retry(Int) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](result/publisher-swift.struct/retry(_:).md)
- [func scan<T>(T, (T, Result<Success, Failure>.Publisher.Output) -> T) -> Result<T, Failure>.Publisher](result/publisher-swift.struct/scan(_:_:).md)
- [func setFailureType<E>(to: E.Type) -> Result<Result<Success, Failure>.Publisher.Output, E>.Publisher](result/publisher-swift.struct/setfailuretype(to:).md)
- [func tryAllSatisfy((Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](result/publisher-swift.struct/tryallsatisfy(_:).md)
- [func tryContains(where: (Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](result/publisher-swift.struct/trycontains(where:).md)
- [func tryMap<T>((Result<Success, Failure>.Publisher.Output) throws -> T) -> Result<T, any Error>.Publisher](result/publisher-swift.struct/trymap(_:).md)
- [func tryMax(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, any Error>.Publisher](result/publisher-swift.struct/trymax(by:).md)
- [func tryMin(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, any Error>.Publisher](result/publisher-swift.struct/trymin(by:).md)
- [func tryReduce<T>(T, (T, Result<Success, Failure>.Publisher.Output) throws -> T) -> Result<T, any Error>.Publisher](result/publisher-swift.struct/tryreduce(_:_:).md)
- [func tryRemoveDuplicates(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, any Error>.Publisher](result/publisher-swift.struct/tryremoveduplicates(by:).md)
- [func tryScan<T>(T, (T, Result<Success, Failure>.Publisher.Output) throws -> T) -> Result<T, any Error>.Publisher](result/publisher-swift.struct/tryscan(_:_:).md)
### Default Implementations
- [Equatable Implementations](result/publisher-swift.struct/equatable-implementations.md)
- [Publisher Implementations](result/publisher-swift.struct/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Publisher](../Combine/Publisher.md)

## See Also

- [var publisher: Result<Success, Failure>.Publisher](result/publisher-swift.property.md)
  A Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct)*