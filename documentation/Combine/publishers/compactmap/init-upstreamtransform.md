# init(upstream:transform:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that republishes all non-`nil` results of calling a closure with each received element.

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
init(upstream: Upstream, transform: @escaping (Upstream.Output) -> Output?)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `transform`: A closure that receives values from the upstream publisher and returns optional values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/compactmap/init(upstream:transform:))*