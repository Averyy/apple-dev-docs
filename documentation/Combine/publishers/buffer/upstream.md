# upstream

**Framework**: Combine  
**Kind**: property

The publisher from which this publisher receives elements.

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
let upstream: Upstream
```

## See Also

- [let size: Int](publishers/buffer/size.md)
  The maximum number of elements to store.
- [let prefetch: Publishers.PrefetchStrategy](publishers/buffer/prefetch.md)
  The strategy for initially populating the buffer.
- [let whenFull: Publishers.BufferingStrategy<Publishers.Buffer<Upstream>.Failure>](publishers/buffer/whenfull.md)
  The action to take when the buffer becomes full.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/buffer/upstream)*