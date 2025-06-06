# init(upstream:other:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that republishes elements until another publisher emits an element.

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
init(upstream: Upstream, other: Other)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `other`: Another publisher, the first output from which causes this publisher to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/prefixuntiloutput/init(upstream:other:))*