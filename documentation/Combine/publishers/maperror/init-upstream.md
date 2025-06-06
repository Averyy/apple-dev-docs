# init(upstream:_:)

**Framework**: Combine  
**Kind**: init

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
init(upstream: Upstream, _ map: @escaping (Upstream.Failure) -> Failure)
```

## See Also

- [init(upstream: Upstream, transform: (Upstream.Failure) -> Failure)](publishers/maperror/init(upstream:transform:).md)
  Creates a publisher that converts any failure from the upstream publisher into a new error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/maperror/init(upstream:_:))*