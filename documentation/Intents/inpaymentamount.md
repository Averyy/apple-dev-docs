# INPaymentAmount

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The amount of money to apply to a bill payment.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPaymentAmount
```

```objc
@interface INPaymentAmount : NSObject
```

## Overview

An [`INPaymentAmount`](./inpaymentamount.md) object describes the amount of money to pay toward a bill. When handling bill payments, Siri may provide an instance of this class with the amount that the user wants to pay. When handling the intent, you also create instances of the class with the amount of money that you scheduled toward the user’s bill.

When receiving an instance of this class from Siri, the amount type might be specified using only an [`INAmountType`](./inamounttype.md) constant, such as [`INAmountType.minimumDue`](./inamounttype/minimumdue.md) or [`INAmountType.currentBalance`](./inamounttype/currentbalance.md). During resolution or when confirming the amount type, you should always supply a value in the [`amount`](./inpaymentamount/amount.md) property in addition to the amount type constant. When communicating with the user, Siri always displays the actual amount of money to be applied to a bill.

## Topics

### Initializing the Payment Amount
- [init(amountType: INAmountType, amount: INCurrencyAmount)](./inpaymentamount/init%28amounttype,amount%29.md)
  Initializes a payment amount object with the specified amounts.
### Getting the Payment Amount
- [var amount: INCurrencyAmount?](./inpaymentamount/amount.md)
  The precise amount of money to pay.
- [var amountType: INAmountType](./inpaymentamount/amounttype.md)
  The account-specific amount to pay.
- [enum INAmountType](./inamounttype.md)
  Constants indicating an account-specific amount to apply to a payment.
### Initializers
- [init?(coder: NSCoder)](./inpaymentamount/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Data Objects
- [enum INAccountType](./inaccounttype.md)
  Constants indicating the type of account involved in a financial transaction.
- [class INCurrencyAmount](./incurrencyamount.md)
  An amount of money to transfer during a financial transaction.
- [class INPaymentAccount](./inpaymentaccount.md)
  A user account that provides the funds when making a payment.
- [class INPaymentMethod](./inpaymentmethod.md)
  Information about a form of payment supported by your app.
- [class INPaymentRecord](./inpaymentrecord.md)
  Detailed information about a financial transaction made between two users.
- [enum INPaymentStatus](./inpaymentstatus.md)
  Constants indicating the state of the financial transaction.
- [class INPerson](./inperson.md)
  Information about a person participating in a SiriKit interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentamount)*