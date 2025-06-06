# internationalCurrencySymbol

**Framework**: Foundation  
**Kind**: property

The international currency symbol used by the receiver.

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
var internationalCurrencySymbol: String! { get set }
```

#### Discussion

A region typically has a local currency symbol and an international currency symbol. The local symbol is used within the region, while the international currency symbol is used in international contexts to specify that region’s currency unambiguously. The international currency symbol is often represented by a Unicode code point.

## See Also

- [var currencySymbol: String!](numberformatter/currencysymbol.md)
  The string used by the receiver as a local currency symbol.
- [var currencyCode: String!](numberformatter/currencycode.md)
  The receiver’s currency code.
- [var currencyGroupingSeparator: String!](numberformatter/currencygroupingseparator.md)
  The currency grouping separator for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/internationalcurrencysymbol)*