# transform

**Framework**: Combine  
**Kind**: property

An error-throwing closure that receives values from the upstream publisher and returns optional values.

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
let transform: (Upstream.Output) throws -> Output?
```

#### Discussion

If this closure throws an error, the publisher fails.

## See Also

- [let upstream: Upstream](publishers/trycompactmap/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycompactmap/transform)*