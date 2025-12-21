# isCanonicallyLessThan(_:)

**Framework**: Swift  
**Kind**: method

Whether `self` orders less than `other` under Unicode Canonical Equivalence using normalized code-unit order (in NFC).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func isCanonicallyLessThan(_ other: UTF8Span) -> Bool
```

#### Discussion

> **Note**: O(n)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/iscanonicallylessthan(_:))*