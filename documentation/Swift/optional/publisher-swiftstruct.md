# Optional.Publisher

**Framework**: Swift  
**Kind**: struct

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

In contrast with the [`Just`](https://developer.apple.com/documentation/Combine/Just) publisher, which always produces a single value, this publisher might not send any values and instead finish normally, if [`output`](optional/publisher-swift.struct/output-swift.property.md) is `nil`.

## Topics

### Declaring Publisher Topography
- [Optional.Publisher.Output](optional/publisher-swift.struct/output-swift.typealias.md)
  The kind of value published by this publisher.
- [Optional.Publisher.Failure](optional/publisher-swift.struct/failure.md)
  The kind of error this publisher might publish.
### Creating an Optional Publisher
- [init(Optional<Wrapped>.Publisher.Output?)](optional/publisher-swift.struct/init(_:).md)
  Creates a publisher to emit the value of the optional, or to finish immediately if the optional doesn’t have a value.
### Inpsecting Publisher Properties
- [let output: Optional<Wrapped>.Publisher.Output?](optional/publisher-swift.struct/output-swift.property.md)
  The output to deliver to each subscriber.
### Working with Subscribers
- [func receive<S>(subscriber: S)](optional/publisher-swift.struct/receive(subscriber:).md)
  Implements the Publisher protocol by accepting the subscriber and immediately publishing the optional’s value if it has one, or finishing normally if it doesn’t.
### Instance Methods
- [func allSatisfy((Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Bool>.Publisher](optional/publisher-swift.struct/allsatisfy(_:).md)
- [func collect() -> Optional<[Optional<Wrapped>.Publisher.Output]>.Publisher](optional/publisher-swift.struct/collect.md)
- [func compactMap<T>((Optional<Wrapped>.Publisher.Output) -> T?) -> Optional<T>.Publisher](optional/publisher-swift.struct/compactmap(_:).md)
- [func contains(Optional<Wrapped>.Publisher.Output) -> Optional<Bool>.Publisher](optional/publisher-swift.struct/contains(_:).md)
- [func contains(where: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Bool>.Publisher](optional/publisher-swift.struct/contains(where:).md)
- [func count() -> Optional<Int>.Publisher](optional/publisher-swift.struct/count.md)
- [func drop(while: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/drop(while:).md)
- [func dropFirst(Int) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/dropfirst(_:).md)
- [func filter((Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/filter(_:).md)
- [func first() -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/first.md)
- [func first(where: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/first(where:).md)
- [func ignoreOutput() -> Empty<Optional<Wrapped>.Publisher.Output, Optional<Wrapped>.Publisher.Failure>](optional/publisher-swift.struct/ignoreoutput.md)
- [func last() -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/last.md)
- [func last(where: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/last(where:).md)
- [func map<T>((Optional<Wrapped>.Publisher.Output) -> T) -> Optional<T>.Publisher](optional/publisher-swift.struct/map(_:).md)
- [func max() -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/max.md)
- [func max(by: (Optional<Wrapped>.Publisher.Output, Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/max(by:).md)
- [func min() -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/min.md)
- [func min(by: (Optional<Wrapped>.Publisher.Output, Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/min(by:).md)
- [func output(at: Int) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/output(at:).md)
- [func output<R>(in: R) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/output(in:).md)
- [func prefix(Int) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/prefix(_:).md)
- [func prefix(while: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/prefix(while:).md)
- [func reduce<T>(T, (T, Optional<Wrapped>.Publisher.Output) -> T) -> Optional<T>.Publisher](optional/publisher-swift.struct/reduce(_:_:).md)
- [func removeDuplicates() -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/removeduplicates.md)
- [func removeDuplicates(by: (Optional<Wrapped>.Publisher.Output, Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/removeduplicates(by:).md)
- [func replaceEmpty(with: Optional<Wrapped>.Publisher.Output) -> Just<Wrapped>](optional/publisher-swift.struct/replaceempty(with:).md)
- [func replaceError(with: Optional<Wrapped>.Publisher.Output) -> Optional<Optional<Wrapped>.Publisher.Output>.Publisher](optional/publisher-swift.struct/replaceerror(with:).md)
- [func retry(Int) -> Optional<Wrapped>.Publisher](optional/publisher-swift.struct/retry(_:).md)
- [func scan<T>(T, (T, Optional<Wrapped>.Publisher.Output) -> T) -> Optional<T>.Publisher](optional/publisher-swift.struct/scan(_:_:).md)
### Default Implementations
- [Equatable Implementations](optional/publisher-swift.struct/equatable-implementations.md)
- [Publisher Implementations](optional/publisher-swift.struct/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Publisher](../Combine/Publisher.md)

## See Also

- [var publisher: Optional<Wrapped>.Publisher](optional/publisher-swift.property.md)
  A Combine publisher that publishes this instance’s value to each subscriber exactly once, if it has any value at all.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct)*