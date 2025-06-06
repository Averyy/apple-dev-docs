# initial

**Framework**: Combine  
**Kind**: property

The initial value provided on the first invocation of the closure.

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

- [let upstream: Upstream](publishers/reduce/upstream.md)
  The publisher from which this publisher receives elements.
- [let nextPartialResult: (Output, Upstream.Output) -> Output](publishers/reduce/nextpartialresult.md)
  A closure that takes the previously-accumulated value and the next element from the upstream publisher to produce a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/reduce/initial)*