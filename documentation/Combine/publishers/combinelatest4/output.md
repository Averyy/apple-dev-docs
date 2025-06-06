# Publishers.CombineLatest4.Output

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
typealias Output = (A.Output, B.Output, C.Output, D.Output)
```

#### Discussion

This publisher produces four-element tuples of the upstream publishers’ output types.

## See Also

- [Publishers.CombineLatest4.Failure](publishers/combinelatest4/failure.md)
  The kind of errors this publisher might publish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/combinelatest4/output)*