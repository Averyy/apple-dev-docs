# INRequestPaymentIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An intent for requesting money from another user’s account.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INRequestPaymentIntent
```

```objc
@interface INRequestPaymentIntent : INIntent
```

## Overview

Siri creates an [`INRequestPaymentIntent`](./inrequestpaymentintent.md) object when the current user requests a payment from another user. A request payment intent object includes the payment amount and the person receiving the request. This intent represents only a request for payment and shouldn’t initiate any payments.

To handle this intent, the handler object in your Intents extension must adopt the [`INRequestPaymentIntentHandling`](./inrequestpaymentintenthandling.md) protocol. Your handler should confirm the request and create an [`INRequestPaymentIntentResponse`](./inrequestpaymentintentresponse.md) object with the results of making the request.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions, Shortcuts app |
| Always requires unlocked device | Yes |

When performing a search, Siri automatically asks the user to unlock a currently locked device. You don’t need to explicitly ask to unlock the device. In addition, Siri always prompts the user to confirm the request before asking your Intents extension to handle it.

## Topics

### Initializing the Intent Object
- [init(payer: INPerson?, currencyAmount: INCurrencyAmount?, note: String?)](./inrequestpaymentintent/init%28payer,currencyamount,note%29.md)
  Initializes the request payment intent object with the specified recipient and payment information.
### Getting Details About the Payment
- [var payer: INPerson?](./inrequestpaymentintent/payer.md)
  The recipient of the payment request.
- [var currencyAmount: INCurrencyAmount?](./inrequestpaymentintent/currencyamount.md)
  The amount of the payment.
- [var note: String?](./inrequestpaymentintent/note.md)
  A note associated with the request.

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

### Request a Payment
- [protocol INRequestPaymentIntentHandling](./inrequestpaymentintenthandling.md)
  The handler interface for delivering a request for payment from another user of your app.
- [class INRequestPaymentIntentResponse](./inrequestpaymentintentresponse.md)
  Your app’s response to a request payment intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintent)*