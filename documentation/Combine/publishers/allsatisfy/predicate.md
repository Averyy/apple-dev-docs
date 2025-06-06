# predicate

**Framework**: Combine  
**Kind**: property

A closure that evaluates each received element.

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
let predicate: (Upstream.Output) -> Bool
```

#### Discussion

Return `true` to continue, or `false` to cancel the upstream and finish.

## See Also

- [let upstream: Upstream](publishers/allsatisfy/upstream.md)
  The publisher from which this publisher receives elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/allsatisfy/predicate)*