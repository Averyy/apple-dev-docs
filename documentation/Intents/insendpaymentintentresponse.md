# INSendPaymentIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a send payment intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INSendPaymentIntentResponse
```

```objc
@interface INSendPaymentIntentResponse : INIntentResponse
```

#### Overview

Use an [`INSendPaymentIntentResponse`](./insendpaymentintentresponse.md) object to specify the details of the financial transaction that you perform. After creating the object, assign the details of the payment transaction to the [`paymentRecord`](./insendpaymentintentresponse/paymentrecord.md) property, the details of which Siri communicates to the user at appropriate times.

You create an [`INSendPaymentIntentResponse`](./insendpaymentintentresponse.md) object in the [`confirm(intent:completion:)`](./insendpaymentintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insendpaymentintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INSendPaymentIntentHandling`](./insendpaymentintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSendPaymentIntentResponseCode, userActivity: NSUserActivity?)](./insendpaymentintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSendPaymentIntentResponseCode](./insendpaymentintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSendPaymentIntentResponseCode](./insendpaymentintentresponsecode.md)
  Constants indicating the state of the response.
### Accessing the Payment Information
- [var paymentRecord: INPaymentRecord?](./insendpaymentintentresponse/paymentrecord.md)
  The details of the payment transaction.

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

### Send a Payment
- [protocol INSendPaymentIntentHandling](./insendpaymentintenthandling.md)
  The handler interface for transferring money from the current user’s account to a different user’s account.
- [class INSendPaymentIntent](./insendpaymentintent.md)
  A request to transfer money from the current user’s account to a different user’s account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintentresponse)*