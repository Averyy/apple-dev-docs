# INBillDetails

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The detailed information associated with a bill.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INBillDetails
```

```objc
@interface INBillDetails : NSObject
```

## Overview

An [`INBillDetails`](./inbilldetails.md) object contains the details surrounding the payment of a bill. You create instances of this class when handling bill payment-related intents. For example, you create instances of this class when searching for the user’s bill payments. The details include the recipient of the funds, the amount that’s due, and the date of payment.

When creating instances of this class, specify as many details as possible. During searches or when paying a bill, Siri may display some of the bill details to the user. Omitting an important piece of information, such as the payee, might cause the user to cancel a bill payment.

## Topics

### Initializing the Bill Details
- [init?(billType: INBillType, paymentStatus: INPaymentStatus, billPayee: INBillPayee?, amountDue: INCurrencyAmount?, minimumDue: INCurrencyAmount?, lateFee: INCurrencyAmount?, dueDate: DateComponents?, paymentDate: DateComponents?)](./inbilldetails/init%28billtype,paymentstatus,billpayee,amountdue,minimumdue,latefee,duedate,paymentdate%29.md)
  Initializes a bill details object with information about the bill to pay.
### Accessing the Bill Information
- [var billPayee: INBillPayee?](./inbilldetails/billpayee.md)
  The entity receiving the payment.
- [var paymentDate: DateComponents?](./inbilldetails/paymentdate.md)
  The scheduled payment date for the bill.
- [var paymentStatus: INPaymentStatus](./inbilldetails/paymentstatus.md)
  The current status of the payment.
- [var billType: INBillType](./inbilldetails/billtype.md)
  The type of the bill.
### Getting the Bill Amount
- [var minimumDue: INCurrencyAmount?](./inbilldetails/minimumdue.md)
  The minimum amount to pay toward the bill.
- [var amountDue: INCurrencyAmount?](./inbilldetails/amountdue.md)
  The amount due for the bill.
- [var dueDate: DateComponents?](./inbilldetails/duedate.md)
  The due date of the payment.
- [var lateFee: INCurrencyAmount?](./inbilldetails/latefee.md)
  The late fee to apply if the payment is late.
### Constants
- [enum INBillType](./inbilltype.md)
  Constants indicating the type of bill.
### Initializers
- [init?(coder: NSCoder)](./inbilldetails/init%28coder%29.md)

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

### Bill Data Objects
- [class INBillPayee](./inbillpayee.md)
  The entity that receives the proceeds from a bill payment.
- [class INBillTypeResolutionResult](./inbilltyperesolutionresult.md)
  A resolution result for the types of bills a user might pay.
- [class INBillPayeeResolutionResult](./inbillpayeeresolutionresult.md)
  A resolution result for the recipient of a bill payment.
- [class INVisualCodeTypeResolutionResult](./invisualcodetyperesolutionresult.md)
  A resolution result for the type of visual code used to exchange information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilldetails)*