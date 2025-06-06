# isPunctuation

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether this character represents punctuation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isPunctuation: Bool { get }
```

#### Discussion

For example, the following characters all represent punctuation:

- “!” (U+0021 EXCLAMATION MARK)
- “؟” (U+061F ARABIC QUESTION MARK)
- “…” (U+2026 HORIZONTAL ELLIPSIS)
- “—” (U+2014 EM DASH)
- ““” (U+201C LEFT DOUBLE QUOTATION MARK)

## See Also

- [var isLetter: Bool](character/isletter.md)
  A Boolean value indicating whether this character is a letter.
- [var isNewline: Bool](character/isnewline.md)
  A Boolean value indicating whether this character represents a newline.
- [var isWhitespace: Bool](character/iswhitespace.md)
  A Boolean value indicating whether this character represents whitespace, including newlines.
- [var isSymbol: Bool](character/issymbol.md)
  A Boolean value indicating whether this character represents a symbol.
- [var isMathSymbol: Bool](character/ismathsymbol.md)
  A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
- [var isCurrencySymbol: Bool](character/iscurrencysymbol.md)
  A Boolean value indicating whether this character represents a currency symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/ispunctuation)*