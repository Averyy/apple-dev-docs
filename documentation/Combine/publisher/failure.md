# Failure

**Framework**: Combine  
**Kind**: associatedtype  
**Required**: Yes

The kind of errors this publisher might publish.

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
associatedtype Failure : Error
```

## Mentions

- [Receiving and Handling Events with Combine](receiving-and-handling-events-with-combine.md)

#### Discussion

Use `Never` if this `Publisher` does not publish errors.

## See Also

- [associatedtype Output](publisher/output.md)
  The kind of values published by this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/failure)*