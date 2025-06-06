# zeroSymbol

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

If not specified, zero values are formatted normally.

You might, for example, set this property to “` ``-`` `” in a spreadsheet used for accounting.

## See Also

- [var percentSymbol: String!](numberformatter/percentsymbol.md)
  The string used to represent a percent symbol.
- [var perMillSymbol: String!](numberformatter/permillsymbol.md)
  The string used to represent a per-mill (per-thousand) symbol.
- [var minusSign: String!](numberformatter/minussign.md)
  The string used to represent a minus sign.
- [var plusSign: String!](numberformatter/plussign.md)
  The string used to represent a plus sign.
- [var exponentSymbol: String!](numberformatter/exponentsymbol.md)
  The string used to represent an exponent symbol.
- [var nilSymbol: String](numberformatter/nilsymbol.md)
  The string used to represent a `nil` value.
- [var notANumberSymbol: String!](numberformatter/notanumbersymbol.md)
  The string used to represent a NaN (“not a number”) value.
- [var negativeInfinitySymbol: String](numberformatter/negativeinfinitysymbol.md)
  The string used to represent a negative infinity symbol.
- [var positiveInfinitySymbol: String](numberformatter/positiveinfinitysymbol.md)
  The string used to represent a positive infinity symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/zerosymbol)*