# init(upstream:other:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that ignores elements from the upstream publisher until it receives an element from another publisher.

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

- `upstream`: A publisher to drop elements from while waiting for another publisher to emit elements.
- `other`: A publisher to monitor for its first emitted element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/dropuntiloutput/init(upstream:other:))*