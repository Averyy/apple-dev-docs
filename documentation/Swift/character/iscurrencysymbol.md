# isCurrencySymbol

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether this character represents a currency symbol.

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
var isCurrencySymbol: Bool { get }
```

#### Discussion

For example, the following characters all represent currency symbols:

- “$” (U+0024 DOLLAR SIGN)
- “¥” (U+00A5 YEN SIGN)
- “€” (U+20AC EURO SIGN)

## See Also

- [var isLetter: Bool](character/isletter.md)
  A Boolean value indicating whether this character is a letter.
- [var isPunctuation: Bool](character/ispunctuation.md)
  A Boolean value indicating whether this character represents punctuation.
- [var isNewline: Bool](character/isnewline.md)
  A Boolean value indicating whether this character represents a newline.
- [var isWhitespace: Bool](character/iswhitespace.md)
  A Boolean value indicating whether this character represents whitespace, including newlines.
- [var isSymbol: Bool](character/issymbol.md)
  A Boolean value indicating whether this character represents a symbol.
- [var isMathSymbol: Bool](character/ismathsymbol.md)
  A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/iscurrencysymbol)*