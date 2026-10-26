# INPaymentRecord

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Detailed information about a financial transaction made between two users.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPaymentRecord
```

```objc
@interface INPaymentRecord : NSObject
```

#### Overview

An [`INPaymentRecord`](./inpaymentrecord.md) object contains the details of a financial transaction that your app is facilitating. You create instances of this class when handling payment-related intents. The payment record contains the users involved in the transaction, the amount of money to transfer, and the current state of the transaction. Siri conveys this detailed information to the user at appropriate times.

When creating payment records, specify as many details as possible. Siri always asks the user to confirm payments before asking your Intents extension to process them. During confirmation, Siri displays the information from this object in the confirmation interface. Omitting important pieces of information, such as the recipient or currency amount, might cause the user to cancel the transaction.

## Topics

### Creating a Payment Record Object
- [init?(payee: INPerson?, payer: INPerson?, currencyAmount: INCurrencyAmount?, paymentMethod: INPaymentMethod?, note: String?, status: INPaymentStatus, feeAmount: INCurrencyAmount?)](./inpaymentrecord/init%28payee,payer,currencyamount,paymentmethod,note,status,feeamount%29.md)
  Initializes a payment record with the specified payment details.
- [convenience init?(payee: INPerson?, payer: INPerson?, currencyAmount: INCurrencyAmount?, paymentMethod: INPaymentMethod?, note: String?, status: INPaymentStatus)](./inpaymentrecord/init%28payee,payer,currencyamount,paymentmethod,note,status%29.md)
  Initializes a payment record with the specified payment details.
### Getting the Payment Status
- [var status: INPaymentStatus](./inpaymentrecord/status.md)
  The current status of the financial transaction.
### Getting Payment Record Details
- [var payee: INPerson?](./inpaymentrecord/payee.md)
  The person receiving the funds.
- [var payer: INPerson?](./inpaymentrecord/payer.md)
  The person providing the funds.
- [var currencyAmount: INCurrencyAmount?](./inpaymentrecord/currencyamount.md)
  The type of currency to transfer and the amount to transfer.
- [var feeAmount: INCurrencyAmount?](./inpaymentrecord/feeamount.md)
  The total amount of any fees added to the payment record.
- [var paymentMethod: INPaymentMethod?](./inpaymentrecord/paymentmethod.md)
  The payment method used to supply the funds.
- [var note: String?](./inpaymentrecord/note.md)
  A description of the payment to send.
### Initializers
- [init?(coder: NSCoder)](./inpaymentrecord/init%28coder%29.md)

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
- [class INPaymentAmount](./inpaymentamount.md)
  The amount of money to apply to a bill payment.
- [class INPaymentMethod](./inpaymentmethod.md)
  Information about a form of payment supported by your app.
- [enum INPaymentStatus](./inpaymentstatus.md)
  Constants indicating the state of the financial transaction.
- [class INPerson](./inperson.md)
  Information about a person participating in a SiriKit interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentrecord)*