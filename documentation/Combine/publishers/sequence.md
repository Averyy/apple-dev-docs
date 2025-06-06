# Publishers.Sequence

**Framework**: Combine  
**Kind**: struct

A publisher that publishes a given sequence of elements.

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
struct Sequence<Elements, Failure> where Elements : Sequence, Failure : Error
```

#### Overview

When the publisher exhausts the elements in the sequence, the next request causes the publisher to finish.

## Topics

### Creating a Sequence Publisher
- [init(sequence: Elements)](publishers/sequence/init(sequence:).md)
  Creates a publisher for a sequence of elements.
### Declaring Publisher Topography
- [Publishers.Sequence.Output](publishers/sequence/output.md)
  The kind of values published by this publisher.
### Inspecting Publisher Properties
- [let sequence: Elements](publishers/sequence/sequence.md)
  The sequence of elements to publish.
### Comparing Publishers
- [static func == (Publishers.Sequence<Elements, Failure>, Publishers.Sequence<Elements, Failure>) -> Bool](publishers/sequence/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](publishers/sequence/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](publishers-sequence-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Instance Methods
- [func allSatisfy((Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](publishers/sequence/allsatisfy(_:).md)
- [func append(Publishers.Sequence<Elements, Failure>.Output...) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/append(_:)-2knh4.md)
- [func append(Publishers.Sequence<Elements, Failure>) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/append(_:)-3dj6k.md)
- [func append<S>(S) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/append(_:)-45rm8.md)
- [func collect() -> Result<[Publishers.Sequence<Elements, Failure>.Output], Failure>.Publisher](publishers/sequence/collect.md)
- [func compactMap<T>((Publishers.Sequence<Elements, Failure>.Output) -> T?) -> Publishers.Sequence<[T], Failure>](publishers/sequence/compactmap(_:).md)
- [func contains(Elements.Element) -> Result<Bool, Failure>.Publisher](publishers/sequence/contains(_:).md)
- [func contains(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](publishers/sequence/contains(where:).md)
- [func count() -> Result<Int, Failure>.Publisher](publishers/sequence/count-5hb52.md)
- [func count() -> Just<Int>](publishers/sequence/count-5rrw2.md)
- [func count() -> Result<Int, Failure>.Publisher](publishers/sequence/count-b8ct.md)
- [func drop(while: (Elements.Element) -> Bool) -> Publishers.Sequence<DropWhileSequence<Elements>, Failure>](publishers/sequence/drop(while:).md)
- [func dropFirst(Int) -> Publishers.Sequence<DropFirstSequence<Elements>, Failure>](publishers/sequence/dropfirst(_:).md)
- [func filter((Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/filter(_:).md)
- [func first() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/first.md)
- [func first(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/first(where:).md)
- [func ignoreOutput() -> Empty<Publishers.Sequence<Elements, Failure>.Output, Failure>](publishers/sequence/ignoreoutput.md)
- [func last() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/last.md)
- [func last(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/last(where:).md)
- [func map<T>((Elements.Element) -> T) -> Publishers.Sequence<[T], Failure>](publishers/sequence/map(_:).md)
- [func max() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/max.md)
- [func max(by: (Publishers.Sequence<Elements, Failure>.Output, Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/max(by:).md)
- [func min() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/min.md)
- [func min(by: (Publishers.Sequence<Elements, Failure>.Output, Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/min(by:).md)
- [func output(at: Elements.Index) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/output(at:)-3r7zo.md)
- [func output(at: Elements.Index) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](publishers/sequence/output(at:)-9kto7.md)
- [func output(in: Range<Elements.Index>) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/output(in:)-6g2zc.md)
- [func output(in: Range<Elements.Index>) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/output(in:)-8l6yw.md)
- [func prefix(Int) -> Publishers.Sequence<PrefixSequence<Elements>, Failure>](publishers/sequence/prefix(_:).md)
- [func prefix(while: (Elements.Element) -> Bool) -> Publishers.Sequence<[Elements.Element], Failure>](publishers/sequence/prefix(while:).md)
- [func prepend<S>(S) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/prepend(_:)-1r564.md)
- [func prepend(Publishers.Sequence<Elements, Failure>.Output...) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/prepend(_:)-2ros1.md)
- [func prepend(Publishers.Sequence<Elements, Failure>) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/prepend(_:)-71f7p.md)
- [func reduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Result<T, Failure>.Publisher](publishers/sequence/reduce(_:_:).md)
- [func removeDuplicates() -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/removeduplicates.md)
- [func replaceNil<T>(with: T) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/replacenil(with:).md)
- [func scan<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Publishers.Sequence<[T], Failure>](publishers/sequence/scan(_:_:).md)
- [func setFailureType<E>(to: E.Type) -> Publishers.Sequence<Elements, E>](publishers/sequence/setfailuretype(to:).md)
- [func tryAllSatisfy((Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](publishers/sequence/tryallsatisfy(_:).md)
- [func tryContains(where: (Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](publishers/sequence/trycontains(where:).md)
- [func tryReduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) throws -> T) -> Result<T, any Error>.Publisher](publishers/sequence/tryreduce(_:_:).md)
### Default Implementations
- [Equatable Implementations](publishers/sequence/equatable-implementations.md)
- [Publisher Implementations](publishers/sequence/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.Catch](publishers/catch.md)
  A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence)*