# Publishers.Zip.Output

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

This publisher produces two-element tuples, whose members’ types correspond to the types produced by the upstream publishers.

## See Also

- [Publishers.Zip.Failure](publishers/zip/failure.md)
  The kind of errors this publisher might publish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip/output)*