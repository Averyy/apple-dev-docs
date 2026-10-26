# balanceType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type associated with the balance.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var balanceType: INBalanceType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INBalanceType balanceType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INBalanceType balanceType;
```

#### Discussion

Use this property to determine how to interpret the value in the [`amount`](./amount.md) property.

## See Also

### Getting the Balance Information
- [var amount: NSDecimalNumber?](./amount.md)
  The numerical amount associated with the balance.
- [var currencyCode: String?](./currencycode.md)
  The ISO 4217 currency code that applies to a monetary amount.
- [enum INBalanceType](../inbalancetype.md)
  Constants indicating the meaning of a balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbalanceamount/balancetype)*