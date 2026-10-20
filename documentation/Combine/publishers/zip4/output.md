# Publishers.Zip4.Output

**Framework**: Combine  
**Kind**: typealias  
**Role**: Type Alias

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

This publisher produces four-element tuples, whose members’ types correspond to the types produced by the upstream publishers.

## See Also

### Declaring supporting types
- [Publishers.Zip4.Failure](./failure.md)
  The kind of errors this publisher might publish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip4/output)*