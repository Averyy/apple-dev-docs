# Publishers.Count

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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
- [init(upstream: Upstream)](./count/init%28upstream%29.md)
  Creates a publisher that publishes the number of elements received from the upstream publisher.
### Declaring supporting types
- [Publishers.Count.Output](./count/output.md)
  The kind of values published by this publisher.
- [Publishers.Count.Failure](./count/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./count/upstream.md)
  The publisher from which this publisher receives elements.
### Comparing publishers
- [static func == (Publishers.Count<Upstream>, Publishers.Count<Upstream>) -> Bool](./count/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent. /// - Parameters:
### Default Implementations
- [Equatable Implementations](./count/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Applying mathematical operations on elements
- [Publishers.Comparison](./comparison.md)
  A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.
- [Publishers.TryComparison](./trycomparison.md)
  A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/count)*