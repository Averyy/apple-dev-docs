# currencyCode

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The ISO 4217 currency code that applies to a monetary amount.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

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

### Getting the Balance Information
- [var amount: NSDecimalNumber?](./amount.md)
  The numerical amount associated with the balance.
- [var balanceType: INBalanceType](./balancetype.md)
  The type associated with the balance.
- [enum INBalanceType](../inbalancetype.md)
  Constants indicating the meaning of a balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbalanceamount/currencycode)*