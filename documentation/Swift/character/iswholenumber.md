# isWholeNumber

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether this character represents a whole number.

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
var isWholeNumber: Bool { get }
```

#### Discussion

For example, the following characters all represent whole numbers:

- “1” (U+0031 DIGIT ONE) => 1
- “५” (U+096B DEVANAGARI DIGIT FIVE) => 5
- “๙” (U+0E59 THAI DIGIT NINE) => 9
- “万” (U+4E07 CJK UNIFIED IDEOGRAPH-4E07) => 10_000

## See Also

- [var isNumber: Bool](character/isnumber.md)
  A Boolean value indicating whether this character represents a number.
- [var wholeNumberValue: Int?](character/wholenumbervalue.md)
  The numeric value this character represents, if it represents a whole number.
- [var isHexDigit: Bool](character/ishexdigit.md)
  A Boolean value indicating whether this character represents a hexadecimal digit.
- [var hexDigitValue: Int?](character/hexdigitvalue.md)
  The numeric value this character represents, if it is a hexadecimal digit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/iswholenumber)*