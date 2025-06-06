# init(upstream:transform:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.

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
init(upstream: Upstream, transform: @escaping (Upstream.Output) throws -> Output)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `transform`: The error-throwing closure that transforms elements from the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trymap/init(upstream:transform:))*