# Publishers.Count

**Framework**: Combine  
**Kind**: struct

A publisher that publishes the number of elements received from the upstream publisher.

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
struct Count<Upstream> where Upstream : Publisher
```

## Topics

### Creating a count Publisher
- [init(upstream: Upstream)](publishers/count/init(upstream:).md)
  Creates a publisher that publishes the number of elements received from the upstream publisher.
### Declaring supporting types
- [Publishers.Count.Output](publishers/count/output.md)
  The kind of values published by this publisher.
- [Publishers.Count.Failure](publishers/count/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/count/upstream.md)
  The publisher from which this publisher receives elements.
### Comparing publishers
- [static func == (Publishers.Count<Upstream>, Publishers.Count<Upstream>) -> Bool](publishers/count/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent. /// - Parameters:
### Default Implementations
- [Equatable Implementations](publishers/count/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.Comparison](publishers/comparison.md)
  A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.
- [Publishers.TryComparison](publishers/trycomparison.md)
  A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/count)*