# Publishers.Output

**Framework**: Combine  
**Kind**: struct

A publisher that publishes elements specified by a range in the sequence of published elements.

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
struct Output<Upstream> where Upstream : Publisher
```

## Topics

### Creating an output publisher
- [init(upstream: Upstream, range: CountableRange<Int>)](publishers/output/init(upstream:range:).md)
  Creates a publisher that publishes elements specified by a range.
### Declaring supporting types
- [Publishers.Output.Output](publishers/output/output.md)
  The kind of values published by this publisher.
- [Publishers.Output.Failure](publishers/output/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/output/upstream.md)
  The publisher from which this publisher receives its elements.
- [let range: CountableRange<Int>](publishers/output/range.md)
  The range of elements to publish.
### Comparing publishers
- [static func == (Publishers.Output<Upstream>, Publishers.Output<Upstream>) -> Bool](publishers/output/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](publishers/output/equatable-implementations.md)

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
- [Publishers.Last](publishers/last.md)
  A publisher that waits until after the stream finishes, and then publishes the last element of the stream.
- [Publishers.LastWhere](publishers/lastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [Publishers.TryLastWhere](publishers/trylastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/output)*