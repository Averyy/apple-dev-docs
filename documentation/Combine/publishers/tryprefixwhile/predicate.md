# predicate

**Framework**: Combine  
**Kind**: property

The error-throwing closure that determines whether publishing should continue.

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
let predicate: (Publishers.TryPrefixWhile<Upstream>.Output) throws -> Bool
```

## See Also

- [let upstream: Upstream](publishers/tryprefixwhile/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryprefixwhile/predicate)*