# isIncluded

**Framework**: Combine  
**Kind**: property

An error-throwing closure that indicates whether this filter should republish an element.

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
let isIncluded: (Upstream.Output) throws -> Bool
```

## See Also

- [let upstream: Upstream](publishers/tryfilter/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryfilter/isincluded)*