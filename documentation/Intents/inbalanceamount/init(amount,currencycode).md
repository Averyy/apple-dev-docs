# init(amount:currencyCode:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a balance amount with a monetary amount.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(amount: NSDecimalNumber, currencyCode: String)
```

```objc
- (instancetype) initWithAmount:(NSDecimalNumber *) amount currencyCode:(NSString *) currencyCode;
```

#### Return Value

An initialized [`INBalanceAmount`](../inbalanceamount.md) object.

#### Discussion

Use this method to initialize balance amounts involving currencies. The [`balanceType`](./balancetype.md) property is automatically set to [`INBalanceType.money`](../inbalancetype/money.md).

## Parameters

- `amount`: The monetary amount to assign to the balance.
- `currencyCode`: The ISO 4217 currency code that applies to the monetary amount.

## See Also

### Initializing a Balance Amount Object
- [init?(amount: NSDecimalNumber, balanceType: INBalanceType)](./init%28amount,balancetype%29.md)
  Initializes a balance amount object with a customizable type of information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbalanceamount/init(amount:currencycode:))*