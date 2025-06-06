# hexDigitValue

**Framework**: Swift  
**Kind**: property

The numeric value this character represents, if it is a hexadecimal digit.

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
var hexDigitValue: Int? { get }
```

#### Discussion

Hexadecimal digits include 0-9, Latin letters a-f and A-F, and their fullwidth compatibility forms. If the character does not represent a hexadecimal digit, the value of this property is `nil`.

```swift
let chars: [Character] = ["1", "a", "Ｆ", "g"]
for ch in chars {
    print(ch, "-->", ch.hexDigitValue)
}
// Prints:
// 1 --> Optional(1)
// a --> Optional(10)
// Ｆ --> Optional(15)
// g --> nil
```

## See Also

- [var isNumber: Bool](character/isnumber.md)
  A Boolean value indicating whether this character represents a number.
- [var isWholeNumber: Bool](character/iswholenumber.md)
  A Boolean value indicating whether this character represents a whole number.
- [var wholeNumberValue: Int?](character/wholenumbervalue.md)
  The numeric value this character represents, if it represents a whole number.
- [var isHexDigit: Bool](character/ishexdigit.md)
  A Boolean value indicating whether this character represents a hexadecimal digit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/hexdigitvalue)*