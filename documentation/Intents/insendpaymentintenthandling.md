# INSendPaymentIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for transferring money from the current user’s account to a different user’s account.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INSendPaymentIntentHandling : NSObjectProtocol
```

```objc
@protocol INSendPaymentIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INSendPaymentIntentHandling`](./insendpaymentintenthandling.md) protocol to resolve, confirm, and handle requests to send money to another user of your app. Adopt this protocol in an object of your Intents extension that is capable of performing the financial transaction.

Siri delivers an [`INSendPaymentIntent`](./insendpaymentintent.md) object to your handler when the user asks to send a payment using your app. The provided intent object contains the details of the payment, including the recipient, the amount to transfer, and any memos associated with the payment. Use the methods of this protocol to resolve the payment parameters and to validate that the payment is possible.

## Topics

### Resolving the Intent Parameters
- [func resolvePayee(for: INSendPaymentIntent, with: (INSendPaymentPayeeResolutionResult) -> Void)](./insendpaymentintenthandling/resolvepayee%28for,with%29-3otmy.md)
  Resolves the recipient for a payment.
- [func resolveCurrencyAmount(for: INSendPaymentIntent, with: (INSendPaymentCurrencyAmountResolutionResult) -> Void)](./insendpaymentintenthandling/resolvecurrencyamount%28for,with%29-75c7o.md)
  Resolves the amount of currency to transfer.
- [func resolveNote(for: INSendPaymentIntent, with: (INStringResolutionResult) -> Void)](./insendpaymentintenthandling/resolvenote%28for,with%29.md)
  Resolves the notes associated with the transaction.
- [func resolvePayee(for: INSendPaymentIntent, with: (INPersonResolutionResult) -> Void)](./insendpaymentintenthandling/resolvepayee%28for,with%29-1kh1g.md)
  Called when you need to resolve the recipient of the funds.
- [func resolveCurrencyAmount(for: INSendPaymentIntent, with: (INCurrencyAmountResolutionResult) -> Void)](./insendpaymentintenthandling/resolvecurrencyamount%28for,with%29-9vd94.md)
  Called when you need to resolve the currency amount to be transferred.
### Confirming the Response
- [func confirm(intent: INSendPaymentIntent, completion: (INSendPaymentIntentResponse) -> Void)](./insendpaymentintenthandling/confirm%28intent,completion%29.md)
  Confirms the transaction and details.
### Handling the Intent
- [func handle(intent: INSendPaymentIntent, completion: (INSendPaymentIntentResponse) -> Void)](./insendpaymentintenthandling/handle%28intent,completion%29.md)
  Handles transferring the money between accounts.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INPaymentsDomainHandling](./inpaymentsdomainhandling.md)

## See Also

### Send a Payment
- [class INSendPaymentIntent](./insendpaymentintent.md)
  A request to transfer money from the current user’s account to a different user’s account.
- [class INSendPaymentIntentResponse](./insendpaymentintentresponse.md)
  Your app’s response to a send payment intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintenthandling)*