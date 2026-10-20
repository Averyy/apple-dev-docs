# Optional.Publisher

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

The type of a Combine publisher that publishes the value of a Swift optional instance to each subscriber exactly once, if the instance has any value at all.

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

In contrast with the [`Just`](../../Combine/just.md) publisher, which always produces a single value, this publisher might not send any values and instead finish normally, if [`output`](./publisher-swift.struct/output-swift.property.md) is `nil`.

## Topics

### Declaring Publisher Topography
- [Optional.Publisher.Output](./publisher-swift.struct/output-swift.typealias.md)
  The kind of value published by this publisher.
- [Optional.Publisher.Failure](./publisher-swift.struct/failure.md)
  The kind of error this publisher might publish.
### Creating an Optional Publisher
- [init(Optional<Wrapped>.Publisher.Output?)](./publisher-swift.struct/init%28_%29.md)
  Creates a publisher to emit the value of the optional, or to finish immediately if the optional doesn’t have a value.
### Inpsecting Publisher Properties
- [let output: Optional<Wrapped>.Publisher.Output?](./publisher-swift.struct/output-swift.property.md)
  The output to deliver to each subscriber.
### Working with Subscribers
- [func receive<S>(subscriber: S)](./publisher-swift.struct/receive%28subscriber%29.md)
  Implements the Publisher protocol by accepting the subscriber and immediately publishing the optional’s value if it has one, or finishing normally if it doesn’t.
### Instance Methods
- [func allSatisfy((Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Bool>.Publisher](./publisher-swift.struct/allsatisfy%28_%29.md)
- [func collect() -> Optional<[Optional<Wrapped>.Publisher.Output]>.Publisher](./publisher-swift.struct/collect%28%29.md)
- [func compactMap<T>((Optional<Wrapped>.Publisher.Output) -> T?) -> Optional<T>.Publisher](./publisher-swift.struct/compactmap%28_%29.md)
- [func contains(Optional<Wrapped>.Publisher.Output) -> Optional<Bool>.Publisher](./publisher-swift.struct/contains%28_%29.md)
- [func contains(where: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Bool>.Publisher](./publisher-swift.struct/contains%28where%29.md)
- [func count() -> Optional<Int>.Publisher](./publisher-swift.struct/count%28%29.md)
- [func drop(while: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/drop%28while%29.md)
- [func dropFirst(Int) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/dropfirst%28_%29.md)
- [func filter((Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/filter%28_%29.md)
- [func first() -> Optional<Wrapped>.Publisher](./publisher-swift.struct/first%28%29.md)
- [func first(where: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/first%28where%29.md)
- [func ignoreOutput() -> Empty<Optional<Wrapped>.Publisher.Output, Optional<Wrapped>.Publisher.Failure>](./publisher-swift.struct/ignoreoutput%28%29.md)
- [func last() -> Optional<Wrapped>.Publisher](./publisher-swift.struct/last%28%29.md)
- [func last(where: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/last%28where%29.md)
- [func map<T>((Optional<Wrapped>.Publisher.Output) -> T) -> Optional<T>.Publisher](./publisher-swift.struct/map%28_%29.md)
- [func max() -> Optional<Wrapped>.Publisher](./publisher-swift.struct/max%28%29.md)
- [func max(by: (Optional<Wrapped>.Publisher.Output, Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/max%28by%29.md)
- [func min() -> Optional<Wrapped>.Publisher](./publisher-swift.struct/min%28%29.md)
- [func min(by: (Optional<Wrapped>.Publisher.Output, Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/min%28by%29.md)
- [func output(at: Int) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/output%28at%29.md)
- [func output<R>(in: R) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/output%28in%29.md)
- [func prefix(Int) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/prefix%28_%29.md)
- [func prefix(while: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/prefix%28while%29.md)
- [func reduce<T>(T, (T, Optional<Wrapped>.Publisher.Output) -> T) -> Optional<T>.Publisher](./publisher-swift.struct/reduce%28_,_%29.md)
- [func removeDuplicates() -> Optional<Wrapped>.Publisher](./publisher-swift.struct/removeduplicates%28%29.md)
- [func removeDuplicates(by: (Optional<Wrapped>.Publisher.Output, Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/removeduplicates%28by%29.md)
- [func replaceEmpty(with: Optional<Wrapped>.Publisher.Output) -> Just<Wrapped>](./publisher-swift.struct/replaceempty%28with%29.md)
- [func replaceError(with: Optional<Wrapped>.Publisher.Output) -> Optional<Optional<Wrapped>.Publisher.Output>.Publisher](./publisher-swift.struct/replaceerror%28with%29.md)
- [func retry(Int) -> Optional<Wrapped>.Publisher](./publisher-swift.struct/retry%28_%29.md)
- [func scan<T>(T, (T, Optional<Wrapped>.Publisher.Output) -> T) -> Optional<T>.Publisher](./publisher-swift.struct/scan%28_,_%29.md)

## Relationships

### Conforms To
- [Equatable](../equatable.md)
- [Publisher](../../Combine/publisher.md)

## See Also

### Publishing an Optional
- [var publisher: Optional<Wrapped>.Publisher](./publisher-swift.property.md)
  A Combine publisher that publishes this instance’s value to each subscriber exactly once, if it has any value at all.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct)*