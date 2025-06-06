# Publishers.TryFirstWhere

**Framework**: Combine  
**Kind**: struct

A publisher that only publishes the first element of a stream to satisfy a throwing predicate closure.

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
struct TryFirstWhere<Upstream> where Upstream : Publisher
```

## Topics

### Creating a Try First Where Publisher
- [init(upstream: Upstream, predicate: (Publishers.TryFirstWhere<Upstream>.Output) throws -> Bool)](publishers/tryfirstwhere/init(upstream:predicate:).md)
### Declaring Publisher Topography
- [Publishers.TryFirstWhere.Output](publishers/tryfirstwhere/output.md)
  The kind of values published by this publisher.
- [Publishers.TryFirstWhere.Failure](publishers/tryfirstwhere/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/tryfirstwhere/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.TryFirstWhere<Upstream>.Output) throws -> Bool](publishers/tryfirstwhere/predicate.md)
  The error-throwing closure that determines whether to publish an element.
### Applying Operators
- [Publisher Operators](publishers-tryfirstwhere-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/tryfirstwhere/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.First](publishers/first.md)
  A publisher that publishes the first element of a stream, then finishes.
- [Publishers.FirstWhere](publishers/firstwhere.md)
  A publisher that only publishes the first element of a stream to satisfy a predicate closure.
- [Publishers.Last](publishers/last.md)
  A publisher that waits until after the stream finishes, and then publishes the last element of the stream.
- [Publishers.LastWhere](publishers/lastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [Publishers.TryLastWhere](publishers/trylastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryfirstwhere)*