# transform

**Framework**: Combine  
**Kind**: property

The error-throwing closure that transforms elements from the upstream publisher.

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
let transform: (Upstream.Output) throws -> Output
```

## See Also

- [let upstream: Upstream](publishers/trymap/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trymap/transform)*