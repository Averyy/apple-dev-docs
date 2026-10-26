# INRequestPaymentIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for delivering a request for payment from another user of your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INRequestPaymentIntentHandling : NSObjectProtocol
```

```objc
@protocol INRequestPaymentIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INRequestPaymentIntentHandling`](./inrequestpaymentintenthandling.md) protocol to resolve, confirm, and handle the requesting of money from another user of your app. Adopt this protocol in an object of your Intents extension that is capable of contacting the designated user and communicating the request for payment.

Siri delivers an [`INRequestPaymentIntent`](./inrequestpaymentintent.md) object to your handler when the user makes a request for payment using your app. The provided intent object contains the details of the payment request, including the recipient of the request, the amount of the payment, and any memos associated with the payment. Use the methods of this protocol to resolve the payment parameters and to validate that the payment is possible.

## Topics

### Resolving the Intent Parameters
- [func resolvePayer(for: INRequestPaymentIntent, with: (INRequestPaymentPayerResolutionResult) -> Void)](./inrequestpaymentintenthandling/resolvepayer%28for,with%29-4xu87.md)
  Resolves the person to receive the payment request.
- [func resolveCurrencyAmount(for: INRequestPaymentIntent, with: (INRequestPaymentCurrencyAmountResolutionResult) -> Void)](./inrequestpaymentintenthandling/resolvecurrencyamount%28for,with%29-1it85.md)
  Resolves the amount of money requested.
- [func resolveNote(for: INRequestPaymentIntent, with: (INStringResolutionResult) -> Void)](./inrequestpaymentintenthandling/resolvenote%28for,with%29.md)
  Resolves the notes associated with the request.
- [func resolvePayer(for: INRequestPaymentIntent, with: (INPersonResolutionResult) -> Void)](./inrequestpaymentintenthandling/resolvepayer%28for,with%29-qp42.md)
  Called when you need to resolve the person who will receive the payment request.
- [func resolveCurrencyAmount(for: INRequestPaymentIntent, with: (INCurrencyAmountResolutionResult) -> Void)](./inrequestpaymentintenthandling/resolvecurrencyamount%28for,with%29-78c2m.md)
  Called when you need to resolve the amount of money being requested.
### Confirming the Response
- [func confirm(intent: INRequestPaymentIntent, completion: (INRequestPaymentIntentResponse) -> Void)](./inrequestpaymentintenthandling/confirm%28intent,completion%29.md)
  Confirms the payment request and confirm the details.
### Handling the Intent
- [func handle(intent: INRequestPaymentIntent, completion: (INRequestPaymentIntentResponse) -> Void)](./inrequestpaymentintenthandling/handle%28intent,completion%29.md)
  Handles sending the payment request to the designated user.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INPaymentsDomainHandling](./inpaymentsdomainhandling.md)

## See Also

### Request a Payment
- [class INRequestPaymentIntent](./inrequestpaymentintent.md)
  An intent for requesting money from another user’s account.
- [class INRequestPaymentIntentResponse](./inrequestpaymentintentresponse.md)
  Your app’s response to a request payment intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintenthandling)*