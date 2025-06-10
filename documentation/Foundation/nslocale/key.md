# NSLocale.Key

**Framework**: Foundation  
**Kind**: struct

The keys used to access components of a locale.

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
struct Key
```

#### Discussion

Use these keys with the methods [`object(forKey:)`](nslocale/object(forkey:).md) and [`displayName(forKey:value:)`](nslocale/displayname(forkey:value:).md).

## Topics

### Initializers
- [init(rawValue: String)](nslocale/key/init(rawvalue:).md)
### Keys
- [static let identifier: NSLocale.Key](nslocale/key/identifier.md)
  The locale identifier.
- [static let countryCode: NSLocale.Key](nslocale/key/countrycode.md)
  The locale country or region code.
- [static let languageCode: NSLocale.Key](nslocale/key/languagecode.md)
  The locale language code.
- [static let scriptCode: NSLocale.Key](nslocale/key/scriptcode.md)
  The locale script code.
- [static let variantCode: NSLocale.Key](nslocale/key/variantcode.md)
  The locale variant code.
- [static let exemplarCharacterSet: NSLocale.Key](nslocale/key/exemplarcharacterset.md)
  The exemplar character set for the locale.
- [static let calendar: NSLocale.Key](nslocale/key/calendar.md)
  The calendar associated with the locale.
- [static let collationIdentifier: NSLocale.Key](nslocale/key/collationidentifier.md)
  The collation associated with the locale.
- [static let collatorIdentifier: NSLocale.Key](nslocale/key/collatoridentifier.md)
  The collation identifier for the locale.
- [static let usesMetricSystem: NSLocale.Key](nslocale/key/usesmetricsystem.md)
  A flag that indicates whether the locale uses the metric system.
- [static let measurementSystem: NSLocale.Key](nslocale/key/measurementsystem.md)
  The measurement system associated with the locale.
- [static let decimalSeparator: NSLocale.Key](nslocale/key/decimalseparator.md)
  The decimal separator associated with the locale.
- [static let groupingSeparator: NSLocale.Key](nslocale/key/groupingseparator.md)
  The numeric grouping separator associated with the locale.
- [static let currencySymbol: NSLocale.Key](nslocale/key/currencysymbol.md)
  The currency symbol associated with the locale.
- [static let currencyCode: NSLocale.Key](nslocale/key/currencycode.md)
  The currency code associated with the locale.
- [static let quotationEndDelimiterKey: NSLocale.Key](nslocale/key/quotationenddelimiterkey.md)
  The end quotation symbol associated with the locale.
- [static let quotationBeginDelimiterKey: NSLocale.Key](nslocale/key/quotationbegindelimiterkey.md)
  The begin quotation symbol associated with the locale.
- [static let alternateQuotationEndDelimiterKey: NSLocale.Key](nslocale/key/alternatequotationenddelimiterkey.md)
  The alternate end quotation symbol associated with the locale.
- [static let alternateQuotationBeginDelimiterKey: NSLocale.Key](nslocale/key/alternatequotationbegindelimiterkey.md)
  The alternating begin quotation symbol associated with the locale.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func object(forKey: NSLocale.Key) -> Any?](nslocale/object(forkey:).md)
  Returns the value of the component corresponding to the specified key.
- [func displayName(forKey: NSLocale.Key, value: Any) -> String?](nslocale/displayname(forkey:value:).md)
  Returns the display name for the given locale component value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/key)*