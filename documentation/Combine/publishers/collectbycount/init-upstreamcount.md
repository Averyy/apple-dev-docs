# init(upstream:count:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that buffers a maximum number of items.

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
init(upstream: Upstream, count: Int)
```

## Parameters

- `upstream`: The publisher that this publisher receives elements from.
- `count`: The maximum number of received elements to buffer before publishing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/collectbycount/init(upstream:count:))*