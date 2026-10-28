# Result.Publisher

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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

Available when `Failure` conforms to `Error`.

## Overview

If the result is `Swift/Result/success`, then the publisher waits until it receives a request for at least one value, then sends the output to all subscribers and finishes normally. If the result is `/Swift/Result/failure`, then the publisher sends the failure immediately upon subscription. This latter behavior is a contrast with [`Just`](../../Combine/just.md), which always publishes a single value.

## Topics

### Creating a Result Publisher
- [init(Result<Result<Success, Failure>.Publisher.Output, Failure>)](./publisher-swift.struct/init%28_%29-516t.md)
  Creates a publisher that delivers the specified result.
- [init(Failure)](./publisher-swift.struct/init%28_%29-69fv4.md)
  Creates a publisher that immediately terminates upon subscription with the given failure.
- [init(Result<Success, Failure>.Publisher.Output)](./publisher-swift.struct/init%28_%29-7t2tt.md)
  Creates a publisher that sends the specified output to all subscribers and finishes normally.
### Inspecting Publisher Properties
- [let result: Result<Result<Success, Failure>.Publisher.Output, Failure>](./publisher-swift.struct/result.md)
  The result to deliver to each subscriber.
### Instance Methods
- [func allSatisfy((Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Bool, Failure>.Publisher](./publisher-swift.struct/allsatisfy%28_%29.md)
- [func collect() -> Result<[Result<Success, Failure>.Publisher.Output], Failure>.Publisher](./publisher-swift.struct/collect%28%29.md)
- [func contains(Result<Success, Failure>.Publisher.Output) -> Result<Bool, Failure>.Publisher](./publisher-swift.struct/contains%28_%29.md)
- [func contains(where: (Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Bool, Failure>.Publisher](./publisher-swift.struct/contains%28where%29.md)
- [func count() -> Result<Int, Failure>.Publisher](./publisher-swift.struct/count%28%29.md)
- [func first() -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](./publisher-swift.struct/first%28%29.md)
- [func ignoreOutput() -> Empty<Result<Success, Failure>.Publisher.Output, Failure>](./publisher-swift.struct/ignoreoutput%28%29.md)
- [func last() -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](./publisher-swift.struct/last%28%29.md)
- [func map<T>((Result<Success, Failure>.Publisher.Output) -> T) -> Result<T, Failure>.Publisher](./publisher-swift.struct/map%28_%29.md)
- [func mapError<E>((Failure) -> E) -> Result<Result<Success, Failure>.Publisher.Output, E>.Publisher](./publisher-swift.struct/maperror%28_%29.md)
- [func max() -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](./publisher-swift.struct/max%28%29.md)
- [func max(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](./publisher-swift.struct/max%28by%29.md)
- [func min() -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](./publisher-swift.struct/min%28%29.md)
- [func min(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](./publisher-swift.struct/min%28by%29.md)
- [func reduce<T>(T, (T, Result<Success, Failure>.Publisher.Output) -> T) -> Result<T, Failure>.Publisher](./publisher-swift.struct/reduce%28_,_%29.md)
- [func removeDuplicates() -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](./publisher-swift.struct/removeduplicates%28%29.md)
- [func removeDuplicates(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](./publisher-swift.struct/removeduplicates%28by%29.md)
- [func replaceEmpty(with: Result<Success, Failure>.Publisher.Output) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](./publisher-swift.struct/replaceempty%28with%29.md)
- [func replaceError(with: Result<Success, Failure>.Publisher.Output) -> Result<Result<Success, Failure>.Publisher.Output, Never>.Publisher](./publisher-swift.struct/replaceerror%28with%29.md)
- [func retry(Int) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher](./publisher-swift.struct/retry%28_%29.md)
- [func scan<T>(T, (T, Result<Success, Failure>.Publisher.Output) -> T) -> Result<T, Failure>.Publisher](./publisher-swift.struct/scan%28_,_%29.md)
- [func setFailureType<E>(to: E.Type) -> Result<Result<Success, Failure>.Publisher.Output, E>.Publisher](./publisher-swift.struct/setfailuretype%28to%29.md)
- [func tryAllSatisfy((Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](./publisher-swift.struct/tryallsatisfy%28_%29.md)
- [func tryContains(where: (Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](./publisher-swift.struct/trycontains%28where%29.md)
- [func tryMap<T>((Result<Success, Failure>.Publisher.Output) throws -> T) -> Result<T, any Error>.Publisher](./publisher-swift.struct/trymap%28_%29.md)
- [func tryMax(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, any Error>.Publisher](./publisher-swift.struct/trymax%28by%29.md)
- [func tryMin(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, any Error>.Publisher](./publisher-swift.struct/trymin%28by%29.md)
- [func tryReduce<T>(T, (T, Result<Success, Failure>.Publisher.Output) throws -> T) -> Result<T, any Error>.Publisher](./publisher-swift.struct/tryreduce%28_,_%29.md)
- [func tryRemoveDuplicates(by: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, any Error>.Publisher](./publisher-swift.struct/tryremoveduplicates%28by%29.md)
- [func tryScan<T>(T, (T, Result<Success, Failure>.Publisher.Output) throws -> T) -> Result<T, any Error>.Publisher](./publisher-swift.struct/tryscan%28_,_%29.md)

## Relationships

### Conforms To
- [Equatable](../equatable.md)
- [Publisher](../../Combine/publisher.md)

## See Also

### Publishing a Result
- [var publisher: Result<Success, Failure>.Publisher](./publisher-swift.property.md)
  A Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct)*