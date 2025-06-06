# Publishers.Buffer

**Framework**: Combine  
**Kind**: struct

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

### Creating a Buffer Publisher
- [init(upstream: Upstream, size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Publishers.Buffer<Upstream>.Failure>)](publishers/buffer/init(upstream:size:prefetch:whenfull:).md)
  Creates a publisher that buffers elements received from an upstream publisher.
### Declaring Publisher Topography
- [Publishers.Buffer.Output](publishers/buffer/output.md)
  The kind of values published by this publisher.
- [Publishers.Buffer.Failure](publishers/buffer/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/buffer/upstream.md)
  The publisher from which this publisher receives elements.
- [let size: Int](publishers/buffer/size.md)
  The maximum number of elements to store.
- [let prefetch: Publishers.PrefetchStrategy](publishers/buffer/prefetch.md)
  The strategy for initially populating the buffer.
- [let whenFull: Publishers.BufferingStrategy<Publishers.Buffer<Upstream>.Failure>](publishers/buffer/whenfull.md)
  The action to take when the buffer becomes full.
### Applying Operators
- [Publisher Operators](publishers-buffer-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/buffer/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.BufferingStrategy](publishers/bufferingstrategy.md)
  A strategy that handles exhaustion of a buffer’s capacity.
- [Publishers.PrefetchStrategy](publishers/prefetchstrategy.md)
  A strategy for filling a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/buffer)*