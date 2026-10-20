# initial

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

The initial value provided on the first-use of the closure.

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
let initial: Output
```

## See Also

### Inspecting publisher properties
- [let upstream: Upstream](./upstream.md)
  The publisher from which this publisher receives elements.
- [let nextPartialResult: (Output, Upstream.Output) throws -> Output](./nextpartialresult.md)
  An error-throwing closure that takes the previously-accumulated value and the next element from the upstream to produce a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryreduce/initial)*