# INTransferMoneyIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to transfer money between two accounts.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INTransferMoneyIntent
```

```objc
@interface INTransferMoneyIntent : INIntent
```

#### Overview

Siri creates an [`INTransferMoneyIntent`](./intransfermoneyintent.md) object when the user asks to transfer money between two accounts. Transfers can occur only between accounts associated with the user. Use the information provided by the intent object to identify the involved accounts and the amount to transfer.

To handle this intent, the handler object in your Intents extension must adopt the [`INTransferMoneyIntentHandling`](./intransfermoneyintenthandling.md) protocol. Your handler should confirm the request and create an [`INTransferMoneyIntentResponse`](./intransfermoneyintentresponse.md) object with the transaction details. For successful transfers, Siri offers a way for the user to view the results.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions |
| Always requires unlocked device | Yes |

When performing a search, Siri automatically asks the user to unlock a currently locked device. You don’t need to explicitly ask to unlock the device. In addition, Siri always prompts the user to confirm the request before asking your Intents extension to handle it.

## Topics

### Initializing the Intent Object
- [init(from: INPaymentAccount?, to: INPaymentAccount?, transactionAmount: INPaymentAmount?, transactionScheduledDate: INDateComponentsRange?, transactionNote: String?)](./intransfermoneyintent/init%28from,to,transactionamount,transactionscheduleddate,transactionnote%29.md)
  Initializes the intent object with the specified transaction details.
### Getting the Account Information
- [var fromAccount: INPaymentAccount?](./intransfermoneyintent/fromaccount.md)
  The account containing the funds to transfer.
- [var toAccount: INPaymentAccount?](./intransfermoneyintent/toaccount.md)
  The account receiving the funds.
### Getting the Transaction Details
- [var transactionAmount: INPaymentAmount?](./intransfermoneyintent/transactionamount.md)
  The amount to transfer.
- [var transactionScheduledDate: INDateComponentsRange?](./intransfermoneyintent/transactionscheduleddate.md)
  The date on which to transfer the funds.
- [var transactionNote: String?](./intransfermoneyintent/transactionnote.md)
  An optional note associated with the transaction.
### Initializers
- [init(fromAccount: INPaymentAccount?, toAccount: INPaymentAccount?, transactionAmount: INPaymentAmount?, transactionScheduledDate: INDateComponentsRange?, transactionNote: String?)](./intransfermoneyintent/init%28fromaccount,toaccount,transactionamount,transactionscheduleddate,transactionnote%29.md)

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Money Transfers
- [protocol INTransferMoneyIntentHandling](./intransfermoneyintenthandling.md)
  The handler interface for transferring money between accounts.
- [class INTransferMoneyIntentResponse](./intransfermoneyintentresponse.md)
  Your app’s response to a request to transfer money.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintent)*