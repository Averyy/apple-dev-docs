# init(upstream:initialResult:nextPartialResult:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.

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
init(upstream: Upstream, initialResult: Output, nextPartialResult: @escaping (Output, Upstream.Output) -> Output)
```

## Parameters

- `upstream`: The publisher that this publisher receives elements from.
- `initialResult`: The previous result returned by the   closure.
- `nextPartialResult`: A closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/scan/init(upstream:initialresult:nextpartialresult:))*