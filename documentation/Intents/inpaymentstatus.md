# INPaymentStatus

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the financial transaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INPaymentStatus
```

```c
enum INPaymentStatus : NSInteger;
```

## Topics

### Constants
- [INPaymentStatus.unknown](./inpaymentstatus/unknown.md)
  The payment status is unknown.
- [INPaymentStatus.pending](./inpaymentstatus/pending.md)
  The app hasn’t sent the payment yet.
- [INPaymentStatus.completed](./inpaymentstatus/completed.md)
  The app made the payment.
- [INPaymentStatus.canceled](./inpaymentstatus/canceled.md)
  The app canceled the transaction before transferring the funds.
- [INPaymentStatus.failed](./inpaymentstatus/failed.md)
  The transaction failed and the funds were not transferred.
- [INPaymentStatus.unpaid](./inpaymentstatus/unpaid.md)
  The bill is currently unpaid.
### Initializers
- [init?(rawValue: Int)](./inpaymentstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data Objects
- [enum INAccountType](./inaccounttype.md)
  Constants indicating the type of account involved in a financial transaction.
- [class INCurrencyAmount](./incurrencyamount.md)
  An amount of money to transfer during a financial transaction.
- [class INPaymentAccount](./inpaymentaccount.md)
  A user account that provides the funds when making a payment.
- [class INPaymentAmount](./inpaymentamount.md)
  The amount of money to apply to a bill payment.
- [class INPaymentMethod](./inpaymentmethod.md)
  Information about a form of payment supported by your app.
- [class INPaymentRecord](./inpaymentrecord.md)
  Detailed information about a financial transaction made between two users.
- [class INPerson](./inperson.md)
  Information about a person participating in a SiriKit interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentstatus)*