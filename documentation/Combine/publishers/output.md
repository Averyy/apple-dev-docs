# Publishers.Output

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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
- [init(upstream: Upstream, range: CountableRange<Int>)](./output/init%28upstream,range%29.md)
  Creates a publisher that publishes elements specified by a range.
### Declaring supporting types
- [Publishers.Output.Output](./output/output.md)
  The kind of values published by this publisher.
- [Publishers.Output.Failure](./output/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./output/upstream.md)
  The publisher from which this publisher receives its elements.
- [let range: CountableRange<Int>](./output/range.md)
  The range of elements to publish.
### Comparing publishers
- [static func == (Publishers.Output<Upstream>, Publishers.Output<Upstream>) -> Bool](./output/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./output/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
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
- [Publishers.TryLastWhere](./trylastwhere.md)
  A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/output)*