# amount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The numerical amount associated with the balance.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@NSCopying
var amount: NSDecimalNumber? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDecimalNumber * amount;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDecimalNumber * amount;
```

## Discussion

Use the [`balanceType`](./balancetype.md) property to determine the meaning of this value.

## See Also

### Getting the Balance Information
- [var currencyCode: String?](./currencycode.md)
  The ISO 4217 currency code that applies to a monetary amount.
- [var balanceType: INBalanceType](./balancetype.md)
  The type associated with the balance.
- [enum INBalanceType](../inbalancetype.md)
  Constants indicating the meaning of a balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbalanceamount/amount)*