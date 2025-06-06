# Publishers.ReplaceEmpty

**Framework**: Combine  
**Kind**: struct

A publisher that replaces an empty stream with a provided element.

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
struct ReplaceEmpty<Upstream> where Upstream : Publisher
```

## Topics

### Creating a Replace Empty Publisher
- [init(upstream: Upstream, output: Publishers.ReplaceEmpty<Upstream>.Output)](publishers/replaceempty/init(upstream:output:).md)
  Creates a publisher that replaces an empty stream with a provided element.
### Declaring Publisher Topography
- [Publishers.ReplaceEmpty.Output](publishers/replaceempty/output-swift.typealias.md)
  The kind of values published by this publisher.
- [Publishers.ReplaceEmpty.Output](publishers/replaceempty/output-swift.typealias.md)
  The kind of values published by this publisher.
- [Publishers.ReplaceEmpty.Failure](publishers/replaceempty/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/replaceempty/upstream.md)
  The publisher from which this publisher receives elements.
- [let output: Publishers.ReplaceEmpty<Upstream>.Output](publishers/replaceempty/output-swift.property.md)
  The element to deliver when the upstream publisher finishes without delivering any elements.
- [let output: Publishers.ReplaceEmpty<Upstream>.Output](publishers/replaceempty/output-swift.property.md)
  The element to deliver when the upstream publisher finishes without delivering any elements.
### Comparing Publishers
- [static func == (Publishers.ReplaceEmpty<Upstream>, Publishers.ReplaceEmpty<Upstream>) -> Bool](publishers/replaceempty/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](publishers/replaceempty/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](publishers-replaceempty-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](publishers/replaceempty/equatable-implementations.md)
- [Publisher Implementations](publishers/replaceempty/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.Filter](publishers/filter.md)
  A publisher that republishes all elements that match a provided closure.
- [Publishers.TryFilter](publishers/tryfilter.md)
  A publisher that republishes all elements that match a provided error-throwing closure.
- [Publishers.CompactMap](publishers/compactmap.md)
  A publisher that republishes all non-nil results of calling a closure with each received element.
- [Publishers.TryCompactMap](publishers/trycompactmap.md)
  A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [Publishers.RemoveDuplicates](publishers/removeduplicates.md)
  A publisher that publishes only elements that don’t match the previous element.
- [Publishers.TryRemoveDuplicates](publishers/tryremoveduplicates.md)
  A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [Publishers.ReplaceError](publishers/replaceerror.md)
  A publisher that replaces any errors in the stream with a provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/replaceempty)*