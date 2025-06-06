# nextPartialResult

**Framework**: Combine  
**Kind**: property

An error-throwing closure that takes the previously-accumulated value and the next element from the upstream to produce a new value.

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

#### Discussion

If this closure throws an error, the publisher fails and passes the error to its subscriber.

## See Also

- [let upstream: Upstream](publishers/tryreduce/upstream.md)
  The publisher from which this publisher receives elements.
- [let initial: Output](publishers/tryreduce/initial.md)
  The initial value provided on the first-use of the closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryreduce/nextpartialresult)*