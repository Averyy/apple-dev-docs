# Publishers.TryLastWhere

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.

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
struct TryLastWhere<Upstream> where Upstream : Publisher
```

## Topics

### Creating a try-last-where publisher
- [init(upstream: Upstream, predicate: (Publishers.TryLastWhere<Upstream>.Output) throws -> Bool)](./trylastwhere/init%28upstream,predicate%29.md)
  Creates a publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.
### Declaring supporting types
- [Publishers.TryLastWhere.Output](./trylastwhere/output.md)
  The kind of values published by this publisher.
- [Publishers.TryLastWhere.Failure](./trylastwhere/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./trylastwhere/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.TryLastWhere<Upstream>.Output) throws -> Bool](./trylastwhere/predicate.md)
  The error-throwing closure that determines whether to publish an element.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Selecting specific elements
- [Publishers.First](./first.md)
  A publisher that publishes the first element of a stream, then finishes.
- [Publishers.FirstWhere](./firstwhere.md)
  A publisher that only publishes the first element of a stream to satisfy a predicate closure.
- [Publishers.TryFirstWhere](./tryfirstwhere.md)
  A publisher that only publishes the first element of a stream to satisfy a throwing predicate closure.
- [Publishers.Last](./last.md)
  A publisher that waits until after the stream finishes, and then publishes the last element of the stream.
- [Publishers.LastWhere](./lastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [Publishers.Output](./output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trylastwhere)*