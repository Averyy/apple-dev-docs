# init(amount:balanceType:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a balance amount object with a customizable type of information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init?(amount: NSDecimalNumber, balanceType: INBalanceType)
```

```objc
- (instancetype) initWithAmount:(NSDecimalNumber *) amount balanceType:(INBalanceType) balanceType;
```

#### Return Value

An initialized [`INBalanceAmount`](../inbalanceamount.md) object.

#### Discussion

Use this method when initializing balance amounts that do not involve money.

> ❗ **Important**:  When initializing a balance involving money, use the [`init(amount:currencyCode:)`](./init%28amount,currencycode%29.md) method instead. Using that initializer method lets you specify the currency associated with the monetary amount.

## Parameters

- `amount`: The numerical amount associated with the balance.
- `balanceType`: The type that indicates what the balance represents. For a list of possible values, see [`INBalanceType`](../inbalancetype.md).

## See Also

### Initializing a Balance Amount Object
- [init(amount: NSDecimalNumber, currencyCode: String)](./init%28amount,currencycode%29.md)
  Initializes a balance amount with a monetary amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbalanceamount/init(amount:balancetype:))*