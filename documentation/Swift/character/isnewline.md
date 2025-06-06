# isNewline

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether this character represents a newline.

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
var isNewline: Bool { get }
```

#### Discussion

For example, the following characters all represent newlines:

- “\n” (U+000A): LINE FEED (LF)
- U+000B: LINE TABULATION (VT)
- U+000C: FORM FEED (FF)
- “\r” (U+000D): CARRIAGE RETURN (CR)
- “\r\n” (U+000D U+000A): CR-LF
- U+0085: NEXT LINE (NEL)
- U+2028: LINE SEPARATOR
- U+2029: PARAGRAPH SEPARATOR

## See Also

- [var isLetter: Bool](character/isletter.md)
  A Boolean value indicating whether this character is a letter.
- [var isPunctuation: Bool](character/ispunctuation.md)
  A Boolean value indicating whether this character represents punctuation.
- [var isWhitespace: Bool](character/iswhitespace.md)
  A Boolean value indicating whether this character represents whitespace, including newlines.
- [var isSymbol: Bool](character/issymbol.md)
  A Boolean value indicating whether this character represents a symbol.
- [var isMathSymbol: Bool](character/ismathsymbol.md)
  A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
- [var isCurrencySymbol: Bool](character/iscurrencysymbol.md)
  A Boolean value indicating whether this character represents a currency symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/isnewline)*