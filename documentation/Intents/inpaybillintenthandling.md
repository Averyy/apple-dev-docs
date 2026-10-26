# INPayBillIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for paying a bill using money from the user’s account.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INPayBillIntentHandling : NSObjectProtocol
```

```objc
@protocol INPayBillIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INPayBillIntentHandling`](./inpaybillintenthandling.md) protocol to resolve, confirm, and handle requests to pay bills. Adopt this protocol in an object of your Intents extension that’s capable of initiating the bill-payment process.

Siri delivers an [`INPayBillIntent`](./inpaybillintent.md) object to your handler when the user asks to pay a bill using your app. The provided intent object contains information about the bill, including the amount to pay and the organization to receive the money. Use the methods of this protocol to resolve the organization and payment details and initiate the transaction.

## Topics

### Resolving the Intent Parameters
- [func resolveBillPayee(for: INPayBillIntent, with: (INBillPayeeResolutionResult) -> Void)](./inpaybillintenthandling/resolvebillpayee%28for,with%29.md)
  Resolves the entity that originated the bill.
- [func resolveBillType(for: INPayBillIntent, with: (INBillTypeResolutionResult) -> Void)](./inpaybillintenthandling/resolvebilltype%28for,with%29.md)
  Resolves the type of the bill.
- [func resolveFromAccount(for: INPayBillIntent, with: (INPaymentAccountResolutionResult) -> Void)](./inpaybillintenthandling/resolvefromaccount%28for,with%29.md)
  Resolves the user account that provides the funds for paying the bill.
- [func resolveTransactionAmount(for: INPayBillIntent, with: (INPaymentAmountResolutionResult) -> Void)](./inpaybillintenthandling/resolvetransactionamount%28for,with%29.md)
  Resolves the amount to pay toward the bill.
- [func resolveDueDate(for: INPayBillIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./inpaybillintenthandling/resolveduedate%28for,with%29.md)
  Resolves the due date of the bill.
- [func resolveTransactionScheduledDate(for: INPayBillIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./inpaybillintenthandling/resolvetransactionscheduleddate%28for,with%29.md)
  Resolves the date for the payment to occur.
- [func resolveTransactionNote(for: INPayBillIntent, with: (INStringResolutionResult) -> Void)](./inpaybillintenthandling/resolvetransactionnote%28for,with%29.md)
  Resolves any custom notes associated with the transaction.
### Confirming the Response
- [func confirm(intent: INPayBillIntent, completion: (INPayBillIntentResponse) -> Void)](./inpaybillintenthandling/confirm%28intent,completion%29.md)
  Confirms the transaction details.
### Handling the Intent
- [func handle(intent: INPayBillIntent, completion: (INPayBillIntentResponse) -> Void)](./inpaybillintenthandling/handle%28intent,completion%29.md)
  Handles scheduling payment of the bill.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INPaymentsDomainHandling](./inpaymentsdomainhandling.md)

## See Also

### Bill Payment
- [class INPayBillIntent](./inpaybillintent.md)
  A request to transfer money to facilitate payment of a bill.
- [class INPayBillIntentResponse](./inpaybillintentresponse.md)
  Your app’s response to a request to pay a bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintenthandling)*