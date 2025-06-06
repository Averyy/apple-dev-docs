# init(upstream:handler:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or by throwing an error.

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
init(upstream: Upstream, handler: @escaping (Upstream.Failure) throws -> NewPublisher)
```

## Parameters

- `upstream`: The publisher from which this publisher receives its elements.
- `handler`: A closure that accepts the upstream failure as input and either returns a publisher to replace the upstream publisher. If this closure throws an error, the publisher terminates with the thrown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycatch/init(upstream:handler:))*