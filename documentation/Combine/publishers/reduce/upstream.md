# upstream

**Framework**: Combine  
**Kind**: property

The publisher from which this publisher receives elements.

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

- [let initial: Output](publishers/reduce/initial.md)
  The initial value provided on the first invocation of the closure.
- [let nextPartialResult: (Output, Upstream.Output) -> Output](publishers/reduce/nextpartialresult.md)
  A closure that takes the previously-accumulated value and the next element from the upstream publisher to produce a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/reduce/upstream)*