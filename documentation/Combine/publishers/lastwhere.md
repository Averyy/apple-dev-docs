# Publishers.LastWhere

**Framework**: Combine  
**Kind**: struct

A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.

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
struct LastWhere<Upstream> where Upstream : Publisher
```

## Topics

### Creating a last-where Publisher
- [init(upstream: Upstream, predicate: (Publishers.LastWhere<Upstream>.Output) -> Bool)](publishers/lastwhere/init(upstream:predicate:).md)
  Creates a publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
### Declaring supporting types
- [Publishers.LastWhere.Output](publishers/lastwhere/output.md)
  The kind of values published by this publisher.
- [Publishers.LastWhere.Failure](publishers/lastwhere/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/lastwhere/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.LastWhere<Upstream>.Output) -> Bool](publishers/lastwhere/predicate.md)
  The closure that determines whether to publish an element.

## Relationships

### Conforms To
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
- [Publishers.TryLastWhere](publishers/trylastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/lastwhere)*