# Publishers.CombineLatest.Output

**Framework**: Combine  
**Kind**: typealias

The kind of values published by this publisher.

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
typealias Output = (A.Output, B.Output)
```

#### Discussion

This publisher produces two-element tuples of the upstream publishers’ output types.

## See Also

- [Publishers.CombineLatest.Failure](publishers/combinelatest/failure.md)
  The kind of errors this publisher might publish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/combinelatest/output)*