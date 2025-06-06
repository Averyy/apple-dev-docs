# transform

**Framework**: Combine  
**Kind**: property

A closure that receives values from the upstream publisher and returns optional values.

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
let transform: (Upstream.Output) -> Output?
```

## See Also

- [let upstream: Upstream](publishers/compactmap/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/compactmap/transform)*