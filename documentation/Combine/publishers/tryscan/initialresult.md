# initialResult

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

The previous result returned by the `nextPartialResult` closure.

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
let initialResult: Output
```

## See Also

### Inspecting publisher properties
- [let upstream: Upstream](./upstream.md)
  The publisher that this publisher receives elements from.
- [let nextPartialResult: (Output, Upstream.Output) throws -> Output](./nextpartialresult.md)
  An error-throwing closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryscan/initialresult)*