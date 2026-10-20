# upstream

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

The publisher from which this publisher receives its elements.

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

### Inspecting publisher properties
- [let handler: (Upstream.Failure) -> NewPublisher](./handler.md)
  A closure that accepts the upstream failure as input and returns a publisher to replace the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/catch/upstream)*