# Publishers.PrefetchStrategy

**Framework**: Combine  
**Kind**: enum  
**Role**: Enumeration

A strategy for filling a buffer.

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
enum PrefetchStrategy
```

## Topics

### Prefetching strategies
- [Publishers.PrefetchStrategy.byRequest](./prefetchstrategy/byrequest.md)
  A strategy that avoids prefetching and instead performs requests on demand.
- [Publishers.PrefetchStrategy.keepFull](./prefetchstrategy/keepfull.md)
  A strategy to fill the buffer at subscription time, and keep it full thereafter.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Buffering elements
- [func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>](../publisher/buffer%28size,prefetch,whenfull%29.md)
  Buffers elements received from an upstream publisher.
- [Publishers.BufferingStrategy](./bufferingstrategy.md)
  A strategy that handles exhaustion of a buffer’s capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/prefetchstrategy)*