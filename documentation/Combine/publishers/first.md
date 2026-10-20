# Publishers.First

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that publishes the first element of a stream, then finishes.

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
struct First<Upstream> where Upstream : Publisher
```

## Topics

### Creating a first publisher
- [init(upstream: Upstream)](./first/init%28upstream%29.md)
  Creates a publisher that publishes the first element of a stream, then finishes.
### Declaring supporting types
- [Publishers.First.Output](./first/output.md)
  The kind of values published by this publisher.
- [Publishers.First.Failure](./first/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./first/upstream.md)
  The publisher from which this publisher receives elements.
### Comparing publishers
- [static func == (Publishers.First<Upstream>, Publishers.First<Upstream>) -> Bool](./first/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two first publishers have equal upstream publishers.
### Default Implementations
- [Equatable Implementations](./first/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Selecting specific elements
- [Publishers.FirstWhere](./firstwhere.md)
  A publisher that only publishes the first element of a stream to satisfy a predicate closure.
- [Publishers.TryFirstWhere](./tryfirstwhere.md)
  A publisher that only publishes the first element of a stream to satisfy a throwing predicate closure.
- [Publishers.Last](./last.md)
  A publisher that waits until after the stream finishes, and then publishes the last element of the stream.
- [Publishers.LastWhere](./lastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [Publishers.TryLastWhere](./trylastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.
- [Publishers.Output](./output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/first)*