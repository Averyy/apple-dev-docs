# init(upstream:areInIncreasingOrder:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.

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
init(upstream: Upstream, areInIncreasingOrder: @escaping (Upstream.Output, Upstream.Output) -> Bool)
```

## Parameters

- `upstream`: The publisher from which this publisher receives its elements.
- `areInIncreasingOrder`: A closure that receives two elements and returns true if they are in increasing order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/comparison/init(upstream:areinincreasingorder:))*