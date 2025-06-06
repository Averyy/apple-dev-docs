# range(of:options:locale:)

**Framework**: Foundation  
**Kind**: method

Returns the range of a substring in the attributed string, if it exists.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func range<T>(of stringToFind: T, options: String.CompareOptions = [], locale: Locale? = nil) -> Range<AttributedString.Index>? where T : StringProtocol
```

#### Return Value

The range where `stringToFind` exists in the attributed string, or `nil` if it isn’t present.

## Parameters

- `stringToFind`: The string to find.
- `options`: Options that affect the search behavior, such as case-insensivity, search direction, and regular expression matching.
- `locale`: The locale to use when searching, or   to use the current locale. The default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol/range(of:options:locale:))*