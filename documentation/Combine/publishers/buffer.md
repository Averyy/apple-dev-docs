# Publishers.Buffer

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that buffers elements from an upstream publisher.

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
struct Buffer<Upstream> where Upstream : Publisher
```

## Topics

### Creating a buffer publisher
- [init(upstream: Upstream, size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Publishers.Buffer<Upstream>.Failure>)](./buffer/init%28upstream,size,prefetch,whenfull%29.md)
  Creates a publisher that buffers elements received from an upstream publisher.
### Declaring supporting types
- [Publishers.Buffer.Output](./buffer/output.md)
  The kind of values published by this publisher.
- [Publishers.Buffer.Failure](./buffer/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./buffer/upstream.md)
  The publisher from which this publisher receives elements.
- [let size: Int](./buffer/size.md)
  The maximum number of elements to store.
- [let prefetch: Publishers.PrefetchStrategy](./buffer/prefetch.md)
  The strategy for initially populating the buffer.
- [let whenFull: Publishers.BufferingStrategy<Publishers.Buffer<Upstream>.Failure>](./buffer/whenfull.md)
  The action to take when the buffer becomes full.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Buffering elements
- [Publishers.BufferingStrategy](./bufferingstrategy.md)
  A strategy that handles exhaustion of a buffer’s capacity.
- [Publishers.PrefetchStrategy](./prefetchstrategy.md)
  A strategy for filling a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/buffer)*