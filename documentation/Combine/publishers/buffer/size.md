# size

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

The maximum number of elements to store.

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
let size: Int
```

## See Also

### Inspecting publisher properties
- [let upstream: Upstream](./upstream.md)
  The publisher from which this publisher receives elements.
- [let prefetch: Publishers.PrefetchStrategy](./prefetch.md)
  The strategy for initially populating the buffer.
- [let whenFull: Publishers.BufferingStrategy<Publishers.Buffer<Upstream>.Failure>](./whenfull.md)
  The action to take when the buffer becomes full.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/buffer/size)*