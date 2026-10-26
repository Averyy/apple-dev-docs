# INTransferMoneyIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to transfer money.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INTransferMoneyIntentResponse
```

```objc
@interface INTransferMoneyIntentResponse : INIntentResponse
```

#### Overview

Use an [`INTransferMoneyIntentResponse`](./intransfermoneyintentresponse.md) object to specify the details of the transfer operation that you perform. After creating the object, fill in the details of the transaction, including the amount to transfer, the accounts involved, and the date to make the transaction. Siri communicates the details back to the user at appropriate times.

You create an [`INTransferMoneyIntentResponse`](./intransfermoneyintentresponse.md) object in the [`confirm(intent:completion:)`](./intransfermoneyintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./intransfermoneyintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INPayBillIntentHandling`](./inpaybillintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INTransferMoneyIntentResponseCode, userActivity: NSUserActivity?)](./intransfermoneyintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INTransferMoneyIntentResponseCode](./intransfermoneyintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INTransferMoneyIntentResponseCode](./intransfermoneyintentresponsecode.md)
  Constants indicating the state of the response.
### Providing the Account Information
- [var fromAccount: INPaymentAccount?](./intransfermoneyintentresponse/fromaccount.md)
  The user account providing the funds.
- [var toAccount: INPaymentAccount?](./intransfermoneyintentresponse/toaccount.md)
  The user account receiving the funds.
### Providing the Transaction Details
- [var transactionAmount: INPaymentAmount?](./intransfermoneyintentresponse/transactionamount.md)
  The amount of money to transfer between accounts.
- [var transactionScheduledDate: INDateComponentsRange?](./intransfermoneyintentresponse/transactionscheduleddate.md)
  The date on which the transfer is to occur.
- [var transactionNote: String?](./intransfermoneyintentresponse/transactionnote.md)
  Notes to include with the transaction.
- [var transferFee: INCurrencyAmount?](./intransfermoneyintentresponse/transferfee.md)
  The fee charged for performing the transaction.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
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

### Money Transfers
- [protocol INTransferMoneyIntentHandling](./intransfermoneyintenthandling.md)
  The handler interface for transferring money between accounts.
- [class INTransferMoneyIntent](./intransfermoneyintent.md)
  A request to transfer money between two accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintentresponse)*