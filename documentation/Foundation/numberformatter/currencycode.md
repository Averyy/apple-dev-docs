# currencyCode

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s currency code.

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
var currencyCode: String! { get set }
```

```objc
@property (copy, null_resettable) NSString * currencyCode;
```

#### Discussion

A currency code is a three-letter code that is, in most cases, composed of a region’s two-character Internet region code plus an extra character to denote the currency unit. For example, the currency code for the Australian dollar is “AUD”. Currency codes are based on the ISO 4217 standard.

## See Also

### Configuring the Format of Currency
- [var currencySymbol: String!](./currencysymbol.md)
  The string used by the receiver as a local currency symbol.
- [var internationalCurrencySymbol: String!](./internationalcurrencysymbol.md)
  The international currency symbol used by the receiver.
- [var currencyGroupingSeparator: String!](./currencygroupingseparator.md)
  The currency grouping separator for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/currencycode)*