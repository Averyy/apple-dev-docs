# init(upstream:isIncluded:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that republishes all elements that match a provided closure.

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
init(upstream: Upstream, isIncluded: @escaping (Upstream.Output) -> Bool)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `isIncluded`: A closure that indicates whether to republish an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/filter/init(upstream:isincluded:))*