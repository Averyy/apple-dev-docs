# Publishers.Comparison

**Framework**: Combine  
**Kind**: struct

A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.

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
struct Comparison<Upstream> where Upstream : Publisher
```

## Topics

### Creating a comparison publisher
- [init(upstream: Upstream, areInIncreasingOrder: (Upstream.Output, Upstream.Output) -> Bool)](publishers/comparison/init(upstream:areinincreasingorder:).md)
  Creates a publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.
### Declaring supporting types
- [Publishers.Comparison.Output](publishers/comparison/output.md)
  The kind of values published by this publisher.
- [Publishers.Comparison.Failure](publishers/comparison/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/comparison/upstream.md)
  The publisher from which this publisher receives its elements.
- [let areInIncreasingOrder: (Upstream.Output, Upstream.Output) -> Bool](publishers/comparison/areinincreasingorder.md)
  A closure that receives two elements and returns true if they are in increasing order.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Count](publishers/count.md)
  A publisher that publishes the number of elements received from the upstream publisher.
- [Publishers.TryComparison](publishers/trycomparison.md)
  A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/comparison)*