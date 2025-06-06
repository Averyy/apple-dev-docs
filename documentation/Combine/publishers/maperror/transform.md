# transform

**Framework**: Combine  
**Kind**: property

The closure that converts the upstream failure into a new error.

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
let transform: (Upstream.Failure) -> Failure
```

## See Also

- [let upstream: Upstream](publishers/maperror/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/maperror/transform)*