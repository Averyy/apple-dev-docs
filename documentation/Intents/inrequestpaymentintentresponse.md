# INRequestPaymentIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request payment intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INRequestPaymentIntentResponse
```

```objc
@interface INRequestPaymentIntentResponse : INIntentResponse
```

#### Overview

Use an [`INRequestPaymentIntentResponse`](./inrequestpaymentintentresponse.md) object to specify the details of a payment request that you make. After creating the object, assign the details of the payment transaction to the [`paymentRecord`](./inrequestpaymentintentresponse/paymentrecord.md) property, the details of which Siri communicates to the user at appropriate times.

You create an [`INRequestPaymentIntentResponse`](./inrequestpaymentintentresponse.md) object in the [`confirm(intent:completion:)`](./inrequestpaymentintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./inrequestpaymentintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INRequestPaymentIntentHandling`](./inrequestpaymentintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INRequestPaymentIntentResponseCode, userActivity: NSUserActivity?)](./inrequestpaymentintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INRequestPaymentIntentResponseCode](./inrequestpaymentintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INRequestPaymentIntentResponseCode](./inrequestpaymentintentresponsecode.md)
  Constants indicating the state of the response.
### Accessing the Response Data
- [var paymentRecord: INPaymentRecord?](./inrequestpaymentintentresponse/paymentrecord.md)
  The details of the request.

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

### Request a Payment
- [protocol INRequestPaymentIntentHandling](./inrequestpaymentintenthandling.md)
  The handler interface for delivering a request for payment from another user of your app.
- [class INRequestPaymentIntent](./inrequestpaymentintent.md)
  An intent for requesting money from another user’s account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintentresponse)*