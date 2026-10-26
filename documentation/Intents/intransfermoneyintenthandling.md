# INTransferMoneyIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for transferring money between accounts.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INTransferMoneyIntentHandling : NSObjectProtocol
```

```objc
@protocol INTransferMoneyIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INTransferMoneyIntentHandling`](./intransfermoneyintenthandling.md) protocol to resolve, confirm, and handle requests to transfer money between accounts. Adopt this protocol in an object of your Intents extension that’s capable of handling the transfer.

Siri delivers an [`INTransferMoneyIntent`](./intransfermoneyintent.md) object to your handler when the user asks to transfer money using your app. The provided intent object contains information about the amount to transfer and the accounts involved. Use the methods of this protocol to resolve the account information and initiate the transaction.

## Topics

### Resolving the Intent Parameters
- [func resolveFromAccount(for: INTransferMoneyIntent, with: (INPaymentAccountResolutionResult) -> Void)](./intransfermoneyintenthandling/resolvefromaccount%28for,with%29.md)
  Resolves the user account that’s the source of the funds.
- [func resolveToAccount(for: INTransferMoneyIntent, with: (INPaymentAccountResolutionResult) -> Void)](./intransfermoneyintenthandling/resolvetoaccount%28for,with%29.md)
  Resolves the user account that’s the destination of the funds.
- [func resolveTransactionAmount(for: INTransferMoneyIntent, with: (INPaymentAmountResolutionResult) -> Void)](./intransfermoneyintenthandling/resolvetransactionamount%28for,with%29.md)
  Resolves the amount that the user wants to transfer.
- [func resolveTransactionScheduledDate(for: INTransferMoneyIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./intransfermoneyintenthandling/resolvetransactionscheduleddate%28for,with%29.md)
  Resolves the date on which the transfer is to occur.
- [func resolveTransactionNote(for: INTransferMoneyIntent, with: (INStringResolutionResult) -> Void)](./intransfermoneyintenthandling/resolvetransactionnote%28for,with%29.md)
  Resolves any custom notes associated with the transaction.
### Confirming the Response
- [func confirm(intent: INTransferMoneyIntent, completion: (INTransferMoneyIntentResponse) -> Void)](./intransfermoneyintenthandling/confirm%28intent,completion%29.md)
  Confirms the transaction details and validates the transaciton.
### Handling the Intent
- [func handle(intent: INTransferMoneyIntent, completion: (INTransferMoneyIntentResponse) -> Void)](./intransfermoneyintenthandling/handle%28intent,completion%29.md)
  Handles the scheduling of the transfer.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INPaymentsDomainHandling](./inpaymentsdomainhandling.md)

## See Also

### Money Transfers
- [class INTransferMoneyIntent](./intransfermoneyintent.md)
  A request to transfer money between two accounts.
- [class INTransferMoneyIntentResponse](./intransfermoneyintentresponse.md)
  Your app’s response to a request to transfer money.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintenthandling)*