# handler

**Framework**: Combine  
**Kind**: property

A closure that accepts the upstream failure as input and either returns a publisher to replace the upstream publisher or throws an error.

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
let handler: (Upstream.Failure) throws -> NewPublisher
```

## See Also

- [let upstream: Upstream](publishers/trycatch/upstream.md)
  The publisher from which this publisher receives its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycatch/handler)*