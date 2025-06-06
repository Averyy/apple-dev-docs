# Publishers.BufferingStrategy

**Framework**: Combine  
**Kind**: enum

A strategy that handles exhaustion of a buffer’s capacity.

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
enum BufferingStrategy<Failure> where Failure : Error
```

## Topics

### Buffering Strategies
- [Publishers.BufferingStrategy.dropNewest](publishers/bufferingstrategy/dropnewest.md)
  When the buffer is full, discard the newly received element.
- [Publishers.BufferingStrategy.dropOldest](publishers/bufferingstrategy/dropoldest.md)
  When the buffer is full, discard the oldest element in the buffer.
- [Publishers.BufferingStrategy.customError(_:)](publishers/bufferingstrategy/customerror(_:).md)
  When the buffer is full, execute the closure to provide a custom error.

## See Also

- [func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>](publisher/buffer(size:prefetch:whenfull:).md)
  Buffers elements received from an upstream publisher.
- [Publishers.PrefetchStrategy](publishers/prefetchstrategy.md)
  A strategy for filling a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/bufferingstrategy)*