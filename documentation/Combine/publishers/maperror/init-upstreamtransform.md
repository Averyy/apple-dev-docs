# init(upstream:transform:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that converts any failure from the upstream publisher into a new error.

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
init(upstream: Upstream, transform: @escaping (Upstream.Failure) -> Failure)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `transform`: The closure that converts the upstream failure into a new error.

## See Also

- [init(upstream: Upstream, (Upstream.Failure) -> Failure)](publishers/maperror/init(upstream:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/maperror/init(upstream:transform:))*