# Publishers.TryComparison

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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

### Creating a try-comparison publisher
- [init(upstream: Upstream, areInIncreasingOrder: (Upstream.Output, Upstream.Output) throws -> Bool)](./trycomparison/init%28upstream,areinincreasingorder%29.md)
  Creates a publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.
### Declaring supporting types
- [Publishers.TryComparison.Output](./trycomparison/output.md)
  The kind of values published by this publisher.
- [Publishers.TryComparison.Failure](./trycomparison/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./trycomparison/upstream.md)
  The publisher from which this publisher receives its elements.
- [let areInIncreasingOrder: (Upstream.Output, Upstream.Output) throws -> Bool](./trycomparison/areinincreasingorder.md)
  A closure that receives two elements and returns true if they are in increasing order.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Applying mathematical operations on elements
- [Publishers.Count](./count.md)
  A publisher that publishes the number of elements received from the upstream publisher.
- [Publishers.Comparison](./comparison.md)
  A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycomparison)*