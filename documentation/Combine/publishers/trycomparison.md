# Publishers.TryComparison

**Framework**: Combine  
**Kind**: struct

A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.

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
struct TryComparison<Upstream> where Upstream : Publisher
```

## Topics

### Creating a Try Comparison Publisher
- [init(upstream: Upstream, areInIncreasingOrder: (Upstream.Output, Upstream.Output) throws -> Bool)](publishers/trycomparison/init(upstream:areinincreasingorder:).md)
  Creates a publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.
### Declaring Publisher Topography
- [Publishers.TryComparison.Output](publishers/trycomparison/output.md)
  The kind of values published by this publisher.
- [Publishers.TryComparison.Failure](publishers/trycomparison/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/trycomparison/upstream.md)
  The publisher from which this publisher receives its elements.
- [let areInIncreasingOrder: (Upstream.Output, Upstream.Output) throws -> Bool](publishers/trycomparison/areinincreasingorder.md)
  A closure that receives two elements and returns true if they are in increasing order.
### Applying Operators
- [Publisher Operators](publishers-trycomparison-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/trycomparison/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Count](publishers/count.md)
  A publisher that publishes the number of elements received from the upstream publisher.
- [Publishers.Comparison](publishers/comparison.md)
  A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycomparison)*