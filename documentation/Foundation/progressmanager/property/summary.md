# Summary

**Framework**: Foundation  
**Kind**: associatedtype  
**Required**: Yes

The type used for aggregated summaries of this property.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
associatedtype Summary : Equatable, Sendable
```

#### Discussion

This associated type represents the type used when summarizing property values across multiple progress managers in a subtree. The currently allowed types are `Int`, `Double`, `[String?]`, `[URL?]` or `[UInt64]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/property/summary)*