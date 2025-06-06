# Publishers.PrefetchStrategy.byRequest

**Framework**: Combine  
**Kind**: case

A strategy that avoids prefetching and instead performs requests on demand.

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
case byRequest
```

#### Discussion

This strategy just forwards the downstream’s requests to the upstream publisher.

## See Also

- [Publishers.PrefetchStrategy.keepFull](publishers/prefetchstrategy/keepfull.md)
  A strategy to fill the buffer at subscription time, and keep it full thereafter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/prefetchstrategy/byrequest)*