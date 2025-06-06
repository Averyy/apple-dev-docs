# upstream

**Framework**: Combine  
**Kind**: property

The publisher that this publisher receives elements from.

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
let upstream: Upstream
```

## See Also

- [let initialResult: Output](publishers/tryscan/initialresult.md)
  The previous result returned by the `nextPartialResult` closure.
- [let nextPartialResult: (Output, Upstream.Output) throws -> Output](publishers/tryscan/nextpartialresult.md)
  An error-throwing closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryscan/upstream)*