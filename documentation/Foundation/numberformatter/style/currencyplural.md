# NumberFormatter.Style.currencyPlural

**Framework**: Foundation  
**Kind**: case

A currency style format that uses the pluralized denomination defined by the number formatter locale.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case currencyPlural
```

#### Discussion

This style behaves like the [`NumberFormatter.Style.currency`](numberformatter/style/currency.md) style, except that the currency symbol is replaced by the corresponding pluralized denomination. For example, in the en_US locale, the number 1234.5678 is represented as 1,234.57 US dollars; in the fr_FR locale, the number 1234.5678 is represented as 1 234,57 euros.

## See Also

- [NumberFormatter.Style.none](numberformatter/style/none.md)
  An integer representation.
- [NumberFormatter.Style.decimal](numberformatter/style/decimal.md)
  A decimal style format.
- [NumberFormatter.Style.percent](numberformatter/style/percent.md)
  A percent style format.
- [NumberFormatter.Style.scientific](numberformatter/style/scientific.md)
  A scientific style format.
- [NumberFormatter.Style.spellOut](numberformatter/style/spellout.md)
  A style format in which numbers are spelled out in the language defined by the number formatter locale.
- [NumberFormatter.Style.ordinal](numberformatter/style/ordinal.md)
  An ordinal style format.
- [NumberFormatter.Style.currency](numberformatter/style/currency.md)
  A currency style format that uses the currency symbol defined by the number formatter locale.
- [NumberFormatter.Style.currencyAccounting](numberformatter/style/currencyaccounting.md)
  An accounting currency style format that uses the currency symbol defined by the number formatter locale.
- [NumberFormatter.Style.currencyISOCode](numberformatter/style/currencyisocode.md)
  A currency style format that uses the ISO 4217 currency code defined by the number formatter locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/style/currencyplural)*