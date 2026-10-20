# nextPartialResult

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

An error-throwing closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.

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
let nextPartialResult: (Output, Upstream.Output) throws -> Output
```

## See Also

### Inspecting publisher properties
- [let upstream: Upstream](./upstream.md)
  The publisher that this publisher receives elements from.
- [let initialResult: Output](./initialresult.md)
  The previous result returned by the `nextPartialResult` closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryscan/nextpartialresult)*