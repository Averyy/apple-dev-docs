# INPayBillIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to pay a bill.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INPayBillIntentResponse
```

```objc
@interface INPayBillIntentResponse : INIntentResponse
```

## Overview

Use an [`INPayBillIntentResponse`](./inpaybillintentresponse.md) object to specify the details of the bill payment operation that you perform. After creating the object, fill in the details of the transaction, including the amount to transfer, the user account involved, the payee, and the date for the transaction to occur. Siri communicates the bill details back to the user at appropriate times.

You create an [`INPayBillIntentResponse`](./inpaybillintentresponse.md) object in the [`confirm(intent:completion:)`](./inpaybillintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./inpaybillintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INPayBillIntentHandling`](./inpaybillintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INPayBillIntentResponseCode, userActivity: NSUserActivity?)](./inpaybillintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INPayBillIntentResponseCode](./inpaybillintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INPayBillIntentResponseCode](./inpaybillintentresponsecode.md)
  Constants indicating the state of the response.
### Providing the Account Information
- [var fromAccount: INPaymentAccount?](./inpaybillintentresponse/fromaccount.md)
  The user account providing the funds.
### Providing the Transaction Details
- [var billDetails: INBillDetails?](./inpaybillintentresponse/billdetails.md)
  The details of the bill to pay.
- [var transactionAmount: INPaymentAmount?](./inpaybillintentresponse/transactionamount.md)
  The amount of money to transfer to the payee.
- [var transactionScheduledDate: INDateComponentsRange?](./inpaybillintentresponse/transactionscheduleddate.md)
  The date on which the transaction is to occur.
- [var transactionNote: String?](./inpaybillintentresponse/transactionnote.md)
  Notes to include with the transaction.

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

### Bill Payment
- [protocol INPayBillIntentHandling](./inpaybillintenthandling.md)
  The handler interface for paying a bill using money from the user’s account.
- [class INPayBillIntent](./inpaybillintent.md)
  A request to transfer money to facilitate payment of a bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintentresponse)*