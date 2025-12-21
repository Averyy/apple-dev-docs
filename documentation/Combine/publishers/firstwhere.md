# Publishers.FirstWhere

**Framework**: Combine  
**Kind**: struct

A publisher that only publishes the first element of a stream to satisfy a predicate closure.

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
struct FirstWhere<Upstream> where Upstream : Publisher
```

## Topics

### Creating a first-where publisher
- [init(upstream: Upstream, predicate: (Publishers.FirstWhere<Upstream>.Output) -> Bool)](publishers/firstwhere/init(upstream:predicate:).md)
### Declaring supporting types
- [Publishers.FirstWhere.Output](publishers/firstwhere/output.md)
  The kind of values published by this publisher.
- [Publishers.FirstWhere.Failure](publishers/firstwhere/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/firstwhere/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.FirstWhere<Upstream>.Output) -> Bool](publishers/firstwhere/predicate.md)
  The closure that determines whether to publish an element.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.First](publishers/first.md)
  A publisher that publishes the first element of a stream, then finishes.
- [Publishers.TryFirstWhere](publishers/tryfirstwhere.md)
  A publisher that only publishes the first element of a stream to satisfy a throwing predicate closure.
- [Publishers.Last](publishers/last.md)
  A publisher that waits until after the stream finishes, and then publishes the last element of the stream.
- [Publishers.LastWhere](publishers/lastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [Publishers.TryLastWhere](publishers/trylastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/firstwhere)*