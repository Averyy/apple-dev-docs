# init(upstream:predicate:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.

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
init(upstream: Upstream, predicate: @escaping (Upstream.Output) -> Bool)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `predicate`: The closure that determines whether the publisher should consider an element as a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/containswhere/init(upstream:predicate:))*