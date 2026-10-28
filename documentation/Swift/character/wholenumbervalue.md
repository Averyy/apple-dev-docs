# wholeNumberValue

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The numeric value this character represents, if it represents a whole number.

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
var wholeNumberValue: Int? { get }
```

## Discussion

If this character does not represent a whole number, or the value is too large to represent as an `Int`, the value of this property is `nil`.

```swift
let chars: [Character] = ["4", "④", "万", "a"]
for ch in chars {
    print(ch, "-->", ch.wholeNumberValue)
}
// Prints:
// 4 --> Optional(4)
// ④ --> Optional(4)
// 万 --> Optional(10000)
// a --> nil
```

## See Also

### Checking a Character’s Numeric Properties
- [var isNumber: Bool](./isnumber.md)
  A Boolean value indicating whether this character represents a number.
- [var isWholeNumber: Bool](./iswholenumber.md)
  A Boolean value indicating whether this character represents a whole number.
- [var isHexDigit: Bool](./ishexdigit.md)
  A Boolean value indicating whether this character represents a hexadecimal digit.
- [var hexDigitValue: Int?](./hexdigitvalue.md)
  The numeric value this character represents, if it is a hexadecimal digit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/wholenumbervalue)*