# Publishers.Zip3.Output

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
typealias Output = (A.Output, B.Output, C.Output)
```

#### Discussion

This publisher produces three-element tuples, whose members’ types correspond to the types produced by the upstream publishers.

## See Also

- [Publishers.Zip3.Failure](publishers/zip3/failure.md)
  The kind of errors this publisher might publish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip3/output)*