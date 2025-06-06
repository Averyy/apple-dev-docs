# predicate

**Framework**: Combine  
**Kind**: property

The predicate closure used to evaluate whether two elements are duplicates.

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
let predicate: (Publishers.RemoveDuplicates<Upstream>.Output, Publishers.RemoveDuplicates<Upstream>.Output) -> Bool
```

## See Also

- [let upstream: Upstream](publishers/removeduplicates/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/removeduplicates/predicate)*