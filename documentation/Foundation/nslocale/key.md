# NSLocale.Key

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * NSLocaleKey;
```

## Discussion

Use these keys with the methods [`object(forKey:)`](./object%28forkey%29.md) and [`displayName(forKey:value:)`](./displayname%28forkey,value%29.md).

## Topics

### Initializers
- [init(rawValue: String)](./key/init%28rawvalue%29.md)
### Keys
- [static let identifier: NSLocale.Key](./key/identifier.md)
  The locale identifier.
- [static let countryCode: NSLocale.Key](./key/countrycode.md)
  The locale country or region code.
- [static let languageCode: NSLocale.Key](./key/languagecode.md)
  The locale language code.
- [static let scriptCode: NSLocale.Key](./key/scriptcode.md)
  The locale script code.
- [static let variantCode: NSLocale.Key](./key/variantcode.md)
  The locale variant code.
- [static let exemplarCharacterSet: NSLocale.Key](./key/exemplarcharacterset.md)
  The exemplar character set for the locale.
- [static let calendar: NSLocale.Key](./key/calendar.md)
  The calendar associated with the locale.
- [static let collationIdentifier: NSLocale.Key](./key/collationidentifier.md)
  The collation associated with the locale.
- [static let collatorIdentifier: NSLocale.Key](./key/collatoridentifier.md)
  The collation identifier for the locale.
- [static let usesMetricSystem: NSLocale.Key](./key/usesmetricsystem.md)
  A flag that indicates whether the locale uses the metric system.
- [static let measurementSystem: NSLocale.Key](./key/measurementsystem.md)
  The measurement system associated with the locale.
- [static let decimalSeparator: NSLocale.Key](./key/decimalseparator.md)
  The decimal separator associated with the locale.
- [static let groupingSeparator: NSLocale.Key](./key/groupingseparator.md)
  The numeric grouping separator associated with the locale.
- [static let currencySymbol: NSLocale.Key](./key/currencysymbol.md)
  The currency symbol associated with the locale.
- [static let currencyCode: NSLocale.Key](./key/currencycode.md)
  The currency code associated with the locale.
- [static let quotationEndDelimiterKey: NSLocale.Key](./key/quotationenddelimiterkey.md)
  The end quotation symbol associated with the locale.
- [static let quotationBeginDelimiterKey: NSLocale.Key](./key/quotationbegindelimiterkey.md)
  The begin quotation symbol associated with the locale.
- [static let alternateQuotationEndDelimiterKey: NSLocale.Key](./key/alternatequotationenddelimiterkey.md)
  The alternate end quotation symbol associated with the locale.
- [static let alternateQuotationBeginDelimiterKey: NSLocale.Key](./key/alternatequotationbegindelimiterkey.md)
  The alternating begin quotation symbol associated with the locale.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Locale Information by Key
- [func object(forKey: NSLocale.Key) -> Any?](./object%28forkey%29.md)
  Returns the value of the component corresponding to the specified key.
- [func displayName(forKey: NSLocale.Key, value: Any) -> String?](./displayname%28forkey,value%29.md)
  Returns the display name for the given locale component value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/key)*