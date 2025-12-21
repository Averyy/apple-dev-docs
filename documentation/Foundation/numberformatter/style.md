# NumberFormatter.Style

**Framework**: Foundation  
**Kind**: enum

The predefined number format styles used by the [`numberStyle`](numberformatter/numberstyle.md) property.

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
enum Style
```

#### Overview

The table below provides examples of each formatting style for the U.S., France, and China.

| Style | en_US Locale | fr_FR Locale | zh_CN Locale |
| --- | --- | --- | --- |
| [`NumberFormatter.Style.none`](numberformatter/style/none.md) | 1235 | 1235 | 1235 |
| [`NumberFormatter.Style.decimal`](numberformatter/style/decimal.md) | 1,234.568 | 1 234,568 | 1,234.568 |
| [`NumberFormatter.Style.percent`](numberformatter/style/percent.md) | 12% | 12 % | 12% |
| [`NumberFormatter.Style.scientific`](numberformatter/style/scientific.md) | 1.2345678E3 | 1,2345678E3 | 1.2345678E3 |
| [`NumberFormatter.Style.spellOut`](numberformatter/style/spellout.md) | one hundred twenty-three | cent vingt-trois | 一百二十三 |
| [`NumberFormatter.Style.ordinal`](numberformatter/style/ordinal.md) | 3rd | 3e | 第3 |
| [`NumberFormatter.Style.currency`](numberformatter/style/currency.md) | $1,234.57 | 1 234,57 € | ￥1,234.57 |
| [`NumberFormatter.Style.currencyAccounting`](numberformatter/style/currencyaccounting.md) | ($1,234.57) | (1 234,57 €) | (￥1,234.57) |
| [`NumberFormatter.Style.currencyISOCode`](numberformatter/style/currencyisocode.md) | USD1,234.57 | 1 234,57 EUR | CNY1,234.57 |
| [`NumberFormatter.Style.currencyPlural`](numberformatter/style/currencyplural.md) | 1,234.57 US dollars | 1 234,57 euros | 1,234.57人民币 |

## Topics

### Formatting Styles
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
- [NumberFormatter.Style.currencyPlural](numberformatter/style/currencyplural.md)
  A currency style format that uses the pluralized denomination defined by the number formatter locale.
### Initializers
- [init?(rawValue: UInt)](numberformatter/style/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NumberFormatter.Behavior](numberformatter/behavior.md)
  These constants specify the behavior of a number formatter. These constants are returned by the [`defaultFormatterBehavior()`](numberformatter/defaultformatterbehavior().md) class method and the [`formatterBehavior`](numberformatter/formatterbehavior.md) property.
- [NumberFormatter.PadPosition](numberformatter/padposition.md)
  These constants are used to specify how numbers should be padded. These constants are used by the [`paddingPosition`](numberformatter/paddingposition.md) property.
- [NumberFormatter.RoundingMode](numberformatter/roundingmode-swift.enum.md)
  These constants are used to specify how numbers should be rounded. These constants are used by the [`roundingMode`](numberformatter/roundingmode-swift.property.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/style)*