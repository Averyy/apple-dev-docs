# init(upstream:initial:nextPartialResult:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.

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
init(upstream: Upstream, initial: Output, nextPartialResult: @escaping (Output, Upstream.Output) throws -> Output)
```

## Parameters

- `upstream`: The publisher from which this publisher receives elements.
- `initial`: The initial value provided on the first-use of the closure.
- `nextPartialResult`: An error-throwing closure that takes the previously-accumulated value and the next element from the upstream to produce a new value. If this closure throws an error, the publisher fails and passes the error to its subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryreduce/init(upstream:initial:nextpartialresult:))*