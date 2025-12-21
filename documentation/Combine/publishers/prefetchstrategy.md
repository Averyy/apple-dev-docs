# Publishers.PrefetchStrategy

**Framework**: Combine  
**Kind**: enum

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
- [Publishers.PrefetchStrategy.byRequest](publishers/prefetchstrategy/byrequest.md)
  A strategy that avoids prefetching and instead performs requests on demand.
- [Publishers.PrefetchStrategy.keepFull](publishers/prefetchstrategy/keepfull.md)
  A strategy to fill the buffer at subscription time, and keep it full thereafter.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>](publisher/buffer(size:prefetch:whenfull:).md)
  Buffers elements received from an upstream publisher.
- [Publishers.BufferingStrategy](publishers/bufferingstrategy.md)
  A strategy that handles exhaustion of a buffer’s capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/prefetchstrategy)*