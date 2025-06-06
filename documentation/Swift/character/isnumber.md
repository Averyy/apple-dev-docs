# isNumber

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether this character represents a number.

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
var isNumber: Bool { get }
```

#### Discussion

For example, the following characters all represent numbers:

- “7” (U+0037 DIGIT SEVEN)
- “⅚” (U+215A VULGAR FRACTION FIVE SIXTHS)
- “㊈” (U+3288 CIRCLED IDEOGRAPH NINE)
- “𝟠” (U+1D7E0 MATHEMATICAL DOUBLE-STRUCK DIGIT EIGHT)
- “๒” (U+0E52 THAI DIGIT TWO)

## See Also

- [var isWholeNumber: Bool](character/iswholenumber.md)
  A Boolean value indicating whether this character represents a whole number.
- [var wholeNumberValue: Int?](character/wholenumbervalue.md)
  The numeric value this character represents, if it represents a whole number.
- [var isHexDigit: Bool](character/ishexdigit.md)
  A Boolean value indicating whether this character represents a hexadecimal digit.
- [var hexDigitValue: Int?](character/hexdigitvalue.md)
  The numeric value this character represents, if it is a hexadecimal digit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/isnumber)*