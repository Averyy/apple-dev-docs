# init(upstream:range:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that publishes elements specified by a range.

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
init(upstream: Upstream, range: CountableRange<Int>)
```

## Parameters

- `upstream`: The publisher from which this publisher receives its elements.
- `range`: The range of elements to publish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/output/init(upstream:range:))*