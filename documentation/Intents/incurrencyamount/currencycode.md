# currencyCode

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The ISO 4217 currency code that applies to the monetary amount.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var currencyCode: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * currencyCode;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * currencyCode;
```

#### Discussion

Use this value to determine the appropriate currency designator to apply to the value in the [`amount`](./amount.md) property. To retrieve the list of available currency codes, call the [`isoCurrencyCodes`](../../Foundation/nslocale/isocurrencycodes.md) method of the [`NSLocale`](../../Foundation/nslocale.md) class.

## See Also

### Getting the Currency Information
- [var amount: NSDecimalNumber?](./amount.md)
  The monetary amount associated with the currency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incurrencyamount/currencycode)*