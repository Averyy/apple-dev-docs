# init(upstream:predicate:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.

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
- `predicate`: A closure that evaluates each received element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/allsatisfy/init(upstream:predicate:))*