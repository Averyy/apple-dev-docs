# compare(_:options:range:locale:)

**Framework**: Swift  
**Kind**: method

Compares the string using the specified options and returns the lexical ordering for the range.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func compare<T>(_ aString: T, options mask: String.CompareOptions = [], range: Range<Self.Index>? = nil, locale: Locale? = nil) -> ComparisonResult where T : StringProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/compare(_:options:range:locale:))*