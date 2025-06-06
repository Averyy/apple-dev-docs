# Publishers.Last

**Framework**: Combine  
**Kind**: struct

A publisher that waits until after the stream finishes, and then publishes the last element of the stream.

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
struct Last<Upstream> where Upstream : Publisher
```

## Topics

### Creating a Last Publisher
- [init(upstream: Upstream)](publishers/last/init(upstream:).md)
  Creates a publisher that waits until after the stream finishes and then publishes the last element of the stream.
### Declaring Publisher Topography
- [Publishers.Last.Output](publishers/last/output.md)
  The kind of values published by this publisher.
- [Publishers.Last.Failure](publishers/last/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/last/upstream.md)
  The publisher from which this publisher receives elements.
### Comparing Publishers
- [static func == (Publishers.Last<Upstream>, Publishers.Last<Upstream>) -> Bool](publishers/last/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](publishers/last/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](publishers-last-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](publishers/last/equatable-implementations.md)
- [Publisher Implementations](publishers/last/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.First](publishers/first.md)
  A publisher that publishes the first element of a stream, then finishes.
- [Publishers.FirstWhere](publishers/firstwhere.md)
  A publisher that only publishes the first element of a stream to satisfy a predicate closure.
- [Publishers.TryFirstWhere](publishers/tryfirstwhere.md)
  A publisher that only publishes the first element of a stream to satisfy a throwing predicate closure.
- [Publishers.LastWhere](publishers/lastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [Publishers.TryLastWhere](publishers/trylastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/last)*