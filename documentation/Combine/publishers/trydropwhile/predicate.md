# predicate

**Framework**: Combine  
**Kind**: property

The error-throwing closure that indicates whether to drop the element.

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
let predicate: (Publishers.TryDropWhile<Upstream>.Output) throws -> Bool
```

## See Also

- [let upstream: Upstream](publishers/trydropwhile/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trydropwhile/predicate)*