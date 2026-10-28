# isSymbol

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether this character represents a symbol.

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
var isSymbol: Bool { get }
```

## Discussion

This property is `true` only for characters composed of scalars in the “Math_Symbol”, “Currency_Symbol”, “Modifier_Symbol”, or “Other_Symbol” categories in the [Unicode Standard](https://unicode.org/reports/tr44/#General_Category_Values).

For example, the following characters all represent symbols:

- “®” (U+00AE REGISTERED SIGN)
- “⌹” (U+2339 APL FUNCTIONAL SYMBOL QUAD DIVIDE)
- “⡆” (U+2846 BRAILLE PATTERN DOTS-237)

## See Also

### Inspecting a Character
- [var isLetter: Bool](./isletter.md)
  A Boolean value indicating whether this character is a letter.
- [var isPunctuation: Bool](./ispunctuation.md)
  A Boolean value indicating whether this character represents punctuation.
- [var isNewline: Bool](./isnewline.md)
  A Boolean value indicating whether this character represents a newline.
- [var isWhitespace: Bool](./iswhitespace.md)
  A Boolean value indicating whether this character represents whitespace, including newlines.
- [var isMathSymbol: Bool](./ismathsymbol.md)
  A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
- [var isCurrencySymbol: Bool](./iscurrencysymbol.md)
  A Boolean value indicating whether this character represents a currency symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/issymbol)*