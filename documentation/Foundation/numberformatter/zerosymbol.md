# zeroSymbol

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The string used to represent a zero value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var zeroSymbol: String? { get set }
```

```objc
@property (copy, nullable) NSString * zeroSymbol;
```

## Discussion

If not specified, zero values are formatted normally.

You might, for example, set this property to “` ``-`` `” in a spreadsheet used for accounting.

## See Also

### Configuring Numeric Symbols
- [var percentSymbol: String!](./percentsymbol.md)
  The string used to represent a percent symbol.
- [var perMillSymbol: String!](./permillsymbol.md)
  The string used to represent a per-mill (per-thousand) symbol.
- [var minusSign: String!](./minussign.md)
  The string used to represent a minus sign.
- [var plusSign: String!](./plussign.md)
  The string used to represent a plus sign.
- [var exponentSymbol: String!](./exponentsymbol.md)
  The string used to represent an exponent symbol.
- [var nilSymbol: String](./nilsymbol.md)
  The string used to represent a `nil` value.
- [var notANumberSymbol: String!](./notanumbersymbol.md)
  The string used to represent a NaN (“not a number”) value.
- [var negativeInfinitySymbol: String](./negativeinfinitysymbol.md)
  The string used to represent a negative infinity symbol.
- [var positiveInfinitySymbol: String](./positiveinfinitysymbol.md)
  The string used to represent a positive infinity symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/zerosymbol)*