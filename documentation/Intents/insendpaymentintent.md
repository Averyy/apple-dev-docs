# INSendPaymentIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to transfer money from the current user’s account to a different user’s account.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INSendPaymentIntent
```

```objc
@interface INSendPaymentIntent : INIntent
```

#### Overview

Siri creates an [`INSendPaymentIntent`](./insendpaymentintent.md) object when the current user asks to transfer money to another user. A send payment intent object includes the payment amount and the recipient of the payment. Use that information to validate the transaction and transfer the funds.

To handle this intent, the handler object in your Intents extension must adopt the [`INSendPaymentIntentHandling`](./insendpaymentintenthandling.md) protocol. Your handler should confirm the request and create an [`INSendPaymentIntentResponse`](./insendpaymentintentresponse.md) object with the result of sending the money to the specified user.

This intent object represents a financial transaction between two users.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions, Shortcuts App |
| Always requires unlocked device | Yes |

When performing a search, Siri automatically asks the user to unlock a currently locked device. You don’t need to explicitly ask to unlock the device. In addition, Siri always prompts the user to confirm the payment before asking your Intents extension to handle the transaction.

## Topics

### Initializing the Intent Object
- [init(payee: INPerson?, currencyAmount: INCurrencyAmount?, note: String?)](./insendpaymentintent/init%28payee,currencyamount,note%29.md)
  Initializes the send payment intent object with the specified recipient and payment information.
### Getting Details About the Payment
- [var payee: INPerson?](./insendpaymentintent/payee.md)
  The recipient of the payment.
- [var currencyAmount: INCurrencyAmount?](./insendpaymentintent/currencyamount.md)
  The amount of the payment.
- [var note: String?](./insendpaymentintent/note.md)
  A note associated with the payment.

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

### Send a Payment
- [protocol INSendPaymentIntentHandling](./insendpaymentintenthandling.md)
  The handler interface for transferring money from the current user’s account to a different user’s account.
- [class INSendPaymentIntentResponse](./insendpaymentintentresponse.md)
  Your app’s response to a send payment intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintent)*