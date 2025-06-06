# predicate

**Framework**: Combine  
**Kind**: property

A closure that evaluates each received element.

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
let predicate: (Upstream.Output) throws -> Bool
```

#### Discussion

Return `true` to continue, or `false` to cancel the upstream and complete. The closure may throw, in which case the publisher cancels the upstream publisher and fails with the thrown error.

## See Also

- [let upstream: Upstream](publishers/tryallsatisfy/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryallsatisfy/predicate)*